---
role: proof
locale: en
of_concept: return-time-moments-reflecting-random-walk
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

The $r$-th moment of the return time $\bar{t}_0$ is by definition

$$M_0[\bar{t}_0^r] = \sum_{k=1}^{\infty} k^r \Pr_0[\bar{t}_0 = k].$$

From the return probability formula, the only possible return times are $1$ (with probability $q$) and $2n$ for $n \geq 1$ (with probability $\binom{2n-2}{n-1} \frac{1}{n} (pq)^n$). Substituting these into the moment sum:

$$M_0[\bar{t}_0^r] = 1^r \cdot q + \sum_{n=1}^{\infty} (2n)^r \cdot \binom{2n-2}{n-1} \frac{1}{n} (pq)^n.$$

This is the stated formula. The term $q$ comes from $k = 1$, and the infinite sum accounts for all even return times.
