---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

**Theorem 3.2 (First Isomorphism Theorem for Sheaves)** states that for any analytic sheaf morphism $\varphi: \mathcal{S}_1 \rightarrow \mathcal{S}_2$, the quotient sheaf $\mathcal{S}_1 / \operatorname{Ker}\varphi$ is isomorphic to the image sheaf $\operatorname{Im}\varphi$.

The proof constructs a stalk-preserving bijective mapping $\bar{\varphi}: \mathcal{S}_1 / \operatorname{Ker}\varphi \to \operatorname{Im}\varphi$ via $\bar{\varphi}(\bar{\sigma}) := \varphi(\sigma)$. This induces an $\mathcal{O}_{\mathfrak{z}}$-module isomorphism in every stalk. Continuity of $\bar{\varphi}$ follows from the fact that for any $\bar{\sigma} \in (\mathcal{S}_1/\operatorname{Ker}\varphi)_{\mathfrak{z}}$, there exists a neighborhood $W(\mathfrak{z})$ and a section $s \in \Gamma(W, \mathcal{S}_1)$ with $\bar{s}(\mathfrak{z}) = \bar{\sigma}$ and $\bar{\varphi} \circ \bar{s} = \varphi \circ s \in \Gamma(W, \operatorname{Im}\varphi)$, which makes $\bar{\varphi}$ a sheaf isomorphism.

The theorem is the sheaf-theoretic analog of the first isomorphism theorem for modules and is essential for studying exact sequences and coherence properties of sheaves.
