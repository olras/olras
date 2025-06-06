# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: default
#     language: python
#     name: python3
# ---

# %%
import kwant
import numpy as np
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
import hvplot.xarray
from scipy.linalg import eigh
from itertools import product

# Define the Pauli matrices and identity matrix for spinor representation
tau_x = np.array([[0, 1], [1, 0]], dtype=complex)
tau_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
tau_z = np.array([[1, 0], [0, -1]], dtype=complex)
tau_0 = np.eye(2)


def ham_sc(Delta, phi=0):
    """Pairing potential.
    Parameters
    ----------
    Delta : complex
        Superconducting pairing potential.
    phi : float
        Phase of the superconducting pairing potential.
    Returns
    -------
    numpy.ndarray
        Superconducting pairing Hamiltonian term.
    """
    Delta *= np.exp(1j * phi)
    return np.kron(np.real(Delta) * tau_x + np.imag(Delta) * tau_y, tau_0)


def onsite(site, mu, tx, Delta, phi, mu_sc, W_N):
    """Onsite term for the Hamiltonian.
    Includes superconducting pairing and chemical potential.
    Parameters
    ----------
    site : kwant.Site
        The site for which the onsite term is calculated.
    mu : float
        Chemical potential.
    tx : float
        Hopping parameter in the x-direction.
    Delta : complex
        Superconducting pairing potential.
    phi : float
        Phase of the superconducting pairing potential.
    mu_sc : float
        Chemical potential in the superconducting region.
    Returns
    -------
    numpy.ndarray
        Onsite Hamiltonian term for the site.
    """
    x = site.pos[0]
    onsite_term = (2 * tx - mu) * np.kron(tau_z, tau_0)
    if x <= -W_N / 2:
        onsite_term += ham_sc(Delta, phi) - (mu_sc - mu) * np.kron(tau_z, tau_0)
    elif x > W_N / 2:
        onsite_term += ham_sc(Delta) - (mu_sc - mu) * np.kron(tau_z, tau_0)
    return onsite_term


def hopping(site1, site2, tx, ty, alpha_x, alpha_y):
    """Hopping term between two sites.
    Parameters
    ----------
    site1 : kwant.Site
        The first site.
    site2 : kwant.Site
        The second site.
    tx : float
        Hopping parameter in the x-direction.
    ty : float
        Hopping parameter in the y-direction.
    alpha_x : float
        Spin-orbit coupling in the x-direction.
    alpha_y : float
        Spin-orbit coupling in the y-direction.
    Returns
    -------
    numpy.ndarray
        Hopping Hamiltonian term between the two sites.
    """
    if site1.pos[0] == site2.pos[0]:
        normal_hopping = ty * np.kron(tau_z, tau_0)  # Normal hopping term
        soc_hopping = 1j * alpha_y * np.kron(tau_z, tau_x)
        return normal_hopping + soc_hopping
    elif site1.pos[1] == site2.pos[1]:
        normal_hopping = tx * np.kron(tau_z, tau_0)  # Normal hopping term
        soc_hopping = -1j * alpha_x * np.kron(tau_z, tau_y)
        return normal_hopping + soc_hopping


def abs_syst(W_SC, W_N, sym=None):
    """
    Constructs a system with superconducting and normal regions.
    Parameters
    ----------
    W_SC : int
        Width of the superconducting region.
    W_N : int
        Width of the normal region.
    t : float
        Hopping parameter.
    sym : kwant.TranslationalSymmetry or None
        Translational symmetry of the system.
    Returns
    -------
    syst : kwant.Builder
        The constructed system.
    """
    lat = kwant.lattice.square(norbs=4)
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
def compute_electron_bands(params, wrapped_syst, charge_op, spin_op, num_bands=16):
    """
    Computes the electron bands of the system.
    Parameters
    ----------
    syst : kwant.Builder
        The system for which to compute the bands.
    num_bands : int
        Number of bands to compute.
    Returns
    -------
    energies : numpy.ndarray
        Energies of the computed bands.
    """
    ham = wrapped_syst.hamiltonian_submatrix(params=params, sparse=False)
    vals, vecs = eigh(ham)
    spin = np.array([spin_op(psi) for psi in vecs.T])
    charge = np.array([charge_op(psi) for psi in vecs.T])
    return vals, spin, charge


