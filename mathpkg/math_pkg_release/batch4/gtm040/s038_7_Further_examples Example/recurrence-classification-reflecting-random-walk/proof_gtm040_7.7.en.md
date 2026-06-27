---
role: proof
locale: en
of_concept: recurrence-classification-reflecting-random-walk
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

We know from earlier results that the reflecting random walk is recurrent if and only if $p \leq \frac{1}{2}$. It remains to distinguish null recurrence from positive recurrence and to verify transience.

The $r$-th moment of the return time $\bar{t}_0$ is

$$M_0[\bar{t}_0^r] = q + \sum_{n=1}^{\infty} (2n)^r \binom{2n-2}{n-1} \frac{1}{n} (pq)^n.$$

By Stirling's formula, the general term behaves asymptotically as

$$(2n)^r \binom{2n-2}{n-1} \frac{1}{n} (pq)^n \sim c \, (4pq)^n \cdot n^{r-3/2}.$$

**Case $p = \frac{1}{2}$:** Then $q = \frac{1}{2}$ and $4pq = 1$. The term behaves like $c \cdot n^{r-3/2}$. For $r = 0$ (the sum of probabilities), the series converges because $\sum n^{-3/2} < \infty$. This confirms the chain is recurrent. For $r = 1$ (the expected return time), the term behaves like $c \cdot n^{-1/2}$, and $\sum n^{-1/2}$ diverges. Hence $M_0[\bar{t}_0] = \infty$, so the chain is null recurrent.

**Case $p < \frac{1}{2}$:** Then $4pq < 1$. The factor $(4pq)^n$ decays exponentially, so the series converges for every $r \geq 0$. All moments $M_0[\bar{t}_0^r]$ are finite; in particular $M_0[\bar{t}_0] < \infty$, so the chain is positive recurrent.

**Case $p > \frac{1}{2}$:** From earlier results the chain is transient, so the return probability sum $\sum \Pr_0[\bar{t}_0 = k] < 1$.
