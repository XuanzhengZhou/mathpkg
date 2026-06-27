---
role: proof
locale: en
of_concept: recurrence-time-distribution-duality
source_book: gtm040
source_chapter: "9"
source_section: "4"
---

By Lemma 6-34, for $n \geq 1$, the taboo return probability can be expressed as a sum over paths that avoid state $0$ before the final step. Using the duality relation $P_{ij} = \frac{\alpha_j}{\alpha_i} \hat{P}_{ji}$, each path in the sum for $\bar{F}_{00}^{(n)}$ corresponds bijectively to the reversed path in the sum for $\hat{\bar{F}}_{00}^{(n)}$, with the product of transition probabilities being identical due to telescoping cancellation of the $\alpha$ factors.
