---
role: proof
locale: en
of_concept: affine-plane-transitivity-equivalence
source_book: gtm006
source_chapter: "XIV"
source_section: "3"
---
**Proof of Theorem 14.6.** Let $\mathcal{A} = \mathcal{P}^{l_{\infty}}$.

**(i) $\Rightarrow$ (ii):** Suppose $\Pi$ is transitive on affine lines. Since each affine point lies on $n+1$ affine lines, and each affine line contains $n$ affine points, the transitivity on affine lines implies transitivity on affine points via simple counting. For transitivity on special points (points of $l_{\infty}$): each special point is the intersection of $n$ mutually parallel affine lines; the action of $\Pi$ on parallel classes must be transitive.

**(ii) $\Rightarrow$ (iii):** If $\Pi$ is transitive on affine points and on special points, consider any affine flag $(C,l)$. By transitivity on affine points, we may map any point to $C$; the stabilizer $\Pi_C$ must then move $l$ to any other line through $C$, which follows from the transitivity on special points and the incidence structure.

**(iii) $\Rightarrow$ (i):** Transitivity on affine flags immediately implies transitivity on affine lines, since each affine flag contains an affine line, and the projection from flags to lines is surjective and $\Pi$-equivariant.

Thus all three conditions are equivalent. $\square$

If $\Pi$ is transitive on the affine flags of $\mathcal{A}$ then, since $\Pi_{C^{\alpha}, l^{\alpha}} = \alpha^{-1} \Pi_{C,l} \alpha$, the stabilizer order $|\Pi_{C,l}|$ is the same for all affine flags $C, l$ of $\mathcal{A}$.
