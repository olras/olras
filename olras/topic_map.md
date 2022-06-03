# Minimal models
<!-- Andreev states have rich physics that can be understood from different perspectives -->
A superconductor in proximity with a non-superconducting region introduces coherent coupling between electrons and holes through *Andreev reflection*.
Under certain conditions this process becomes resonant and forms stable superpositions of electrons and holes known as *Andreev bound states* (ABS).
If the same normal region is coupled to more than one superconductor, the bound state energies become dependent on the superconducting phase differences between terminals, which implies the ABS carry supercurrent across superconductors.
The interplay between the physics of the normal region and the superconductors makes ABS manifest in very different regimes and alters their properties.
Depending on the situation one considers, a different perspective on the ABS captures the essential physics most naturally.
To illustrate this variation, we begin with three toy models, each corresponding to a different physical limit.

## Weak coupling - tunneling perspective
<!-- When the normal region has few levels and weak tunneling, a Hamiltonian description is natural. -->
The simplest normal region is a quantum dot containing a single electron level with a bare hamiltonian

$$
H_\mathrm{dot} = -\mu (c_\downarrow^\dagger c_\downarrow + c_\uparrow^\dagger c_\uparrow)
$$

where $\mu$ is the chemical potential of the dot.
Weakly coupling the quantum dot to the superconductors imbues a part of the superconducting properties on the dot level, introducing a *proximity-induced superconducting pairing*.
Within the mean-field approximation, we can model this effect with the term

$$
H_\mathrm{SC} = (\Delta_1^* + \Delta_2^*) c_\uparrow c_\downarrow  + (\Delta_1 + \Delta_2)  c_\downarrow^\dagger c_\uparrow^\dagger
$$

with $\Delta_{1, 2}$ the induced superconducting pairing of each superconductor.
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
By diagonalizing $H_\mathrm{BdG}$ we find quasiparticle operators $d_i$ that allows to write the hamiltonian as $\mathcal{H} = \sum_{i} \varepsilon_i d_i^\dagger d_i$, with $\varepsilon_i \ge 0$.
Assuming the Fermi energy is much larger than the superconducting pairing ($|\mu| \gg |\Delta_{i}|$), we obtain

$$
\begin{aligned}
\varepsilon_{_i} &\approx \mu + \frac{|\Delta_1 + \Delta_2 |^2}{2\mu} \\
d_\downarrow &\approx \left(\frac{|\Delta_1 + \Delta_2 |^2}{2\mu}\right) c_\downarrow +  c_\uparrow^\dagger \\
d_\uparrow &\approx  c_\downarrow^\dagger - \left(\frac{|\Delta_1 + \Delta_2 |^2}{2\mu}\right) c_\uparrow \\
\end{aligned}
$$

The manifold of many-body states spanned by $d_i$ is frequently dubbed the *Andreev doublet*.
To explore interesting properties of ABS, we compute the wavefunctions of these states explicitly.
The ground state does not contain any quasiparticles.
Therefore, we can construct it by taking the vacuum state $|0\rangle$ and projecting out all components with quasiparticles:

$$
|g \rangle \propto d_\downarrow d_\uparrow |0\rangle \propto -\left(\frac{|\Delta_1 + \Delta_2 |^2}{2\mu}\right)|0\rangle + |\uparrow \downarrow \rangle
$$

The wavefunction shows one of the most striking properties of ABS: *they are localized states in weak links *without* charge quantization.*
The ground state energy reads

$$
E = -\mu - \frac{|\Delta|^2}{\mu}(1 + \cos(\varphi)).
$$

Where for simplicity we assumed $|\Delta_1| = |\Delta_2| = |\Delta|$.
This reveals yet another important property of ABS.
*Because the ground state energy disperses with $\varphi$, ABS mediate supercurrent between the superconductors* with magnitude

$$
I = \frac{2e}{\hbar} \frac{dE}{d\varphi} = \frac{2e |\Delta|^2}{\hbar\mu}\sin(\varphi).
$$

A similar calculation shows that the doubly-excited state $|e \rangle = d_{\downarrow}^\dagger d_{\uparrow}^\dagger |g\rangle = |\uparrow \downarrow\rangle$ carries an opposite supercurrent of equal magnitude.
The states $| g \rangle$ and $| e \rangle$ contain even numbers of quasiparticles, and thus span the *even* manifold.
The *odd* manifold is spanned by a pair of zero-energy, degenerate states with single quasiparticles

$$
d_\downarrow^\dagger |g\rangle \propto |\downarrow \rangle \\
d_\uparrow^\dagger |g\rangle \propto |\uparrow \rangle
$$

In contrast with the even manifold, their energy does not disperse with $\varphi$ and hence they do not carry a supercurrent.

## Strong coupling
In the previous subsection we considered a normal dot that is only weakly coupled to the two superconductors.
This allowed us to avoid explicitly modelling the superconducting regions and to capture their effects on the dot through an effective perturbative term.
In this subsection we go beyond this limit and allow the superconductors to be strongly coupled to the normal region.
To do so, it is useful to adopt a different perspective that focuses on how electrons and hole waves propagate in the normal and superconducting regions.
We consider an electron with energy $E < \Delta$ travelling in a one-dimensional normal region sandwiched between two superconductors.
Once it reaches an interface with a superconductor it must be reflected back to the normal region because there are no available single-particle states below the gap.
While this can happen through simple normal reflection, sufficiently transparent interfaces support another energy-conserving process: Andreev reflection to hole.

