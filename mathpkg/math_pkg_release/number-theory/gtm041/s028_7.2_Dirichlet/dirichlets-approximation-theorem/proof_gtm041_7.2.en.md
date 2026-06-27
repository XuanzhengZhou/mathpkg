---
role: proof
locale: en
of_concept: dirichlets-approximation-theorem
source_book: gtm041
source_chapter: "7"
source_section: "7.2"
---

Let $\{x\} = x - [x]$ denote the fractional part of $x$. Consider the $N + 1$ real numbers

$$0, \{\theta\}, \{2\theta\}, \ldots, \{N\theta\}.$$

All these numbers lie in the half-open unit interval $0 \leq \{m\theta\} < 1$. Now divide the unit interval into $N$ equal half-open subintervals of length $1/N$. Then some subinterval must contain at least two of these fractional parts, say $\{a\theta\}$ and $\{b\theta\}$, where $0 \leq a < b \leq N$. Hence we can write

$$|\{b\theta\} - \{a\theta\}| < \frac{1}{N}.$$

But

$$\{b\theta\} - \{a\theta\} = b\theta - [b\theta] - a\theta + [a\theta] = (b - a)\theta - ([b\theta] - [a\theta]).$$

Therefore if we let

$$k = b - a \quad \text{and} \quad h = [b\theta] - [a\theta]$$

the inequality becomes

$$|k\theta - h| < \frac{1}{N}, \quad \text{with} \quad 0 < k \leq N.$$

**Note.** Given $\varepsilon > 0$ we can choose $N > 1/\varepsilon$ and the theorem implies $|k\theta - h| < \varepsilon$.
