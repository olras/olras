# Minimal models
We begin our discussion by analyzing three simple limiting models that illustrate interesting properties of ABS.

## Weakly couple quantum dot
We consider a small metallic region with a single fermionic level with a hamiltonian coupled to two superconducting reservoirs with a phase difference $\varphi$.
The bare hamiltonian of the dot reads

$$
H_\mathrm{dot} = -\mu (c_\downarrow^\dagger c_\downarrow + c_\uparrow^\dagger c_\uparrow)
$$

where $\mu$ is the chemical potential of the dot.
The proximity with the superconducting reservoirs induces superconducting correlations in dot.
Within the mean-field approximation, we can model this effect with the term

$$
H_\mathrm{SC} = (\Delta_1 + \Delta_2 e^{i\varphi}) c_\uparrow c_\downarrow  + (\Delta_1 + \Delta_2 e^{-i\varphi})  c_\downarrow^\dagger c_\uparrow^\dagger
$$

with $\Delta_{1, 2}$ the superconducting pairing of the two superconductors.
Using the Bogoliubov De Gennes formalism, we can bring the Hamiltonian to a quadratic form

$$
\begin{aligned}
\mathcal{H} &= \frac{1}{2} \mathbf{\mathcal{C}}^\dagger
\begin{pmatrix}
-\mu & 0 & 0 & -\Delta_1 - \Delta_2 e^{-i\varphi}\\
0 & -\mu & \Delta_1 + \Delta_2 e^{-i\varphi} & 0\\
0 & \Delta_1 + \Delta_2 e^{i\varphi} & \mu & 0\\
-\Delta_1 - \Delta_2 e^{i\varphi}  & 0 & 0 & \mu \end{pmatrix}\mathbf{\mathcal{C}} \\
&= \frac{1}{2} \mathbf{\mathcal{C}}^\dagger H_\mathrm{BdG} \mathbf{\mathcal{C}}^\dagger
\end{aligned}
$$

where $\mathbf{\mathcal{C}} = \begin{pmatrix} c_{\uparrow} & c_{\downarrow} & c_{\uparrow}^\dagger & c_{\downarrow}^\dagger \end{pmatrix}^T$.
Though $H_\mathrm{BdG}$ is a $4 \times 4$ matrix, it has the tensor product structure

$$
 H_\mathrm{BdG}= -\mu \tau_z \otimes \mathbb{I} + (\Delta_1 + \Delta_2 \cos \varphi) \mathbb{I} \otimes \sigma_x + \Delta_2 \sin \varphi \mathbb{I} \otimes \sigma_y
$$


# Sub-fields of Andreev states

## Superconductor-semiconductor structures

## Andreev bound states as qubits

## Metallic weak links

## Multiterminal devices

## Majorana zero modes
