---
locale: en
of_concept: let-x-be-an-n-dimensional-cw-complex-with-one-n-cell-and-let
role: proof
source_book: gtm020
source_chapter: 16. Vector Fields on the Sphere
source_section: '1'
---

If $X$ is reducible, there must be a reduction map $f: S^n \rightarrow X$ (in dimension $n$) by the homology condition. To prove that $vf$ is homotopic to the identity, consider the following diagram:

$$\tilde{H}_n(S^n) \rightarrow \tilde{H}_n(X) \rightarrow \tilde{H}_n(S^n) \rightarrow \tilde{H}_{n-1}(X_{n-1})$$

Since $\tilde{H}_{n-1}(X^{n-1})$ is a free abelian group, $v_*$ is an isomorphism, and, by hypothesis, $f_*$ is an isomorphism. Consequently, $(vf)_*$ is an isomorphism and $vf$ is homotopic to the identity. Conversely, the existence of such an $f$ with $vf$ of degree 1 yields a reduction of $X$ since $\tilde{H}_n(X)$ has at most one generator.
