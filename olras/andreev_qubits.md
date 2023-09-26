---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Andreev qubits

+++

- Superconducting qubits in cQED such as the transmon, fluxonium and the $0 - \pi$ qubit rely on electrodynamic excitations of the superconducting condensate. They exploit emergent excitations in which millions of Andreev levels participate.
- In contrast, Andreev qubits store information in the fermionic degrees of freedom of individual Andreev bound states.
- In conventional tunnel junctions, used widely in cQED, there are millions of Andreev levels. Controlling single levels in such a setup is hopeless.
- Therefore, we must engineer a weak link that host only a handful of Andreev levels. This is possible by using low-density semiconducting or quantum dot junctions.
- Andreev qubits come in two main flavors: charge and spin.

+++

## Andreev spin qubits

+++

- Andreev spin qubits encode information in the spin of a trapped quasiparticle in the weak link. They were first proposed in 2003 by Chtchelkatchev and Nazarov {cite}`PhysRevLett.90.226806`.
- In the setups we studied in minimal models sections, Andreev bound states were spin-degenerate.
- There are two approaches to breaking this degeneracy.

+++

### Splitting Andreev levels with spin-orbit coupling

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-input]
---
import xarray as xr
import hvplot.xarray
import warnings
warnings.filterwarnings("ignore")

andreev_data = xr.load_dataset("andreev_qubits.nc")

bstruct_plot = andreev_data.sel(phase=0).hvplot.scatter(width=300,
                                                        y="band_structure",
                                                        x="k",
                                                        by="level",
                                                        legend=False,
                                                        size=1,
                                                        c="spin",
                                                        ylim=(-80, 50),
                                                       )
andreev_plot = andreev_data.sel(k=0).hvplot.line(width=300,
                                                 y="andreev_energies",
                                                 x="phase",
                                                 by="level",
                                                 legend=False,
                                                 c="black",
                                                 title="",
                                                )

bstruct_plot + andreev_plot
```

To see how we can introduce a splitting of ABS, we begin from the short-junction limit where $E_T = \hbar v_F / L \gg \Delta$. The lowest-order correction to the ABS hamiltonian in $1/E_T$ is

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

This is a transcendental equation, but we can get an approximate solution by letting E = $\Delta \cos \varphi/2 + \epsilon = E_0 + \epsilon$ and searching for solutions with small $\epsilon$. Plugging this in we obtain

$$
\frac{\varepsilon}{\Delta} - \frac{E_0 + \varepsilon}{E_T} |\sin(\varphi/2)| \sqrt{1 + \frac{2E_0\varepsilon}{\Delta^2 \sin^2(\varphi/2)}} = 0
$$

expanding the square root, and collecting terms only first order contributions in $\varepsilon$ we obtain

$$
\varepsilon \left[ \frac{1}{\Delta} - \frac{|\sin(\varphi/2)|}{E_T } + \frac{\cos(\varphi/2)^2}{E_T |\sin(\varphi/2)|} \right] = \frac{E_0 |\sin(\varphi/2)|}{E_T}
$$

By neglecting terms of order $1/E_T$ on the LHS and end up with the equation above.
:::

- From this expression we see that in order to introduce a splitting, the channels at the Fermi level must have different Fermi velocities. One way to achieve this is to add spin-orbit coupling.
- If the spin-orbit is linear, we need higher bands. The relevant expression was derived by Tosi et al.

+++

### Phase-induced splitting in multiterminal junctions
- The spin-orbit approach has the limitation that the splitting is of order $\Delta^2/E_T$, which is very small in short-junctions.
- One can increase the splitting by increasing the length of the weak link. However, this also decreases the level spacing and makes it harder to address individual states.
- An alternative approach that allows us to stay in the short-junction limit is extend out setup with an additional superconducting lead.

+++

## Experimental results

```{code-cell} ipython3

```
