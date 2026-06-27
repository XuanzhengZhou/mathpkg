---
role: proof
locale: en
of_concept: bott-periodicity-isomorphism
source_book: gtm020
source_chapter: "IV"
source_section: "9"
---

We prove by induction on $k$ that the Bott map $\beta$ is an isomorphism for $X = S^{2k}$ and that the integrality statement holds.

Consider the following commutative diagram:

$$\tilde{K}(S^{2k}) \xrightarrow{\beta} \tilde{K}(S^{2k+2})$$
$$\downarrow{\scriptstyle \mathrm{ch}} \qquad\qquad \downarrow{\scriptstyle \mathrm{ch}}$$
$$\tilde{H}^*(S^{2k}, \mathbf{Z}) \xrightarrow{\smile u} \tilde{H}^*(S^{2k+2}, \mathbf{Z}) \subset \tilde{H}^*(S^{2k+2}, \mathbf{Q})$$

where $u \in H^2(S^2, \mathbf{Z})$ is the canonical generator. The diagram commutes since $\mathrm{ch}(\gamma - 1) = u$. The bottom horizontal arrow (cup product with $u$) is an isomorphism.

If $\mathrm{ch}$ factors through $\tilde{H}^*(S^{2k}, \mathbf{Z})$ by an isomorphism, then $\beta$ is injective. By Remark (9.5), $\beta$ is surjective, hence $\beta$ is bijective. If $\beta$ is an isomorphism, then $\mathrm{ch}$ factors through $\tilde{H}^*(S^{2k+2}, \mathbf{Z})$ by an isomorphism.

The induction starts at $k = 1$ with Proposition 9.1, which establishes that $\mathrm{ch} \colon K(S^2) \to H^*(S^2, \mathbf{Z})$ is an isomorphism. Thus the integrality theorem holds.

Since $\tilde{K}(S^1) = [S^0, U]_0$ and $U$ is connected, and since $\beta$ is an epimorphism, we conclude that $\tilde{K}(S^{2k+1}) = 0$ for all $k$.
