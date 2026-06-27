---
role: proof
locale: en
of_concept: binomial-coefficient-properties
source_book: gtm027
source_chapter: "7"
source_section: "Q"
---

# Proof of Binomial Coefficient Properties for Square Root Series

Let $a_n$ be the $n$-th binomial coefficient in the expansion of $(1 - t)^{1/2}$ about $t = 0$. Then:

$$(1 - t)^{1/2} = \sum_{n=0}^{\infty} a_n t^n, \qquad a_n = \binom{1/2}{n} (-1)^n.$$

We verify the stated properties:

1. **$a_0 = 1$.** Immediate from $(1 - 0)^{1/2} = 1$.

2. **$a_n < 0$ for $n > 0$.** For $n \geq 1$,
   $$\binom{1/2}{n} = \frac{\frac{1}{2}(\frac{1}{2} - 1) \cdots (\frac{1}{2} - n + 1)}{n!} = \frac{(\frac{1}{2})(-\frac{1}{2})(-\frac{3}{2})\cdots(\frac{3-2n}{2})}{n!}.$$
   The numerator has one positive factor ($1/2$) and $n-1$ negative factors, so the sign is $(-1)^{n-1}$. With $(-1)^n$, we get $a_n = \binom{1/2}{n}(-1)^n < 0$ for all $n \geq 1$.

3. **$\sum_{n=0}^\infty a_n = 0$.** Substitute $t = 1$ into $(1 - 1)^{1/2} = 0 = \sum a_n \cdot 1^n$. The series converges at $t = 1$ (alternatively, the partial sums are monotone decreasing and bounded below by $0$, so the limit exists and equals $(1 - 1)^{1/2} = 0$).

4. **Convolution identity.** The coefficients satisfy:
   $$\sum_{k=0}^p a_k a_{p-k} = \begin{cases} 1, & p = 0 \\ -1, & p = 1 \\ 0, & p > 1 \end{cases}$$
   This follows from squaring the power series:
   $$(1 - t) = \left(\sum_{n=0}^\infty a_n t^n\right)^2 = \sum_{p=0}^\infty \left(\sum_{k=0}^p a_k a_{p-k}\right) t^p.$$
   Since $(1 - t) = 1 - t + 0 \cdot t^2 + \cdots$, equating coefficients gives the stated values.

Alternatively, one may define $a_n$ recursively by the convolution identity and verify $a_n < 0$ for $n \geq 1$ by induction, observing that partial sums $\sum_{n < p} a_n t^n$ are monotonically decreasing in $p$ and bounded below by $(1 - t)^{1/2}$ for $0 \leq t < 1$, hence also for $t = 1$.
