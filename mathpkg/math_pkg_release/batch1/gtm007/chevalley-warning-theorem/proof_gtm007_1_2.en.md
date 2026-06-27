---
role: proof
locale: en
of_concept: chevalley-warning-theorem
source_book: gtm007
source_chapter: "I"
source_section: "2"
---

Let $P = \prod_\alpha (1 - f_\alpha^{q-1})$. For $x \in K^n$, we have $P(x) = 1$ if $x \in V$ (since then $f_\alpha(x) = 0$), and $P(x) = 0$ if $x \notin V$ (since then some $f_\alpha(x) \neq 0$ and $f_\alpha(x)^{q-1} = 1$). Thus $\operatorname{Card}(V) \equiv \sum_{x \in K^n} P(x) \pmod{p}$.

Now $\deg P \leq (q-1) \sum_\alpha \deg f_\alpha < (q-1)n$. Expand $P$ as a linear combination of monomials $X_1^{u_1} \cdots X_n^{u_n}$ with $\sum u_i < (q-1)n$. Each monomial sum over $K^n$ factors: $\sum_{x \in K^n} X_1^{u_1} \cdots X_n^{u_n} = \prod_i (\sum_{x_i \in K} x_i^{u_i})$. By the power sum lemma, each factor $\sum_{x \in K} x^{u_i}$ is nonzero only when $u_i \geq 1$ and $(q-1) \mid u_i$. Since $\sum u_i < (q-1)n$, at least one $u_i$ is not a multiple of $q-1$, so the product vanishes. Hence $\sum_{x \in K^n} P(x) = 0$ in $K$, giving $\operatorname{Card}(V) \equiv 0 \pmod{p}$.
