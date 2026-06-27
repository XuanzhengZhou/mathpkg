---
role: proof
locale: en
of_concept: injective-sheaf-homomorphism-into-w
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---

Clearly $i_U(s) \mid V = i_V(s \mid V)$ for $s \in \Gamma(U, \mathcal{S})$. If we identify the sheaf induced by $\{\Gamma(U, \mathcal{S}), r_V^U\}$ with the sheaf $\mathcal{S}$, then it follows from Theorem 2.1 of Chapter IV that there exists exactly one sheaf morphism $\varepsilon: \mathcal{S} \to W(\mathcal{S})$ with $\varepsilon_*(s) = r \, i_U(s)$ for $s \in \Gamma(U, \mathcal{S})$.

To prove injectivity: let $\sigma \in \mathcal{S}_x$ and suppose $\varepsilon(\sigma) = \mathbf{O}_x$. Then there exists a neighborhood $U(x) \subset X$ and an $s \in \Gamma(U, \mathcal{S})$ with $s(x) = \sigma$. Therefore
$$\mathbf{O}_x = \varepsilon(\sigma) = \varepsilon \circ s(x) = \varepsilon_*(s)(x) = r \, i_U(s)(x).$$
Since $r$ is an isomorphism (Theorem 1.2(1)), this implies $i_U(s)(x) = \mathbf{O}_x$, hence $s(x) = \sigma = \mathbf{O}_x$ in $\mathcal{S}_x$. Thus $\varepsilon$ is injective.
