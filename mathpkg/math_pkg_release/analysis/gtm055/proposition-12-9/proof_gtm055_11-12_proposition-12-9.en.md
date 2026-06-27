---
role: proof
locale: en
of_concept: proposition-12-9
source_book: gtm055
source_chapter: "11-12"
source_section: "Section 13_Section_13"
---

Proof. To verify the first part of the proposition it suffices to show that if $R$ is a left inverse of $T$ with $\| R \| = d$, and if $\| S - T \| < 1/d$, then $S$ is left invertible. But in these circumstances we have

$$\| 1_{\mathcal{E}} - RS \| = \| R(T - S) \| \leq \| R \| \| S - T \| < 1,$$

so that $RS$ is invertible by the preceding lemma. Thus $(RS)^{-1}(RS) = 1$, and $(RS)^{-1}R$ is a left inverse of $S$. To complete the proof, let $0 < \varepsilon < \frac{1}{2}$ and suppose that $T \in \mathcal{U}$ and that $\| S - T \| < \varepsilon/\| T^{-1} \|$. Then, as we have just
