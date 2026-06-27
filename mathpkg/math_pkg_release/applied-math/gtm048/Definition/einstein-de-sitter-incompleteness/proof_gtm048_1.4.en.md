---
role: proof
locale: en
of_concept: einstein-de-sitter-incompleteness
source_book: gtm048
source_chapter: "1"
source_section: "1.4"
---

By Section 1.0.3 and the proof of Proposition 1.4.4,

$$D_Z Z = \sum_{i=1}^{4} Z(\omega^i Z) X_i + \sum_{i,j=1}^{4} \omega_j^i(Z) \omega^j(Z) X_i = (Z1) X_4 + 0 = 0.$$

Thus each integral curve of $Z$ is a geodesic. Now $\gamma: (0, \infty) \rightarrow M$ defined by $\gamma u = (0, 0, 0, u) \in M$ is an integral curve of $Z$; moreover, the scalar curvature obeys $\lim_{u \rightarrow 0} S(\gamma u) = \infty$.

If $(\tilde{M}, \tilde{g})$ were a complete extension, then (by Section 0.0.13) the isometric image $\phi \circ \gamma: (0, \infty) \rightarrow \tilde{M}$ could be extended to a geodesic $\psi: (-\infty, \infty) \rightarrow \tilde{M}$. Then (Exercise 1.0.4) for $\tilde{S}$ the scalar curvature of $(\tilde{M}, \tilde{g})$,

$$\lim_{u \rightarrow 0^+} \tilde{S}(\psi u) = \lim_{u \rightarrow 0^+} (S \circ \phi^{-1}) \psi u = \lim_{u \rightarrow 0} S(\gamma u) = \infty.$$

This contradicts the smoothness of $\tilde{S}$ along $\psi$ and establishes the corollary.