def compute_andreev_spectrum(params, syst, num_states):
    """
    Computes the Andreev spectrum for a given phase.
    Parameters
    ----------
    phi : float
        Phase of the superconducting pairing potential.
    wrapped_syst : kwant.Builder
        The system for which to compute the Andreev spectrum.
    charge_op : function
        Function to compute the charge operator.
    spin_op : function
        Function to compute the spin operator.
    num_bands : int
        Number of bands to compute.
    Returns
    -------
    energies : numpy.ndarray
        Energies of the Andreev spectrum.
    """
    ham = syst.hamiltonian_submatrix(params=params, sparse=True)
    vals, vecs = eigsh(ham, sigma=0, k=num_states, return_eigenvectors=True)
    return np.sort(vals)


# %%
default_params = dict(
    mu=-0.15, mu_sc=-0.15, tx=1, ty=0.2, Delta=0.2, phi=0, alpha_x=0.5, alpha_y=0.2, W_N=1
)
wrapped_syst = kwant.wraparound.wraparound(abs_syst(0, 0, sym=True)).finalized()
Sy = kwant.operator.Density(wrapped_syst, np.kron(tau_0, tau_y), sum=True)
Q = kwant.operator.Density(wrapped_syst, np.kron(tau_z, tau_0), sum=True)
ks = np.linspace(0, 2 * np.pi, 201)
alphas = np.linspace(0, default_params["alpha_y"], 3)

# %%
results = []
for k, alpha in product(ks, alphas):
    results.append(
        compute_electron_bands(
            params={**default_params, "k_x": k, "alpha_y": alpha},
            wrapped_syst=wrapped_syst,
            charge_op=Q,
            spin_op=Sy,
        )
    )
results = np.array(results).reshape(len(ks), len(alphas), 3, -1)

# %%
import xarray as xr

ds_bands = xr.Dataset(
    {
        "bandstructure": (["k", "alpha", "band"], results[:, :, 0, :]),
        "spin": (["k", "alpha", "band"], results[:, :, 1, :]),
        "charge": (["k", "alpha", "band"], results[:, :, 2, :]),
    },
    coords={
        "k": ks,
        "band": np.arange(results.shape[-1]),
        "alpha": alphas,

    },
)

# %%
# Filter the dataset where charge > 0
filtered_ds = ds_bands.where(ds_bands.charge > 0, drop=True)

# Plot k vs energy for all bands (filtered), grouped by band, without legends
plot = filtered_ds.hvplot.scatter(
    x="k",
    y="bandstructure",
    c="spin",  # Color by spin
    by="band",  # Separate bands
    title="",
    colorbar=True,
    legend=False,  # Remove legends
    ylim=(-1, 1),
    aspect=1,
)

plot

# %%
from tqdm import tqdm

num_states = 20

eig = []
W_Ns = [1, 10, 20]  # Normal region widths
phis = np.linspace(0, 2 * np.pi, 51)
W_SC = 20  # Width of the superconducting region
for phi, alpha, W in tqdm(product(phis, alphas, W_Ns)):
    syst = abs_syst(W_SC, W).finalized()
    eig.append(
        compute_andreev_spectrum(
            params={**default_params, "alpha_y": alpha, "phi": phi, "W_N": W},
            syst=syst,
            num_states=num_states,
        )
    )

# %%
eig = np.array(eig).reshape(len(phis), len(alphas), len(W_Ns), num_states)
ds_andreev = xr.Dataset(
    {
        "energy": (["phi", "alpha", "W", "level"], eig),
    },
    coords={
        "phi": phis,
        "level": np.arange(num_states),
        "alpha": alphas,
        "W": W_Ns,
    },
)

# %%
# Plot k vs energy for all bands (filtered), grouped by band, without legends
plot = ds_andreev.hvplot(
    x="phi",
    y="energy",
    c="k",  # Color by spin
    by="level",  # Separate bands
    colorbar=True,
    legend=False,  # Remove legends
    aspect=1,
    dynamic=False
)

plot


# %%
ds_bands.to_netcdf("./data/soc_bands.nc")
ds_andreev.to_netcdf("./data/andreev_levels.nc")
