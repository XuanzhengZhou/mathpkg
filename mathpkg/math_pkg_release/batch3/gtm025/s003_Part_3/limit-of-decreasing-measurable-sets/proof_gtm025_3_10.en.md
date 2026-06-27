---
role: proof
locale: en
of_concept: limit-of-decreasing-measurable-sets
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** The sequence $(A_1 \cap A_n')$ is nondecreasing with terms in $\mathcal{A}$. By (10.13),
$$\mu(A_1) - \lim_{n} \mu(A_n) = \lim_{n} (\mu(A_1) - \mu(A_n)) = \lim_{n} \mu(A_1 \cap A_n')$$
$$= \mu\left(\bigcup_{n=1}^{\infty} (A_1 \cap A_n')\right) = \mu(A_1 \cap \bigcup_{n} A_n') = \mu(A_1) - \mu\left(\bigcap_{n=1}^{\infty} A_n\right).$$
Thus $\lim \mu(A_n) = \mu(\bigcap A_n)$. $\square$
