---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $(X, \mathcal{A}, \mu)$ be any measure space and let $f$ be a nonnegative, real-valued, bounded, $\mathcal{A}$-measurable function on $X$. Let $\alpha = \inf\{f(x) : x \in X\}$ and $\beta = \sup\{f(x) : x \in X\}$. For $n \in N$ and $j = 1, 2, \ldots, n - 1$, let

$$A_j = \left\{x \in X : \alpha + \frac{(j - 1)(\beta - \alpha)}{n} \le f(x) < \alpha + \frac{j(\beta - \alpha)}{n}\right\}$$

and let

$$A_n = \left\{x \in X : \alpha + \frac{(n - 1)(\beta - \alpha)}{n} \le f(x) \le \beta\right\}.$$

The Lebesgue sums for $f$ are defined as the numbers

$$s_n = \sum_{j=1}^{n} \left(\alpha + \frac{(j - 1)(\beta - \alpha)}{n}\right) \mu(A_j).$$

Prove that $\lim_{n \to \infty} s_n = \int_X f d\mu$.

Next suppose that $\mu(X) < \infty$. Let $f$ be any bounded, real-valued, $\mathcal{A}$-measurable function on $X$. Define $s_n$ as above. Prove that $\lim_{n \to \infty} s_n = \int_X f d\mu$.
