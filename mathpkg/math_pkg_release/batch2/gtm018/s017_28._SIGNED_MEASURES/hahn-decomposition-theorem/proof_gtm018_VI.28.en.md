---
role: proof
locale: en
of_concept: hahn-decomposition-theorem
source_book: gtm018
source_chapter: "VI"
source_section: "28"
---
Since $\mu$ assumes at most one of the values $+\infty$ and $-\infty$, we may assume that $-\infty < \mu(E) \leq \infty$ for every measurable set $E$. Every countable union of negative sets is negative. Write $\beta = \inf \mu(B)$ for all measurable negative sets $B$. Let $\{B_i\}$ be a sequence of measurable negative sets with $\lim_i \mu(B_i) = \beta$; set $B = \bigcup_{i=1}^{\infty} B_i$. Then $B$ is a measurable negative set with minimal $\mu(B)$.

We prove $A = X - B$ is positive. Suppose $E_0 \subset A$ is measurable with $\mu(E_0) < 0$. $E_0$ cannot be negative (otherwise $B \cup E_0$ contradicts minimality). Let $k_1$ be the smallest positive integer such that $E_0$ contains a measurable $E_1$ with $\mu(E_1) \geq 1/k_1$. Since $\mu(E_0 - E_1) = \mu(E_0) - \mu(E_1) \leq \mu(E_0) - 1/k_1 < 0$, iterate: let $k_2$ be minimal with $E_2 \subset E_0 - E_1$, $\mu(E_2) \geq 1/k_2$. Inductively obtain disjoint $\{E_j\}$ with $\lim_n 1/k_n = 0$. Then $F_0 = E_0 - \bigcup_{j=1}^{\infty} E_j$ is a negative set disjoint from $B$ with $\mu(F_0) = \mu(E_0) - \sum_j \mu(E_j) \leq \mu(E_0) < 0$, contradicting minimality. Hence $A$ is positive.

For near-uniqueness: if $X = A_1 \cup B_1 = A_2 \cup B_2$ are two Hahn decompositions, then $E \cap (A_1 - A_2) \subset E \cap A_1$ gives $\mu(E \cap (A_1 - A_2)) \geq 0$, and $E \cap (A_1 - A_2) \subset E \cap B_2$ gives $\mu(E \cap (A_1 - A_2)) \leq 0$. Hence $\mu(E \cap (A_1 - A_2)) = 0$. By symmetry $\mu(E \cap (A_2 - A_1)) = 0$, so $\mu(E \cap A_1) = \mu(E \cap (A_1 \cup A_2)) = \mu(E \cap A_2)$.
