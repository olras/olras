# %%
import kwant
import numpy as np
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt

sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
identity = np.eye(2)

# Sublattice space (A and B)
tau_x = sigma_x  # Hopping between sublattices
tau_y = sigma_y  # Hopping between sublattices with a phase
tau_z = sigma_z  # Onsite potential difference between sublattices
tau_0 = identity  # Identity in sublattice space

W_SC = 20
W_N = 5

lat = kwant.lattice.square(norbs=4)

def ham_sc(Delta, phi=0):
    Delta *= np.exp(1j * phi)
    return np.kron(np.real(Delta) * tau_x + np.imag(Delta) * tau_y, tau_0)


def onsite(site, mu, tx, Delta, phi, mu_sc):
    x = site.pos[0]
    onsite_term = (2 * tx - mu) * np.kron(tau_z, tau_0)
    if x <= -W_N / 2:
        onsite_term += ham_sc(Delta, phi) - (mu_sc - mu) * np.kron(tau_z, tau_0)
    elif x > W_N / 2:
        onsite_term += ham_sc(Delta) - (mu_sc - mu) * np.kron(tau_z, tau_0)
    return onsite_term


def hopping(site1, site2, tx, ty, alpha_x, alpha_y):
    """Hopping term between two sites."""
    if site1.pos[0] == site2.pos[0]:
        normal_hopping = ty * np.kron(tau_z, tau_0)  # Normal hopping term
        soc_hopping = 1j * alpha_y * np.kron(tau_z, tau_x)
        return normal_hopping + soc_hopping
    elif site1.pos[1] == site2.pos[1]:
        normal_hopping = tx * np.kron(tau_z, tau_0)  # Normal hopping term
        soc_hopping = -1j * alpha_x * np.kron(tau_z, tau_y)
        return normal_hopping + soc_hopping


def abs_syst(W_SC, W_N, t=1, sym=None):
    if sym:
        sym = kwant.TranslationalSymmetry(lat.vec((1, 0)))
    syst = kwant.Builder(sym)
    syst[
        (
            lat(x, y)
            for x in np.arange(-W_SC - W_N // 2, W_SC + 1 + W_N // 2)
            for y in range(2)
        )
    ] = onsite
    syst[lat.neighbors()] = hopping
    return syst


# %%
default_params = dict(
    mu=-0.15, mu_sc=-0.15, tx=1, ty=0.2, Delta=0.2, phi=0, alpha_x=0.5, alpha_y=0.2
)
wrapped_syst = kwant.wraparound.wraparound(abs_syst(W_SC, 0, sym=True)).finalized()
Sy = kwant.operator.Density(wrapped_syst, np.kron(tau_0, tau_y), sum=True)
Q = kwant.operator.Density(wrapped_syst, np.kron(tau_z, tau_0), sum=True)

ks = np.linspace(0, 2 * np.pi, 201)
from scipy.linalg import eigh

eig = []
spin = []
charge = []
for k in ks:
    ham = wrapped_syst.hamiltonian_submatrix(
        params={"k_x": k, **default_params}, sparse=False
    )
    vals, vecs = eigh(ham)
    eig.append(np.sort(vals))
    spin.append(np.array([Sy(psi) for psi in vecs.T]))
    charge.append(np.array([Q(psi) for psi in vecs.T]))
eig = np.array(eig)
spin = np.array(spin)
charge = np.array(charge)

# %%
electron_bands = eig[charge > 0].reshape(len(ks), -1)
electron_spin = spin[charge > 0].reshape(len(ks), -1)
for i, neig in enumerate(electron_bands.T):
    plt.scatter(
        ks, np.array(neig), c=electron_spin[:, i], cmap="coolwarm", s=5, vmax=1, vmin=-1
    )
plt.ylim(-1, 1)
plt.axhline(0, color="black", linestyle="--")
plt.show()

# %%
import xarray as xr

ds_bands = xr.Dataset(
    {
        "energy": (["k", "band"], eig),
        "spin": (["k", "band"], spin),
        "charge": (["k", "band"], charge),
    },
    coords={
        "k": ks,
        "band": np.arange(eig.shape[1]),
    },
)

# %%
# Filter the dataset where charge > 0
filtered_ds = ds_bands.where(ds_bands.charge > 0, drop=True)

# Plot k vs energy for all bands (filtered), grouped by band, without legends
plot = filtered_ds.hvplot.scatter(
    x="k",
    y="energy",
    c="spin",  # Color by spin
    by="band",  # Separate bands
    title="k vs Energy for All Bands (Filtered by Charge > 0)",
    colorbar=True,
    legend=False,  # Remove legends
)

plot

# %%
# Filter the dataset where charge > 0
filtered_ds = ds_bands.where(ds_bands.charge > 0, drop=True)

# Plot k vs energy for all bands (filtered), grouped by band, without legends
plot = filtered_ds.hvplot.scatter(
    x="k",
    y="energy",
    c="spin",  # Color by spin
    by="band",  # Separate bands
    title="k vs Energy for All Bands (Filtered by Charge > 0)",
    colorbar=True,
    legend=False,  # Remove legends
)

plot

# %%
import matplotlib.pyplot as plt

# Filter the dataset where charge > 0
filtered_ds = ds_bands.where(ds_bands.charge > 0, drop=True)

# Ensure consistent filtering by stacking dimensions
filtered_ds = filtered_ds.stack(flat_dim=("band", "k")).dropna(
    dim="flat_dim", how="any"
)

# Extract data for plotting
k = filtered_ds.k.values  # Extract k values
energy = filtered_ds.energy.values  # Extract energy values
spin = filtered_ds.spin.values  # Extract spin values

# Create the scatter plot
plt.figure(figsize=(8, 6))
sc = plt.scatter(
    filtered_ds.k,
    filtered_ds.energy,
    c=filtered_ds.spin.values,
    cmap="coolwarm",
    edgecolor=None,
)
plt.colorbar(sc, label="Spin")  # Add a colorbar for spin
plt.xlabel("k")
plt.ylabel("Energy")
plt.title("k vs Energy (Filtered by Charge > 0)")
plt.grid()
plt.show()

# %%
N_states = 16
syst = abs_syst(W_SC, W_N).finalized()
eig = []
phis = np.linspace(0, 2 * np.pi, 51)
for phi in phis:
    ham = syst.hamiltonian_submatrix(params={**default_params, "phi": phi}, sparse=True)
    values = eigsh(ham, sigma=0, k=N_states, return_eigenvectors=False)
    eig.append(np.sort(values))

plt.plot(phis, np.array(eig))
plt.show()
