---
role: proof
locale: en
of_concept: continuity-of-u-operator
source_book: gtm059
source_chapter: ""
source_section: "5"
---

We estimate

$$\frac{1}{p} \sum_{\zeta} f(X + \zeta - 1) = \frac{1}{p} \sum_{\zeta} \sum_{n} a_n (X + \zeta - 1)^n.$$

Expanding $(X + \zeta - 1)^n$, the coefficient of $X^i$ is

$$\sum_{n} a_n \binom{n}{i} (\zeta - 1)^{n-i}.$$

Since $|\zeta - 1|_p = |p|^{1/(p-1)} < 1$ for any primitive $p$-th root of unity $\zeta$, and each coefficient is a rational integer combination of such terms, the coefficient of $X^i$ in the average is bounded by $\|f\|_p$. The projection property $U^2 = U$ follows from the fact that applying $U$ twice amounts to averaging over $p$-th roots of unity twice, which reduces to a single averaging because the set of $p$-th roots of unity is closed under multiplication.
