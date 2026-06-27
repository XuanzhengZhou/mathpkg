---
role: proof
locale: en
of_concept: first-isomorphism-theorem-for-sheaves
source_book: gtm038
source_chapter: "IV"
source_section: "3. Sheaf Morphisms"
---

**Proof.** Define $\bar{\varphi}(\bar{\sigma}) := \varphi(\sigma)$. This gives a stalk-preserving bijective mapping $\bar{\varphi}: \mathcal{S}_1/\operatorname{Ker}\varphi \rightarrow \operatorname{Im}\varphi$ which induces an $\mathcal{O}_{\mathfrak{z}}$-module isomorphism in every stalk.

To verify continuity: if $\bar{\sigma} \in (\mathcal{S}_1/\operatorname{Ker}\varphi)_{\mathfrak{z}}$, then there exists a neighborhood $W(\mathfrak{z})$ and an $s \in \Gamma(W, \mathcal{S}_1)$ with $\bar{s}(\mathfrak{z}) = \bar{\sigma}$. Then $\bar{\varphi} \circ \bar{s} = \varphi \circ s \in \Gamma(W, \operatorname{Im}\varphi)$, showing that $\bar{\varphi}$ is continuous.

Since $\bar{\varphi}$ is bijective, stalk-preserving, and continuous, it is a sheaf isomorphism. $\square$

**Remark (Canonical Decomposition).** If $\mathfrak{q}: \mathcal{S}_1 \rightarrow \mathcal{S}_1/\operatorname{Ker}\varphi$ is the canonical quotient map and $\iota: \operatorname{Im}\varphi \hookrightarrow \mathcal{S}_2$ is the canonical inclusion, then $\varphi$ admits the canonical decomposition:
$$
\varphi = \iota \circ \bar{\varphi} \circ \mathfrak{q}: \mathcal{S}_1 \twoheadrightarrow \mathcal{S}_1/\operatorname{Ker}\varphi \simeq \operatorname{Im}\varphi \hookrightarrow \mathcal{S}_2.
$$
