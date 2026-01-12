---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.13'
    jupytext_version: '1.15.0'
kernelspec:
  display_name: "Python 3 (ipykernel)"
  language: "python"
  name: "python3"
---

# Andreev spin qubits

+++

## Conceptual idea

### Why should we encode spins in Andreev devices?

- Spin qubits are well-established, but readout is slow and long-range qubit-qubit interactions is difficult.
- It is challenging to strongly couple spin qubits to superconducting elements.
- Andreev spins carry supercurrent, and therefore are easy to couple with superconducting elements.

### Splitting spins without a Zeeman field

- Andreev spins split in energy with phase bias under the presence of spin-orbit coupling.
- The basic ingredients are: (i) modes with different spins moving with different velocitites; (ii) a junction much longer than the spin-orbit length.
- The difference between the spin-dependent dynamical phases of the two modes split spins.
- Typically, a Josephson junction with multiple Andreev doublets is desired for spin manipulation: the ideal situation is a long(ish) junction ($\xi \lesssim L$).

### Coupling Andreev spins

- Because Andreev spins carry supercurrent, it is possible to couple Andreev spins inductively.
- Variable inductors therefore allow manipulation of qubit-qubit interactions for two-qubit gates.

+++

## Current status

### Spin splitting in Rashba nanowires

- We can achieve the necessary ingredients for spin splitting in a Rashba nanowire.
- The subband coupling results in spin-dependent propagating modes with different velocities.
- In a sufficiently long wire, we observe spin splittings are a sizeable fraction of the superconducting gap.
- This splitting has been observed in Rashba nanowires via dispersive readout.
- A quasiparticle remains trapped in a superconducting weak link if there is no quasiparticle poisoning.
- Due to spin conservation, transitions to states with opposite spins are suppressed, resulting in lifetimes on the order of microseconds.

### Coherent manipulation of Andreev spins

- Two-tone spectroscopy allows to identify possible transitions.
- Direct spin-flip transitions are suppressed since $\langle \uparrow | J_A | \downarrow\rangle = 0$.
- However, spin-flip transitions to higher doublets and allow Raman transitions via a $\Lambda$ system.
- It is therefore possible to drive $\Lambda$-Rabi oscillations via this Raman process.

### Coupling Andreev spins

- It is possible to couple Andreev states by simply connecting them in series as an Andreev molecule.
- This process however requires tuning in a nanoscale, which may be challenging due to cross talk and charge noise.
- Long-range coupling solves these issues and can be done with tunable inductors.
- Such long-range coupling has been achieved using gate-tunable transmons.

+++

## Future directions

### Mitigating effects of nuclear spins

- There are indications that the lifetime of Andreev spins is limited by the presence of nuclear spins.
- To solve this issue, a next generation of devices is exploring materials that allow isotopic purification, such as germanium.
- Superconducting proximity in germanium has been achieved with both top and side contacts, but no spin splitting has been observed.

## Increasing spin splitting with multiterminal setups

- The spin splittings observed in experiments are still small.
- Increasing the lenght of the devices increases the splitting, but also increases the number of the level doublets within the gap.
- An alternative to increase the spin splitting is via multiterminal devices.
- Recent works performed tunnel spectroscopy of multiterminal junctions, but they still lack spin resolution.

### Qubit protection and error correction

- Since, differently from topological qubits, ASQs are not fault-tolerant, schemes for QEC are necessary.
- There are recent proposals for ASQ protection using Kramers degeneracy and Franck-Condon blockade.

### Scaling

- The long-range coupling of ASQs allows architectures with all-to-all connections.

+++

### Splitting Andreev levels with spin-orbit coupling

```{code-cell} ipython3
import xarray as xr
import hvplot.xarray
import warnings
warnings.filterwarnings("ignore")

ds_andreev = xr.load_dataset("./simulations/asq/data/andreev_levels.nc")
ds_bands = xr.load_dataset("./simulations/asq/data/soc_bands.nc")

# Filter the dataset where charge > 0
filtered_ds = ds_bands.where(ds_bands.charge > 0, drop=True)

# Plot k vs energy for all bands (filtered), grouped by band, without legends
plot1 = filtered_ds.hvplot.scatter(
    x="k",
    y="bandstructure",
    c="spin",  # Color by spin
    by="band",  # Separate bands
    title="",
    colorbar=True,
    legend=False,  # Remove legends
    ylim=(-1, 1),
    aspect=1,
    dynamic=False
)

# Plot k vs energy for all bands (filtered), grouped by band, without legends
plot2 = ds_andreev.hvplot(
    x="phi",
    y="energy",
    c="k",  # Color by spin
    by="level",  # Separate bands
    title="",
    colorbar=True,
    legend=False,  # Remove legends
    aspect=1,
    dynamic=False
)

plot1 + plot2
```

To see how we can introduce a splitting of ABS, we begin from the short-junction limit where $E_T = \hbar v_F / L \gg \Delta$. The lowest-order correction to the ABS Hamiltonian in $1/E_T$ is

$$
\varepsilon = \frac{\Delta^2 \sin(\varphi)}{2E_T}
$$

:::{admonition} Derivation
:class: note, dropdown

_(warning: derivation is still sloppy)_

Recall that in the Andreev limit $\mu \gg E$ the bound state equation reads

$$
\pm \varphi + 2\pi n  = 2E/E_T + 2\arccos(E/\Delta)
$$

$$
\cos(\varphi/2) = \cos\left(E/E_T + \arccos(E/\Delta) \right) 
$$

We expand the cosine term to first order in $1/E_T$ and the RHS becomes

$$
\cos(\arccos(E/\Delta) + E/E_T)) \approx E/\Delta - \frac{E}{E_T} \sin{\arccos(E/\Delta)} 
$$

Using $\sin(\arccos(x)) = \sqrt{1 - x^2}$ we obtain 

$$
E/\Delta - \frac{E}{E_T} \sqrt{1 - (E/\Delta)^2} - \cos(\varphi/2) = 0
$$

This is a transcendental equation, but we can get an approximate solution by letting $E = \Delta \cos(\varphi/2) + \epsilon = E_0 + \epsilon$ and searching for solutions with small $\epsilon$. Plugging this in we obtain

$$
\frac{\varepsilon}{\Delta} - \frac{E_0 + \varepsilon}{E_T} |\sin(\varphi/2)| \sqrt{1 + \frac{2E_0\varepsilon}{\Delta^2 \sin^2(\varphi/2)}} = 0
$$

Expanding the square root, and collecting terms only first-order contributions in $\varepsilon$, we obtain

$$
\varepsilon \left[ \frac{1}{\Delta} - \frac{|\sin(\varphi/2)|}{E_T } + \frac{\cos(\varphi/2)^2}{E_T |\sin(\varphi/2)|} \right] = \frac{E_0 |\sin(\varphi/2)|}{E_T}
$$

By neglecting terms of order $1/E_T$ on the LHS, we end up with the equation above.
:::

- From this expression, we see that in order to introduce a splitting, the channels at the Fermi level must have different Fermi velocities. One way to achieve this is to add spin-orbit coupling.
- If the spin-orbit is linear, we need higher bands. The relevant expression was derived by Tosi et al.