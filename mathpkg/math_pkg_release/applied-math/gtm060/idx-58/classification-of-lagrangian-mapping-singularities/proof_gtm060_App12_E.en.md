---
role: proof
locale: en
of_concept: classification-of-lagrangian-mapping-singularities
source_book: gtm060
source_chapter: "Appendix 12"
source_section: "E. Lagrangian equivalence"
---

The classification theorem for Lagrangian mapping singularities up to dimension $n \leq 5$ relies on the following key ingredients:

**1. Reduction to generating families.** Every Lagrangian submanifold $L \subset T^*\mathbb{R}^n$ that projects submersively onto some coordinate subspace can be described locally by a generating function $F(p_I, q_J)$ via
$$q_I = \frac{\partial F}{\partial p_I}, \quad p_J = -\frac{\partial F}{\partial q_J}.$$
At points where the projection is not submersive, one applies a linear symplectic change of coordinates (a "canonical transformation") to achieve this form.

**2. Lagrangian equivalence = contact equivalence of generating families.** Two Lagrangian mappings are Lagrangian equivalent if and only if their generating families are stably contact equivalent. This reduces the geometric classification problem to an algebraic one about function germs.

**3. Classification of simple function singularities.** The classification of simple critical points of functions (no parameters) up to right equivalence yields the ADE series: $A_k$ ($x^{k+1}$), $D_k$ ($x^2y \pm y^{k-1}$), $E_6$ ($x^3 \pm y^4$), $E_7$ ($x^3 + xy^3$), $E_8$ ($x^3 + y^5$). The simple singularities are those of modality 0 — they have no continuous moduli.

**4. Versal deformations.** The generating family $F(p_i, q_j)$ is a deformation of the function singularity $f(p_i) = F(p_i, 0)$. For the mapping to be stable, this deformation must be versal (i.e., transverse to the orbit of $f$ under the contact group). The parameters $q_j$ play the role of deformation parameters. The versality condition restricts which function singularities can appear as typical Lagrangian singularities in a given dimension $n$.

**5. Dimension counting.** An $A_k$ singularity has codimension $k-1$ in the space of function germs, so it becomes generic (unavoidable) in Lagrangian mappings when $n \geq k-1$. A $D_k$ singularity has codimension $k-1$ and becomes generic when $n \geq k-1$ with at least two $p$-variables. This explains the tables:
- For $n=1$: only $A_1$ (codim 0) and $A_2$ (codim 1) are generic.
- For $n=2$: $A_3$ (codim 2) additionally becomes generic.
- For $n=3$: $A_4$ (codim 3) and $D_4$ (codim 3) become generic.
- The $E_6, E_7, E_8$ singularities (codim 6, 7, 8) appear first in dimensions $n=5$ and above.

**6. Stability.** The stability of these singularities under small Lagrangian perturbations follows from the fact that the versal deformation is stable — any small perturbation of the generating family is contact equivalent to the original family after a suitable change of parameters. Thus, complicated singularities break up into collections of the simple ones under small generic perturbations.

The proof that Lagrangian equivalence is finer than right-left equivalence of the projection maps follows from the fact that not every diffeomorphism of the configuration space lifts to a symplectic diffeomorphism of the cotangent bundle. Only those diffeomorphisms of $M$ whose lift preserves the symplectic form can be used, which imposes additional constraints on the admissible coordinate changes.
