---
role: proof
locale: en
of_concept: f-stage-subset-of-previous-stages
source_book: gtm001
source_chapter: "15"
source_section: ""
---

**Proof.** (1) By transfinite induction. Let $\beta = K_1'\alpha$, $\gamma = K_2'\alpha$, $n = K_3'\alpha$. If $n = 0$: $F'\alpha = F''\alpha$, done. If $n \neq 0$: by Proposition 15.10, $\beta < \alpha$ and $\gamma < \alpha$, so $F'\beta, F'\gamma \in F''\alpha$. If $n = 1$: $F'\alpha = \{F'\beta, F'\gamma\} \subseteq F''\alpha$. If $n > 1$: $F'\alpha = \mathcal{F}_n(F'\beta, F'\gamma) \subseteq F'\beta$, and by induction $F'\beta \subseteq F''\beta \subseteq F''\alpha$.
