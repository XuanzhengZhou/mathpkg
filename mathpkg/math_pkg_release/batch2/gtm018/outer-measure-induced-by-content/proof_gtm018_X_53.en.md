---
role: proof
locale: en
of_concept: outer-measure-induced-by-content
source_book: gtm018
source_chapter: "X"
source_section: "53"
---

The proof verifies that $\mu^*(0) = 0$, monotonicity, and countable subadditivity. For countable subadditivity, given a sequence $\{E_i\}$ and $\epsilon > 0$, choose $U_i \in \mathbf{U}$ with $E_i \subset U_i$ and $\lambda_*(U_i) \leq \mu^*(E_i) + \epsilon/2^i$. Then $\mu^*(\bigcup E_i) \leq \lambda_*(\bigcup U_i) \leq \sum \lambda_*(U_i) \leq \sum \mu^*(E_i) + \epsilon$, and the result follows from the arbitrariness of $\epsilon$.