:::{admonition} A primer on Andreev reflection
:class: note, dropdown
placeholder
:::

The resulting hole will then travel towards the other normal-superconductor interface, where it also undergoes Andreev reflection to an electron, restarting the cycle.
If these processes interfere constructively, they give rise to an ABS.
This gives us another perspective of how ABS are formed, namely through sucessive Andreev reflections.
Because each Andreev reflection results in charge transfer of $2e$, it also provides a microscopic explanation of how an ABS mediates supercurrent.
Below we formalize this treatment of the problem through the scattering formalism, which analyzes how electron waves entering a superconductor reflect from it, and from the junction.

### Point scatterer perspective
<!-- When most of the wave function is in the superconductor, the scattering state basis is the most appropriate. -->
The weak link between two superconductors can be arbitrarily small.
In the extreme limit of the *Dayem bridge* there is no normal region at all, only a constriction between two superconductors.
We consider two superconducting contacts with phase difference $\varphi$ connected by a normal region with a point scatterer, also known as the *short junction* regime.
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
$$(sc_scattering_mat)

has a block off-diagonal structure because the superconductors mix electron and hole degrees of freedom.

Plugging {eq}`normal_reflection` into {eq}`andreev_reflection` we obtain

$$
(\mathbb{I} - S_A(\varepsilon) S_N) \begin{pmatrix} a_{e, R} \\ a_{e, L} \\ a_{h, R} \\ a_{h, L} \end{pmatrix} = 0
$$(andreev_system)

Equation {eq}`andreev_system` implies that $\det(\mathbb{I} - s_A(\varepsilon) s_N(\varepsilon)) = 0$.
Solving this equation yields the short junction spectrum {cite}`beenakker1991universal`:

$$
E = \Delta \sqrt{1 - t \sin^2 \frac{\varphi}{2}}
$$(short_junction)


## Large normal region perspective
<!-- When quasiparticles spend most of the time in the normal region, the superconductors become hard wall boundaries. -->
In the opposite limit, the normal region is sufficiently large for the quasiparticles to spend most of the time outside of the superconductor.
In other words, in the *long junction* limit, the quasiparticle dwell time $\tau_\text{dw} = v_F / L $ (with $v_F$ the Fermi velocity, $L$ the size of the normal region, and $\hbar$ the reduced Plank constant) becomes much larger than the Andreev reflection time $\hbar/\Delta$, as follows from the uncertainty relation.
The quasiparticle wave functions then are linear superpositions of travelling waves, matched at the interfaces with the superconductor by the effective boundary conditions.

