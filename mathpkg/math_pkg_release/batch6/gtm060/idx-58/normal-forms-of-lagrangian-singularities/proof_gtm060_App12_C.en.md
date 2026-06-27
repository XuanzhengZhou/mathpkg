---
role: proof
locale: en
of_concept: normal-forms-of-lagrangian-singularities
source_book: gtm060
source_chapter: "Appendix 12"
source_section: "C. Tables of normal forms"
---

The derivation of normal forms relies on the theory of generating families and the classification of critical points of functions. For a Lagrangian submanifold $L \subset T^*\mathbb{R}^n$, locally one can find a generating function $F(p_I, q_J)$ where $(I, J)$ is a partition of $\{1,\ldots,n\}$, such that

$$L = \left\{(p,q) : q_I = \frac{\partial F}{\partial p_I},\; p_J = -\frac{\partial F}{\partial q_J}\right\}.$$

The projection of $L$ onto the $q$-space has singularities at points where the Hessian $\partial^2 F/\partial p_I^2$ is degenerate. The type of singularity is determined by the contact equivalence class of the generating family $F$, viewed as a deformation of a function singularity.

The classification proceeds by:

1. **$A_k$ series**: These arise when the generating function depends on a single variable $p_1$ and the singularity type is determined by the contact class of $F(p_1, q_J)$. The normal forms $F = \pm p_1^{k+1} + q_k p_1^{k-1} + \cdots + q_2 p_1^2$ correspond to the versal deformations of the $A_k$ function singularity $f(p_1) = \pm p_1^{k+1}$.

2. **$D_k$ series**: These occur when the generating function depends on two variables $p_1, p_2$ (so $i = 1, 2$). The normal form $F = \pm p_1^2 p_2 \pm p_2^{k-1} + q_k p_2^2$ is the versal deformation of the $D_k$ boundary singularity $f(p_1, p_2) = \pm p_1^2 p_2 \pm p_2^{k-1}$.

3. **$E_6, E_7, E_8$**: These exceptional singularities appear first in dimensions $n \geq 5$ and correspond to the simple elliptic and parabolic function singularities.

The fact that the same function $F(p_i, q_j)$ describes Lagrangian manifolds in any dimension $\geq k$ is a consequence of the stability theorem: adding "dummy" parameters $q_j$ on which $F$ does not depend is a trivial extension that preserves the singularity type up to Lagrangian equivalence.

**Geometric interpretation of low-dimensional cases:**
- $A_2$ (fold): The projection map is $(p_1, q_j) \mapsto (\pm 3p_1^2, q_j)$ — a fold onto a half-line.
- $A_3$ (cusp): The mapping $(p_1, q_2) \mapsto (\pm 4p_1^3 + 2q_2 p_1, q_2)$ produces a semi-cubical cusp $27x^2 = 4y^3$ on the caustic.
- $A_4$ (swallowtail): Appears first in three dimensions; the caustic is a surface with a swallowtail singularity.
- $D_4$: The caustic is a surface with three cuspidal edges (all of type $A_3$) meeting tangentially at a point. Two variants exist depending on whether the two extra edges are real or purely imaginary.

For complete details of the classification theorem, see Arnold's original papers on Lagrangian singularities and the references cited in the text (Arnold, *Normal forms of functions near degenerate critical points*, Functional Anal. Appl. 6 (1972), 254–272).
