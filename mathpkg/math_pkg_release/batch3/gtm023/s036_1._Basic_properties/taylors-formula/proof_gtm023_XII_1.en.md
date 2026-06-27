---
role: proof
locale: en
of_concept: taylors-formula
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

Since the relation is linear in $f$, it suffices to consider $f = t^n$. By the binomial formula:
$$f(a+b) = (a+b)^n = \sum_{p=0}^{n} \binom{n}{p} a^{n-p} \cdot b^p.$$
On the other hand, $f^{(p)}(t) = n(n-1)\cdots(n-p+1)t^{n-p}$, so
$$f^{(p)}(a) = n(n-1)\cdots(n-p+1)a^{n-p}.$$
Since $\binom{n}{p} = \frac{n(n-1)\cdots(n-p+1)}{p!}$, we have $\frac{f^{(p)}(a)}{p!} = \binom{n}{p}a^{n-p}$. Substituting gives the formula. The sum stops at $n = \deg f$ since $f^{(p)} = 0$ for $p > n$.
