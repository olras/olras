# Minimal models
We begin our discussion by analyzing three simple limiting models that illustrate interesting properties of ABS.

## Weakly coupled quantum dot
We consider a small metallic region with a single fermionic level with a hamiltonian coupled to two superconducting reservoirs with complex order paramters $\Delta_{1,2}$.
The bare hamiltonian of the dot reads

$$
H_\mathrm{dot} = -\mu (c_\downarrow^\dagger c_\downarrow + c_\uparrow^\dagger c_\uparrow)
$$

where $\mu$ is the chemical potential of the dot.
The proximity with the superconducting reservoirs induces superconducting correlations in dot.
Within the mean-field approximation, we can model this effect with the term

$$
H_\mathrm{SC} = (\Delta_1^* + \Delta_2^*) c_\uparrow c_\downarrow  + (\Delta_1 + \Delta_2)  c_\downarrow^\dagger c_\uparrow^\dagger
$$

with $\Delta_{1, 2}$ the superconducting pairing of the two superconductors.
Using the Bogoliubov De Gennes formalism, we can bring the Hamiltonian to a quadratic form

$$
\begin{aligned}
\mathcal{H} &= \frac{1}{2} \mathbf{\mathcal{C}}^\dagger
\begin{pmatrix}
-\mu & 0 & 0 & -\Delta_1 - \Delta_2\\
0 & -\mu & \Delta_1 + \Delta_2 & 0\\
0 & \Delta_1^* + \Delta_2^* & \mu & 0\\
-\Delta_1^* - \Delta_2^*  & 0 & 0 & \mu \end{pmatrix}\mathbf{\mathcal{C}} \\
&= \frac{1}{2} \mathbf{\mathcal{C}}^\dagger H_\mathrm{BdG} \mathbf{\mathcal{C}}^\dagger
\end{aligned}
$$

where $\mathbf{\mathcal{C}} = \begin{pmatrix} c_{\uparrow} & c_{\downarrow} & c_{\uparrow}^\dagger & c_{\downarrow}^\dagger \end{pmatrix}^T$.
By diagonalizing $H_\mathrm{BdG}$ we find quasiparticle operators $d_i$ that bring $\mathcal{H} = \sum_{i} \varepsilon_i d_i^\dagger d_i$, with $\varepsilon_i \ge 0$.
Assuming the Fermi energy is much larger than the superconducting pairing ($|\mu| \gg |\Delta_{i}|$), we find

$$
\begin{aligned}
\varepsilon_{_i} &\approx \mu + \frac{|\Delta_1 + \Delta_2 |^2}{2\mu} \\
d_1 &\approx \left(\frac{|\Delta_1 + \Delta_2 |^2}{2\mu}\right) c_\downarrow +  c_\uparrow^\dagger \\
d_2 &\approx  c_\downarrow^\dagger - \left(\frac{|\Delta_1 + \Delta_2 |^2}{2\mu}\right) c_\uparrow \\
\end{aligned}
$$

We can construct the ground state wavefunction $|\Psi\rangle$ by taking the vacuum state $|0\rangle$ and removing all quasiparticles:

$$
|\Psi \rangle \propto d_1 d_2 |0\rangle \propto -\left(\frac{|\Delta_1 + \Delta_2 |^2}{2\mu}\right)|0\rangle + |\uparrow \downarrow \rangle
$$

The wavefunction shows [one](one) of the most striking properties of ABS: **they are localized states in metallic regions *without* charge quantization.**

We now study what happens when there is a finite phase difference $\varphi$ between the superconductors.
For simplicity we consider $|\Delta_1| = |\Delta_2| = |\Delta|$.
The ground state energy becomes

$$
E = -2 \mu - \frac{2|\Delta|^2}{\mu}(1 + \cos(\varphi)).
$$

Here we observe another striking property of ABS.
**Because the ground state energy disperses with $\varphi$, the ABS mediate supercurrent between the superconductors** with magnitude

$$
\frac{dE}{d\varphi} = \frac{2|\Delta|^2}{\mu}\sin(\varphi).
$$


# Sub-fields of Andreev states

## Superconductor-semiconductor structures

## Andreev bound states as qubits

## Metallic weak links

## Multiterminal devices

## Majorana zero modes
