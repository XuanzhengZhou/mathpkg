---
role: proof
locale: en
of_concept: mathcalp-has-the-direct-limit-property
source_book: gtm001
source_chapter: "15"
source_section: ""
---

Let $\Pi = \langle \eta_i, \pi_{ij} \rangle_{i \leq j}$ be a well-founded direct system of strong $\mathcal{P} <$ maps with an index set $\langle I, \leq \rangle$. First we shall show by induction on $J(\hat{\pi}_{i\infty}(\alpha))$ that if $J^{\eta_i}(\alpha) \simeq \beta$, then $J(\hat{\pi}_{i\infty}(\alpha)) = \pi_{i\infty}(\beta)$. Let $\delta \in \eta_\infty^\circ$ be such that $\delta < \hat{\pi}_{i\infty}(\alpha)$. Then there exist $j \geq i$ and $\delta' \in \eta_j^\circ$ such that $\hat{\pi}_{j\infty}(\delta') = \delta$. If we put $\alpha' = \hat{\pi}_{ij}(\alpha)$, then we have $\hat{\pi}_{j\infty}(\delta') < \hat{\pi}_{i\infty}(\alpha) = \hat{\pi}_{j\infty}(\alpha')$, and so $J(\hat{\pi}_{j\infty}(\delta')) < J(\hat{\pi}_{i\infty}(\alpha))$. By the induction hypothesis, we see that $J(\delta) = \pi_{j\infty}(J(\delta'))$. Since $\pi_{j\infty}$ is order preserving and $\hat{\pi}_{j\infty}(\delta') < \hat{\pi}_{j\infty}(\alpha')$, we have $\delta' < \alpha'$. Noting that $J(\alpha') = J^{\eta_j}(\

Remark. We next introduce a ramified language $\mathcal{L}$, to provide a notation for each member of $L$, the class of constructible sets. The symbols of $\mathcal{L}$ are the following:

Variables: $x_0, x_1, \ldots, x_n, \ldots$ ($n \in \omega$).
Relation symbols: $\in, =$.
Propositional connectives: $\neg, \vee$.
Quantifiers: $\exists^\alpha (\alpha \in \text{On})$.
Abstraction operators: $\wedge^\alpha (\alpha \in \text{On})$.
Parenthesis: $(,)$.
