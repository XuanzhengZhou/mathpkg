---
role: proof
locale: en
of_concept: limit-of-increasing-measurable-sets
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** Write $\bigcup_{n=1}^{\infty} A_n = A_1 \cup \bigcup_{n=2}^{\infty} (A_n \setminus A_{n-1})$, a disjoint union. By countable additivity,
$$\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \mu(A_1) + \sum_{n=2}^{\infty} \mu(A_n \setminus A_{n-1}) = \mu(A_1) + \sum_{n=2}^{\infty} (\mu(A_n) - \mu(A_{n-1}))$$
$$= \lim_{n \to \infty} \mu(A_n). \quad \square$$
