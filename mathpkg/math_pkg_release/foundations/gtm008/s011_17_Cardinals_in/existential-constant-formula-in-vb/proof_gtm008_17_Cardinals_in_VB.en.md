---
role: proof
locale: en
of_concept: existential-constant-formula-in-vb
source_book: gtm008
source_chapter: "17"
source_section: "Cardinals in V^{(B)}"
---

This is derived from Theorem 17.8 in the same way that Corollary 13.23 was derived from Theorem 13.22. The key step uses the fact that $[F(\alpha)^{\vee} = F(\check{\alpha})] = 1$, hence

$$\llbracket \text{Const}(u) \rrbracket = \sum_{\alpha \in On} \llbracket u = F(\check{\alpha}) \rrbracket \cdot \llbracket (F(\alpha))^{\vee} = F(\check{\alpha}) \rrbracket$$

$$= \sum_{\alpha \in On} \llbracket u = (F(\alpha))^{\vee} \rrbracket$$

$$= \sum_{x \in L} \llbracket u = \check{x} \rrbracket.$$

Therefore

$$\llbracket (\exists u) [\text{Const}(u) \wedge \varphi(u)] \rrbracket = \sum_{x \in L} \llbracket \varphi(\check{x}) \rrbracket.$$
