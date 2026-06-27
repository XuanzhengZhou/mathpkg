---
role: proof
locale: en
of_concept: jordan-decomposition-linear-form
source_book: gtm003
source_chapter: "4"
source_section: "4.2"
---

The proof rests on the existence of sufficiently many positive linear forms on a given $C^*$-algebra; essentially, this is a consequence of (V, 3.3) Corollary 3 and its predecessors, i.e., of the normality of the positive cone $A_+$. The decomposition is obtained by applying the standard Jordan decomposition in ordered vector spaces, using that $A'_+$ is a generating cone in the self-adjoint part of $A'$.

If $\phi$ is a positive linear form on $A$, the definition $[x, y]_\phi := \phi(y^*x)$ ($x, y \in A$) yields a positive semi-definite Hermitian form on the underlying complex vector space of $A$ (Chapter II, Section 2, Example 5). Its kernel $A_\phi := \{x : [x, x]_\phi = 0\}$ is clearly closed, because $\phi$ is continuous, and a left ideal because of

$$0 \leq \phi(x^*y^*yx) \leq \|y\|^2 \phi(x, x) \quad (x, y \in A),$$

which follows from (3.2)(i). Thus the quotient vector space $A/A_\phi$ is a pre-Hilbert space on which $[\,,\,]$ induces an inner product.

The uniqueness follows from the additivity of the dual norm on $A'_+$ (Corollary 2 of 4.1).