While it is possible to use the scattering formalism to derive the spectrum of a long junction, we resort to a simpler semiclassical approach.
In particular, we apply the [Bohr-Sommerfeld](https://en.wikipedia.org/wiki/Old_quantum_theory#Basic_principles) condition, which states that bound states arise when there are closed trajectories in which quasiparticles acquire a total phase of $2 \pi n$, with $n$ integer.
We consider right-moving electron in the weak link.
As it moves through the weak link, it acquires a dynamical phase $kL$.
When it reaches the right superconductor, it Andreev reflects as a hole and acquires a phase $-\frac{\varphi}{2} - \arccos(E/\Delta)$ (see equation {eq}`sc_scattering_mat`).
The hole then travels to the left terminal, acquiring a dynamical phase of $-k_h L$ and Andreev reflects with the same phase as the right-moving electron.
Collecting these terms, the quantization condition becomes

$$
2\pi n = -\varphi - 2\arccos(E/\Delta) + (k_e - k_h) L
$$(quantization_condition)

```{note}
:class: dropdown
By neglecting the dynamical phase $(k_e - k_h) L$ we recover the short-junction spectrum {eq}`short_junction` with $t=0$.
```

Equation {eq}`quantization_condition` does not have a general closed-form solutions.
However, we can can obtain approximate solutions by making some simplifying, but reasonable assumptions.
First, we assume large carrier density $k_{e/h} \ll k_F$ (*Andreev approximation*) and linearize $k_e = \sqrt{k_F^2 + \frac{2mE}{k_F \hbar^2}} \approx k_F  + \frac{E}{\hbar v_F}$, where $v_F$ is the Fermi velocity. An analogous calculation for the hole branch yields find $k_h \approx k_F  - \frac{E}{\hbar v_F}$.
Because we're interested in low-lying states we may also expand $\arccos (E / \Delta) \approx \pi/2 - E / \Delta$.
Plugging these approximate expressions in {eq}`quantization_condition` we obtain levels that disperse linearly with the phase:

$$
E = \frac{\hbar}{2}\frac{1}{\tau_\text{AR} + \tau_\text{dw}} (2\pi (n + \frac{1}{2}) + \varphi).
$$

Analogously to the square-well potential, the level spacing decreases with the length of junction. Calculating the full Josephson current of this model is out of scope for this section, as it requires carrying out complicated sums over all levels and including continuum contributions {cite}`kulik1969macroscopic, ishii1970josephson`. Nevertheless, it is instructive to compute the current carried by a single level in the limit of $\tau_\text{AR} \gg \tau_\text{dw}$

$$
I = \frac{2e}{\hbar} \frac{\partial E}{\partial \varphi} \approx \frac{2e}{2\tau_\text{AR}} = \frac{2e}{2 v_F / L}
$$

This corresponds to the expected supercurrent mediated by Andreev reflections occuring at every $\tau_\text{AR}$.

## Comparison of models
We summarize the features of each model in {numref}`model-table`.

```{list-table} Comparison of models. Definitions of some variables: $\xi$, $\tau_\text{dw}$, $\Gamma$, $\delta \Gamma$
:header-rows: 1
:name: model-table

* - Model
  - Basis
  - Physical limit
  - Relevant parameters
  - Supercurrent scale
  - Can describe
* - Dot
  - Localized dot wavefunctions
  - $\Gamma, \varepsilon \ll \Delta, L \ll \xi$
  - $\varepsilon, \Gamma, \delta \Gamma$
  - $e \Gamma / \hbar$
  - Finite charging energy
* - Short junction
  - Scattering states in the superconducting leads
  - $L \ll \xi$
  - $\Delta, \tau$
  - $e \Delta / \hbar$
  - Point scatterers
* - Long junction
  - Scattering states in the normal region
  - $L \gg \xi$
  - $\tau_\text{dw}, \tau$
  - $e / \tau_\text{dw}$
  - Band structure
```

# Sub-fields of Andreev states
Initial experiments on Andreev states were carried out in metallic junctions where these states form a continuum.
Modern research, however, focuses on resolving and manipulating individual states.

## Superconductor-semiconductor structures
Due to their low density of states, semiconductors offer a reliable platform to confine only a small number of states between two superconductors.
Additionally, the variability of the material physical properties allows to extend Andreev physics by combining it with other phenomena: spin physics, Coulomb blockade and tunability of electron wave functions in the normal region.
Initial attempts to observe Josephson physics in quantum wells were met with fabrication difficulties.
However, the second generation of experiments focusing on carbon nanotubes, semiconducting nanowires and, later, graphene, resulted in a reliable and commonly used approach.
Nowadays, gradual accumulation of expertise in fabrication and combining different materials enabled a wide variety of platforms and devices to be within experimental reach.

## Qubit applications
Qubits based on superconducting circuits (such as transmons or charge qubits) rely on bosonic excitations of the superconducting condensate which are mediated by a large number of ABS.
In contrast, Andreev qubits store quantum information in the fermionic degrees of freedom of individual Andreev doublets.
Specifically, in *Andreev level qubits* the computational basis corresponds to the even manifold of the doublet.
Information is therefore encoded in the number of quasiparticles trapped in the junction.
*Andreev spin qubits* rely instead on the odd manifold, with the qubit states corresponding to the spin of a single trapped quasiparticle.
In this case, spin-orbit interaction becomes a necessary ingredient to lift spin degeneracy and allow control of individual states.
In both types of qubits, readout is typically performed by measuring state-dependent supercurrent or resonator frequency shifts, whereas qubit operations can be achieved through microwave irradiation.

## Multiterminal devices
Attaching three or more superconducting contacts to a weak link enables physical phenomena with no analogues in two-terminal devices.
One example is *multiplet supercurrent*, where multiterminal Andreev states mediate dissipationless charge transfers across superconducting electrodes at finite voltage.
The simplest implementation of this is a three-terminal device where two terminals biased at $n_1 V_1 = n_2 V_2$ each transfer $n_1$ and $n_2$ Cooper pairs to a third grounded terminal.
Another popular avenue of research focuses on realizing effective topological matter in multiterminal junctions, where the superconducting phase differences play the role of crystal momenta.
By carefully engineering the weak link, the resulting Andreev bands can host topologically protected Weyl points that serve as monopoles of Berry curvature.
In some 2D planes of parameter space this Berry curvature can integrate to non-zero Chern numbers, which manifests as quantized transconductance.
Extending the sample geometry with multiple normal regions weakly coupled through superconductors implements Andreev molecules due to crossed Andreev reflection processes.

## Majorana zero modes
Carefully engineering a combination of superconducting proximity effect, control over the electron spin and sppatial position allows to split a single Andreev bound state into two.
The fractionalized nature of Majorana zero modes also allows manipulation of quantum information in an error-free way.
Each of the halves---the Majorana zero modes---is protected from dephasing because they are pinned to zero energy due to particle-hole symmetry.
Despite this proposed robustness, reliably creating Majorana states is a challenging task with active experimental search under way.

## Other topics
Andreev physics also manifests in the following physical systems:
- Yu-Shiba-Rusinov states bound to magnetic impurities at the surface of a superconductor
- Caroli-de Gennes-Matricon states in the vortex cores of type-II superconductors
- States confined to a scattering region of superconducting break junctions

## References
```{bibliography}
:filter: docname in docnames
```
