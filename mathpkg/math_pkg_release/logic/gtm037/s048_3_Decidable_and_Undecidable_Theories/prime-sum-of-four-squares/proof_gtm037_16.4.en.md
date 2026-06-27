---
role: proof
locale: en
of_concept: prime-sum-of-four-squares
source_book: gtm037
source_chapter: "16"
source_section: "1"
---

The members of $\{x^2 : 0 \leq x \leq (p-1)/2\}$ are pairwise incongruent mod $p$, as are the members of $\{-1 - y^2 : 0 \leq y \leq (p-1)/2\}$. There are $p+1$ numbers in the union of these two sets, so there are $x$ and $y$ such that $0 \leq x, y \leq (p-1)/2$ and $x^2 \equiv -1 - y^2 \pmod{p}$. Say

$$x^2 + 1 + y^2 = mp.$$

Thus $1 \leq m$. Since $x, y \leq (p-1)/2$, we have

$$mp < \left(\frac{p}{2}\right)^2 + \left(\frac{p}{2}\right)^2 + 1 = \frac{p^2}{2} + 1 < p^2$$

for $p > 2$, hence $m < p$.
