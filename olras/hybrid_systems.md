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

# Hybrid systems

- Semiconductors are often use in nanoelectronics because their low density of states allows electrostatic control of devices.
- It is possible to induce superconducting correlations in these materials via proximity effect.
- The electric control in hybrid systems allows accessing phenomena that is hard or impossible to access in superconductor-only devices.

## Proximity effect

Andreev reflection converts electron-like into hole-like quasiparticles.
Thus, the interface with a superconductor induces superconducing correlations in a normal material.

We demonstrate this proximity effect by considering a one-dimensional electron gas coupled to a superconductor, depicted in the figure.
The normal region has a Hamiltonian $H_N$, the superconducting region $H_{SC}$, and the hopping between the two regions is $T$.
Thus, choosing a basis $\Psi = (\mathcal{D}(k), \mathcal{C}(k))^T$ where $\mathcal{D}(k)$ annihilates a quasiparticle with momentum $k$ in the normal region and $\mathcal{C}(k)$ in ths superconducting region, we arrive to the Hamiltonian
$$
H = \sum_k \Psi^{\dagger}(k)\left(
\begin{array}{cc}
  H_N & T\\
  T^{\dagger} & H_{SC}
\end{array}
\right)\Psi(k)~.
$$

We then calculate the Green's function in the normal region with the Schur's complement of $H$:
$$
G_N(\omega) = (H_N + \Sigma(\omega))^{-1}~,\quad \Sigma(\omega) = T (\omega - H_{SC})^{-1}T^{\dagger}~.
$$
Meaning that the renormalized Hamiltonian in the normal region is
$$
\tilde{H}_N = H_N + \Sigma(\omega)~.
$$

Assuming that the superconductor has a time-reversal symmetric Hamiltonian, we can write it with the Bogoliubov-de Gennes formalism as
$$
H_{SC}=\sum_k \mathcal{C}_k^{\dagger}[(\epsilon_{k}\tau_z + \Delta \tau_x)\otimes\sigma_0] \mathcal{C}_k
$$
where $\mathcal{C} = (c_{\uparrow}, c_{\downarrow}, -c_{\downarrow}^{\dagger}, c_{\uparrow}^{\dagger})^T$, $\tau_i$ and $\sigma_i$ are Pauli matrices acting in the particle-hole and spin degrees of freedom, $\epsilon_k$ is the normal state dispersion of the superconducting material, and $\Delta$ is the superconducting order parameter.
With this Hamiltonian, we conclude that
$$
\Sigma(\omega) = \frac{1}{\omega^2 - \epsilon_k^2 - \Delta^2}T (\omega\tau_0\otimes\sigma_0 + H_{SC}) T^{\dagger}~.
$$
Since the self-energy $\Sigma(\omega)$ is proportional to $H_{SC}$, the normal region acquires an induced superconducting pairing
$$
\Delta_{ind} = \frac{1}{\omega^2 - \epsilon_k^2 - \Delta^2}T (\Delta\tau_x\otimes\sigma_0) T^{\dagger}~.
$$

## Quantum dots

### Proximity effect in quantum dots

If we now consider a single-level spin-degenerate quantum dot with a Hamiltonian
$$
H_N = -\mu \sum_{\sigma} d_{\sigma}^{\dagger}d_{\sigma} = \mathcal{D}^{\dagger}(-\mu \tau_0\otimes \sigma_0)\mathcal{D}
$$
coupled to two superconducing reservoirs with phases $\pm \varphi / 2$ by
$$
T = \sum_{\sigma} \sum_{k,\sigma'} \left(t_1 c_{1,k\sigma'}^{\dagger}d_{\sigma} + t_2 c_{2,k\sigma'}^{\dagger}d_{\sigma}\right) = \sum_k \left[\mathcal{C}_{1,k}^{\dagger}(t_1 \tau_z \otimes \sigma_0)\mathcal{D} + \mathcal{C}_{2,k}^{\dagger}(t_2 \tau_z \otimes \sigma_0)\mathcal{D} \right]
$$
we [recover the Hamiltonian from the introduction](./topic_map.md) in the limit where $\omega \to 0$:
$$
\tilde{H}_N = \epsilon\sum_{\sigma} d_{\sigma}^{\dagger}d_{\sigma} + (\Gamma_1 e^{-i\frac{\varphi}{2}} + \Gamma_2 e^{i\frac{\varphi}{2}}) d_\uparrow d_\downarrow  + (\Gamma_1e^{i\frac{\varphi}{2}} + \Gamma_2e^{-i\frac{\varphi}{2}}) d_\downarrow^\dagger d_\uparrow^\dagger
$$
where
$$
\epsilon = -\mu - \sum_k \left(\frac{t_1^2 + t_2^2}{\epsilon_k^2 + \Delta^2}\right) \epsilon_k~,\\
\Gamma_{i} = \sum_k \left(\frac{t_1^2 + t_2^2}{\epsilon_k^2 + \Delta^2}\right) \Delta~.
$$

### Local and non-local transport

### Josephson effect

### Interacting Andreev levels

## Carbon nanotubes

## Nanowires

### Electrostatics

### Full-shell nanowires

### Superconductivity and magnetism

## 2DEGs

### Electrostatically-defined devices

### Planar Josephson junctions

## Graphene

### Andreev reflection and valleys

### Quantum Hall edge states

### van der Waals proximity

### Intrinsic superconductivity in multilayers

## Other two-dimensional materials

## Chern insulators

## Quantum spin Hall and three-dimensional topological insulators