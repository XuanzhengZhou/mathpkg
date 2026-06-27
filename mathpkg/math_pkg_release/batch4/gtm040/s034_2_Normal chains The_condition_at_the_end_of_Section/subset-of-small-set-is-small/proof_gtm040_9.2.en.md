---
role: proof
locale: en
of_concept: subset-of-small-set-is-small
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

By Proposition 5-8, we have $B^E = B^F B^E$. Since $F$ is a small set, each row of $P^n B^F$ tends to the probability vector $\lambda^F$. It follows from Proposition 1-57 (convergence of matrix products) that
$$P^n B^E = P^n B^F B^E \to 1 \lambda^F B^E.$$
Thus $\lambda^E = \lambda^F B^E$ exists. In addition,
$$\lambda^E 1 = \lambda^F B^E 1 = \lambda^F 1 = 1,$$
so $E$ is a small set by Definition 9-35.
