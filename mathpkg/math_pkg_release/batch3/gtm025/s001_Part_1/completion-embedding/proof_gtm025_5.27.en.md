---
role: proof
locale: en
of_concept: completion-embedding
source_book: gtm025
source_chapter: "5"
source_section: "5.27"
---

Since $\alpha > \bar{0}$, there exists $(a_n) \in \alpha$ such that $a_n > 0$ for all $n$ and $(a_n) \notin \mathfrak{N}$. Hence there is a $d \in P$ such that $a_s = |a_s| \geq d$ for arbitrarily large $s$. We have $|a_p - a_q| < \frac{1}{2}d$ if $p, q \geq N(\frac{1}{2}d)$. Choose $s \geq N(\frac{1}{2}d)$ with $a_s \geq d$; then for $p \geq N(\frac{1}{2}d)$,
$$d \leq a_s = a_s - a_p + a_p \leq |a_s - a_p| + |a_p| < \frac{1}{2}d + a_p,$$
so $\frac{1}{2}d < a_p$. It follows that $(a_n - \overline{\frac{1}{2}d}) + \mathfrak{N} = \alpha - \overline{\frac{1}{2}d} \geq \bar{0}$. Thus $\bar{0} < \overline{\frac{1}{2}d} < \alpha$, and we may take $e = \frac{1}{2}d$. The preservation of the Archimedean property follows similarly from the density of $F$ in $\bar{F}$.
