---
role: proof
locale: en
of_concept: theorem-6-9
source_book: gtm040
source_chapter: "6"
source_section: "9"
---

**Proof:** Order the states by the positive integers, let $E$ be the first $n$ of the states, and let $F$ be the first $n + 1$. Then $P^E$ and $P^F$ are ergodic chains and have regular measures $\alpha^E$ and $\alpha^F$. Also $(P^F)^E = P^E$. Thus $\alpha^F$ is $P^E$-regular by Lemma 6-7, and we may choose $\alpha^F$ such that $\alpha^F = \alpha^E$ by the uniqueness part of Proposition 6-4. The procedure of adding a single state to $F$ may be continued by induction, and we set $\alpha = \lim_{E \to S} (\alpha^E 0)$. Now for any of these sets $E$ we have

$$\alpha_E T \leq \alpha_E T + \alpha_E UNR = \alpha_E P^E = \alpha_E$$

or

$$\alpha_E T \leq \alpha_E.$$
