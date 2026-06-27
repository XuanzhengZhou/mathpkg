---
role: proof
locale: en
of_concept: fractional-parts-dense
source_book: gtm041
source_chapter: "7"
source_section: "7.4"
---

First we note that $\{n\theta\} \neq \{m\theta\}$ for distinct integers $m$ and $n$.

Now choose the largest integer $N$ which satisfies $\{k\theta\} < 1/N$. Then we have

$$\frac{1}{N+1} < \{k\theta\} < \frac{1}{N}.$$

Therefore $\{mk\theta\} = m\{k\theta\}$ for $m = 1, 2, \ldots, N$, so the $N$ numbers

$$\{k\theta\}, \{2k\theta\}, \ldots, \{Nk\theta\}$$

form an increasing equally-spaced chain running from left to right in the interval $(0, 1)$. The last member of this chain (by the definition of $N$) satisfies the inequality

$$\frac{N}{N+1} < \{Nk\theta\} < 1,$$

or

$$1 - \frac{1}{N+1} < \{Nk\theta\} < 1.$$

Thus $\{Nk\theta\}$ differs from $1$ by less than $1/(N+1) < \{k\theta\} < \varepsilon$. Therefore the first $N$ members of the subsequence $\{nk\theta\}$ subdivide the unit interval into subintervals of length $\varepsilon$. Since $\alpha$ lies in one of these subintervals, the theorem is proved.
