# Minimal models
<!-- Andreev states have rich physics that can be understood from different perspectives -->
Andreev states are coherent superpositions of electrons and holes that exist in a non-superconducting region or a weak link between two superconductors, and are coupled by reflecting from a nearby superconductor.
If the same normal region is coupled to more than one superconductor, the energies of the Andreev states start depending on the superconducting phase difference through the *energy-phase relation*, and therefore they carry supercurrent.
The interplay between the physics of the normal region and the superconductor makes Andreev states manifest in very different regimes and alters their properties.
Depending on the situation one considers, a different perspective on the Andreev states captures the essential physics most naturally.
To illustrate this variation, we begin with three toy models of Andreev states, each capturing a different way of viewing them.

## Tunneling perspective
<!-- When the normal region has few levels and weak tunneling, a Hamiltonian description is natural. -->
The go-to approach to combining different ingredients in quantum mechanics is perturbation theory.
The simplest normal region is a quantum dot containing a single electron level.
Weakly coupling the quantum dot to the superconductors imbues a part of the superconducting properties on the dot level, introducing a *proximity-induced superconducting pairing*.

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

## Point scatterer perspective
<!-- When most of the wave function is in the superconductor, the scattering state basis is the most appropriate. -->
The weak link between two superconductors can be arbitrarily small.
In the extreme limit of the *Dayem bridge* there is no normal region at all, only a constriction between two superconductors.
The natural starting point for describing this *short junction* regime is the scattering approach, which analyzes how electron waves entering a superconductor reflect from it, and from the junction.
We consider two superconducting contacts with phase difference $\varphi$ connected by a normal region with a point scatterer.
Scattering states at energy $\varepsilon$ in the left and normal regions are superpositions of incoming and outgoing states:

$$
\Psi_L = \sum_{c=e, h} a_{c, L} |c_{L, \mathrm{in}}\rangle + b_{c, L} |c_{L, \mathrm{out}}\rangle \\
\Psi_R = \sum_{c=e, h} a_{c, R} |c_{L, \mathrm{in}}\rangle + b_{c, R} |c_{R, \mathrm{out}}\rangle
$$

Incoming waves that interact with the point scatterer are normal-reflected according to the scattering matrix $S_N$:

$$
\begin{pmatrix} b_{e, R} \\ b_{e, L} \\ b_{h, R} \\ b_{h, L} \end{pmatrix} = S_N \begin{pmatrix} a_{e, R} \\ a_{e, L} \\ a_{h, R} \\ a_{h, L} \end{pmatrix}
$$(normal_reflection)

Because the normal region does not mix electrons and holes, $S_N$ is block-diagonal in electron-hole space:

$$
S_N = \begin{pmatrix}s_N & 0 \\ 0 & s_N\end{pmatrix}, \\\\
s_N = \begin{pmatrix} r & t \\ t & r \end{pmatrix}.
$$

Here we have used the short-junction approximation to neglect the energy dependence of $s_N$.
At energies below the bulk superconducting gap ($\varepsilon < \Delta$), there are no propagating states in the superconductors.
Therefore, outgoing particles that come into contact with a superconducting terminal will be Andreev reflected:

$$
\begin{pmatrix} a_{e, R} \\ a_{e, L} \\ a_{h, R} \\ a_{h, L} \end{pmatrix} = S_A(\varepsilon) \begin{pmatrix} b_{e, R} \\ b_{e, L} \\ b_{h, R} \\ b_{h, L} \end{pmatrix}
$$(andreev_reflection)

where

$$
S_A = \begin{pmatrix}0 & s_A(\varepsilon) \\ s_A(\varepsilon)^* & 0 \end{pmatrix}, \\\\
s_A = e^{-i \arccos \varepsilon / \Delta} \begin{pmatrix} e^{i\varphi/2} & 0 \\ 0 & e^{-i\varphi/2} \end{pmatrix}
$$

has a block off-diagonal structure because the superconductors mix electron and hole degrees of freedom.

Plugging {eq}`normal_reflection` into {eq}`andreev_reflection` we obtain

$$
(\mathbb{I} - S_A(\varepsilon) S_N) \begin{pmatrix} a_{e, R} \\ a_{e, L} \\ a_{h, R} \\ a_{h, L} \end{pmatrix} = 0
$$(andreev_system)

Equation {eq}`andreev_system` implies that $\det(\mathbb{I} - s_A(\varepsilon) s_N(\varepsilon)) = 0$.
Solving this equation yields the short junction spectrum:

$$
E = \Delta \sqrt{1 - t \sin^2 \frac{\varphi}{2}}
$$(short_junction)

## Large normal region perspective
<!-- When quasiparticles spend most of the time in the normal region, the superconductors become hard wall boundaries. -->
In the opposite limit, the normal region is sufficiently large for the quasiparticles to spend most of the time outside of the superconductor.
In other words, in the *long junction* limit, the quasiparticle dwell time $\tau_\text{dw} = v_F / L $ (with $v_F$ the Fermi velocity, $L$ the size of the normal region, and $\hbar$ the reduced Plank constant) becomes much larger than the Andreev reflection time $\hbar/\Delta$, as follows from the uncertainty relation.
The quasiparticle wave function then are linear superpositions of travelling waves, matched at the interfaces with the superconductor by the effective boundary conditions.
To derive the spectrum of a long junction, we consider the phase acquired by an electron propagating in the weak link.

```{note}
:class: dropdown
By neglecting the dynamical phase $2kL$ we recover the short-junction spectrum {eq}`short_junction`.
```


## Comparison of models


# Sub-fields of Andreev states

## Superconductor-semiconductor structures

## Andreev bound states as qubits

## Metallic weak links

## Multiterminal devices

## Majorana zero modes

## Andreev bound states as topological matter
