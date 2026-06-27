---
role: proof
locale: en
of_concept: "chevalley-warning-theorem"
source_book: gtm007
source_chapter: "I"
source_section: "2.2"
---
Let $P = \prod_\alpha (1 - f_\alpha^{q-1})$. For $x \in \mathbb{F}_q^n$, if $x \in V$ then $f_\alpha(x) = 0$ for all $\alpha$, so $P(x) = 1$. If $x \notin V$, then some $f_\alpha(x) \neq 0$, so $f_\alpha(x)^{q-1} = 1$ and $P(x) = 0$. Thus $\operatorname{Card}(V) \equiv \sum_{x \in \mathbb{F}_q^n} P(x) \pmod{p}$.

Now $\deg P \leq (q-1) \sum_\alpha \deg f_\alpha < (q-1)n$, so $P$ is a sum of monomials $X_1^{u_1} \cdots X_n^{u_n}$ with $\sum u_i < (q-1)n$, hence at least one $u_i < q-1$. For such a monomial, $\sum_{x \in \mathbb{F}_q^n} x_1^{u_1} \cdots x_n^{u_n} = \prod_i (\sum_{x_i \in \mathbb{F}_q} x_i^{u_i}) = 0$ by the power sum lemma. Thus $\sum_{x} P(x) = 0$ in $\mathbb{F}_q$, so $\operatorname{Card}(V) \equiv 0 \pmod{p}$.

For the last assertion: if the $f_\alpha$ have no constant term, $0 \in V$, and $\operatorname{Card}(V) \equiv 0 \pmod{p}$ with $\operatorname{Card}(V) \geq 1$ implies $\operatorname{Card}(V) \geq p$, so a nontrivial zero exists.
