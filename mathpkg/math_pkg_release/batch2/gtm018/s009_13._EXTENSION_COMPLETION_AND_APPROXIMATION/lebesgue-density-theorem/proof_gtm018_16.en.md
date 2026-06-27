---
role: proof
locale: en
of_concept: lebesgue-density-theorem
source_book: gtm018
source_chapter: "III. Extension of Measures"
source_section: "§16. Non Measurable Sets"
---

By 15.C, $\bar{\mu}(E) = \inf\{\mu(U): E \subset U \in \mathbf{U}\}$, so find open $U_0 \supset E$ with $\alpha\mu(U_0) \leq \bar{\mu}(E)$. Decompose $U_0$ into disjoint open intervals $\{U_n\}$. Then $\alpha\sum\mu(U_n) \leq \sum\bar{\mu}(E \cap U_n)$, so $\alpha\mu(U_n) \leq \bar{\mu}(E \cap U_n)$ for some $n$.
