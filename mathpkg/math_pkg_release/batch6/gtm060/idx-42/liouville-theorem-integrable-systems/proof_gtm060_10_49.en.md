---
role: proof
locale: en
of_concept: liouville-theorem-integrable-systems
source_book: gtm060
source_chapter: "10"
source_section: "49"
---

**Proof.** The proof proceeds in several steps.

1. **Invariance and smoothness.** Since $(F_i, F_j) \equiv 0$ for all $i, j$, each $F_i$ Poisson-commutes with $H = F_1$. Therefore each $F_i$ is a first integral, and the level set $M_{\mathbf{f}}$ is invariant under the hamiltonian flow of $H$. The independence of the $1$-forms $dF_i$ on $M_{\mathbf{f}}$ implies (by the implicit function theorem) that $M_{\mathbf{f}}$ is a smooth $n$-dimensional submanifold.

2. **Torus structure.** On $M_{\mathbf{f}}$, the $n$ hamiltonian vector fields $X_{F_i}$ (defined by $\iota_{X_{F_i}} \omega^2 = -dF_i$) are everywhere linearly independent (since the $dF_i$ are independent) and mutually commute (since $(F_i, F_j) = 0$ implies $[X_{F_i}, X_{F_j}] = 0$). These $n$ commuting vector fields on a compact connected $n$-manifold define an $\mathbb{R}^n$-action. Compactness implies the stabilizer is a full-rank lattice, giving $M_{\mathbf{f}} \cong \mathbb{R}^n / \mathbb{Z}^n \cong T^n$.

3. **Conditionally periodic motion.** In the angular coordinates $\boldsymbol{\varphi}$ coming from the torus identification, each vector field $X_{F_i}$ corresponds to a constant vector field $\boldsymbol{\omega}_i$. Since the hamiltonian flow of $H = F_1$ is precisely $X_{F_1}$, we obtain $d\boldsymbol{\varphi}/dt = \boldsymbol{\omega}$, where $\boldsymbol{\omega}$ depends only on the values $\mathbf{f}$ of the first integrals.

4. **Integration by quadratures.** The existence of $n$ independent commuting first integrals allows one to introduce action-angle variables $(\mathbf{I}, \boldsymbol{\varphi})$ via a canonical transformation. In these variables, the hamiltonian depends only on the action variables $\mathbf{I}$, and the equations of motion become $\dot{\mathbf{I}} = 0$, $\dot{\boldsymbol{\varphi}} = \partial H/\partial \mathbf{I} = \text{const}$, which are immediately integrable by quadratures.
