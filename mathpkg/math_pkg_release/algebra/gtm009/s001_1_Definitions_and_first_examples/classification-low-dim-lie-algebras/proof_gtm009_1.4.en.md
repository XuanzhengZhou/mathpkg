---
role: proof
locale: en
of_concept: classification-low-dim-lie-algebras
source_book: gtm009
source_chapter: "1"
source_section: "1.4"
---

**Dimension 1:** Let $x$ be a basis vector. By (L2), $[xx] = 0$, so the bracket is identically zero. The algebra is abelian and unique.

**Dimension 2:** Let $x, y$ be a basis of $L$. By bilinearity, all products are determined by $[xy]$, since $[xx] = [yy] = 0$ by (L2) and $[yx] = -[xy]$ by (L2').

Write $[xy] = ax + by$ for some scalars $a, b \in F$.

If $a = b = 0$, then $[xy] = 0$ and $L$ is abelian.

Otherwise, assume $(a, b) \neq (0, 0)$. We perform a change of basis to simplify the structure.

First, note that $[xy]$ spans a 1-dimensional subspace of $L$. Replace $x$ by a vector spanning this subspace: choose $x'$ to be any nonzero scalar multiple of $[xy]$. Take $y'$ to be any vector linearly independent of $x'$. Then $[x'y'] = cx'$ for some $c \neq 0$ (since $[x'y']$ is a multiple of $x'$, and the bracket is nontrivial).

Now replace $y'$ by $c^{-1}y'$. Since the bracket is bilinear:
$$[x', c^{-1}y'] = c^{-1}[x'y'] = c^{-1}(cx') = x'.$$

Thus, after relabeling $x, y$, we obtain $[xy] = x$.

It remains to verify that this multiplication table indeed defines a Lie algebra. Axioms (L1) and (L2) are clear. For (L3), check the Jacobi identity on the basis:
$$[x[xy]] + [x[yx]] + [y[xx]] = [xx] + [x, -x] + [y, 0] = 0 - [xx] + 0 = 0 - 0 = 0.$$
$$[y[xy]] + [x[yy]] + [y[yx]] = [yx] + [x, 0] + [y, -x] = -x + 0 - [yx] = -x + x = 0.$$

Thus $[xy] = x$ defines a valid Lie algebra, unique up to isomorphism among nonabelian 2-dimensional Lie algebras.
