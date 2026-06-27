---
role: proof
locale: en
of_concept: chevalley-warning-theorem
source_book: gtm007
source_chapter: "I. Finite Fields"
source_section: "2. Equations over a finite field"
---

Let $|K| = q$ and let $p = \operatorname{char}(K)$. Consider the polynomial
$$P(X_1, \ldots, X_n) = \prod_{\alpha} (1 - f_\alpha(X_1, \ldots, X_n)^{q-1}).$$
For any $(x_1, \ldots, x_n) \in K^n$, if it is a common zero of all $f_\alpha$, then each factor equals $1$, so $P(x) = 1$. If some $f_\alpha(x) \neq 0$, then $f_\alpha(x)^{q-1} = 1$ (since $K^*$ has order $q-1$), so the corresponding factor is $0$, giving $P(x) = 0$. Thus $P$ is the characteristic function of $V$ on $K^n$.

Therefore,
$$\operatorname{Card}(V) \equiv \sum_{x \in K^n} P(x) \pmod{p},$$
where the sum is taken in $K$ (or in $\mathbb{Z}$ and then reduced modulo $p$; since $p = 0$ in $K$, this is equivalent).

Now expand $P$ as a linear combination of monomials $X_1^{u_1} \cdots X_n^{u_n}$. The total degree of $P$ is at most $(q-1) \sum_\alpha \deg f_\alpha < (q-1)n$. Hence in each monomial term, there exists some index $i$ with $u_i < q-1$.

The sum over $K^n$ of a monomial factors as
$$\sum_{x \in K^n} X_1^{u_1} \cdots X_n^{u_n} = \prod_{i=1}^n \left(\sum_{x_i \in K} x_i^{u_i}\right) = \prod_{i=1}^n S(X^{u_i}).$$
By the power sum lemma, $S(X^{u_i}) = 0$ whenever $0 \leq u_i < q-1$ (since $u_i \geq 1$ and not divisible by $q-1$, or $u_i = 0$ giving $S(X^0) = 0$). Thus each monomial sum vanishes, yielding $\sum_{x \in K^n} P(x) = 0$ in $K$.

Hence $\operatorname{Card}(V) \equiv 0 \pmod{p}$. For the second assertion: if each $f_\alpha$ has no constant term, then $(0, \ldots, 0)$ is a common zero, so $\operatorname{Card}(V) \geq 1$. Since $\operatorname{Card}(V)$ is a positive multiple of $p$, it must be at least $p \geq 2$, guaranteeing a nontrivial common zero.
