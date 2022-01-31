# Minimal models
We begin our discussion by analyzing three simple limiting models that illustrate interesting properties of ABS.

## Weakly couple quantum dot
We consider a pair of single-mode, spinless superconducting leads weakly coupled by a normal region.
The Hamiltonian reads

$$
H = H_\mathrm{dot} + \sum_{\alpha \in \{L, R\}} H_{\alpha} + H_\mathrm{tunnel}^\alpha
$$
where

$$
H_{\alpha} = \sum_k (\varepsilon_k - \mu) c_{\alpha, k}^\dagger c_{\alpha, k} - \mu + \sum_k\Delta e^{\pm i\varphi/2}  c_{\alpha, k}^\dagger c_{\alpha, -k}^\dagger + \mathrm{h.c.}
$$
is the Hamiltonian of the left and right superconducting leads, $\Delta$ is the superconducting order parameter, $\mu$ the chemical potential, and $\varphi$ is the phase difference between the leads.
The dot hosts a single energy level

$$
H_\mathrm{dot} = \varepsilon_d d^\dagger d.
$$

Finally, the coupling to the leads is parameterized by

$$
H^{L/R}_\mathrm{tunnel} = t_{L/R} \sum_k d^\dagger c_{L/R, k} + \mathrm{h.c.}
$$

Using the Bogoliubov De Gennes formalism, the Hamiltonian of the superconducting leads can be brought to a quadratic form

$$
H_{\alpha}(k) = \begin{pmatrix}c_{\alpha, k}^\dagger && c_{\alpha, -k} \end{pmatrix}  \begin{pmatrix} \varepsilon_k - \mu  & \Delta e^{i\varphi/2} \\ \Delta e^{-i\varphi/2} & -\varepsilon_k + \mu \end{pmatrix} \begin{pmatrix}c_{\alpha, k} \\ c_{\alpha, -k}^\dagger \end{pmatrix} = C^\dagger H_{\alpha}^\mathrm{BdG}(k) C
$$

The scattering states of each lead are then readily obtained by diagonalizing $H_{\alpha}^\mathrm{BdG}(k)$:

$$
E(k) = \pm \sqrt{(\varepsilon_k - \mu)^2 + \Delta^2} \\
\langle r | \Psi(k) \rangle = \begin{pmatrix} \sqrt{E + \varepsilon_k - \mu} \\ \sqrt{E - \varepsilon_k + \mu} \end{pmatrix} e^{ikx}
$$

We are now ready to look for ABS.
Because the superconductors have a bulk gap of $\Delta$, the ABS will decay exponentially into the superconductors with a length scale set by the coherence length $\xi = $.
Furthermore, since scattering is elastic, a bound state at energy $E$ is a superposition


# Sub-fields of Andreev states

## Superconductor-semiconductor structures

## Andreev bound states as qubits

## Metallic weak links

## Multiterminal devices

## Majorana zero modes
