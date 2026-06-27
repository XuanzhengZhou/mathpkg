---
role: proof
locale: en
of_concept: "for-there-exists-such-that-if-is-archimedean"
source_book: gtm025
source_chapter: "Set Theory and Algebra"
source_section: "5.27"
---

Since $\alpha > \bar{0}$, there exists $(a_n) \in \alpha$ such that $a_n > 0$ for $n = 1, 2, 3, \ldots$ and $(a_n) \notin \mathfrak{N}$. Hence there is a $d \in P$ such that $a_s = |a_s| \geq d$ for arbitrarily large $s$. We have

$$|a_p - a_q| < \frac{1}{2} d$$

if $p, q \geq N\left(\frac{1}{2} d\right)$. Choose an $s$ as above such that $s \geq N\left(\frac{1}{2} d\right)$; then we have

$$d \leq a_s = a_s - a_p + a_p \leq |a_s - a_p| + |a_p| < \frac{1}{2} d + a_p;$$

i.e., $\frac{1}{2} d < a_p$ whenever $p \geq N\left(\frac{1}{2} d\right)$. It follows that $\left(a_n - \frac{1}{2} d_{(n)}\right) + \mathfrak{N} = \alpha - \frac{1}{2} d \geq \bar{0}$. We have

$$\alpha - \frac{1

Now fix $p \geq N(e)$. For $n \geq N(e)$ we have

$$a_p - a_n < e,$$
$$a_n - a_p < e.$$

It follows that

$$\bar{a}_p - \alpha \leq \bar{e} < \varepsilon,$$
$$\alpha - \bar{a}_p \leq \bar{e} < \varepsilon;$$

i.e.,

$$|\alpha - \bar{a}_p| < \varepsilon \text{ if } p \geq N(e).$$

We now state and prove our main result about $\bar{F}$.
