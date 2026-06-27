---
locale: en
of_concept: let-xi-x-p-b-be-a-principal-g-bundle-and-let-xif-x-f-p-f-b-b
role: proof
source_book: gtm020
source_chapter: 4. General Fibre Bundles
source_section: '8'
---

Since $(xt, \phi(xt))G = (xt, t^{-1}\phi(x))G = (x, \phi(x))G$ in $X_F = X \times F \bmod G$, the function $s_\phi$ is well defined. Since $s_\phi$ is the factorization of $x \mapsto (x, \phi(x))G$ by the quotient map $p$, the function $s_\phi$ is continuous. Clearly, the relation $p_F(s_\phi(xG)) = p_F((x, \phi(x))G) = p(x) = xG$ holds, and the map $s_\phi$ is a cross section.

Conversely, let $s$ be a cross section of $\xi[F]$, and let $\phi_s$: $X \rightarrow F$ be defined by the relation $s(xG) = (x, \phi_s(x))G$ for each $x \in X$. Since $(x, \phi_s(X))G = (xt, t^{-1}\phi_s(x))G = (xt, \phi_s(xt))G$, and since $s$ is a cross section, the function $\phi_s$ satisfies the relation $\phi_s(xt) = t^{-1}\phi_s(x)$ for each $x \in X$,

Proof. By Theorem (8.1) the set of cross sections of $\xi[X']$ are in bijective correspondence with $G$-morphisms $\phi_s: X \rightarrow X'$, that is, maps $\phi_s: X \rightarrow X'$ with $\phi_s(xt) = t^{-1}\phi_s(x) = \phi_s(x)t$.

From the relation $f = (p'_X)s$, we observe that $s(xG) = (x, \phi_s(x))G$ and $p'_X(s(xG)) = p'_X((x, \phi_s(x))G) = p'_X(\phi_s(x))$ for $x \in X$. Since $f(xG) = p'_X(\phi_s(x))$, we have the relation $f = (p'_X)s$. This proves the corollary.

This corollary reduces the problem of the existence of a principal bundle morphism $\xi \rightarrow \xi'$ to a more manageable problem of the existence of a cross section. In particular, we can apply the results of Chap. 2, Sec. 7. An application of this corollary is a decisive step in the homotopy classification of locally trivial fibre bundles, and it plays a role similar to that of Gauss maps for vector bundles.
