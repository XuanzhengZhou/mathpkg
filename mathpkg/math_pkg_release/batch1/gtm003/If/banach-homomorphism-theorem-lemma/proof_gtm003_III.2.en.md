---
role: proof
locale: en
of_concept: banach-homomorphism-theorem-lemma
source_book: gtm003
source_chapter: "III"
source_section: "2"
---

Assume the hypotheses. Let $y \in S_\rho$ be given. Since $S_\rho \subset \overline{u(S_r)}$, we can select $x_1 \in S_r$ such that $|y - u(x_1)| \leq \rho_1$. Having chosen $x_1, \ldots, x_n$, select $x_{n+1}$ such that $|(y - \sum_{i=1}^n u(x_i)) - u(x_{n+1})| \leq \rho_n$, which is possible since the remainder lies in a sufficiently small ball contained in $\overline{u(S_{r/2^n})}$ by scaling. By choice of the sequence $\{\rho_n\}$, the series $\sum_i |x_i|$ converges (the terms are suitably bounded), so $\sum_i x_i$ converges to some $z \in L$ by completeness of $L$. Clearly $|z| \leq t$ for suitable $t$, and $u(z) = y$ follows from continuity of $u$ and the fact that $\{\rho_n\}$ is a null sequence.
