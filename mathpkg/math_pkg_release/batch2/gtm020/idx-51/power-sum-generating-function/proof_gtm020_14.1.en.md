---
role: proof
locale: en
of_concept: power-sum-generating-function
source_book: gtm020
source_chapter: "14"
source_section: "1"
---

We prove the result for the polynomial ring $R[\sigma_1, \ldots, \sigma_n] \subset R[x_1, \ldots, x_n]$ and then substitute $y_i$ for $\sigma_i$. Here $\sigma_i$ is the $i$-th elementary symmetric function in $x_1, \ldots, x_n$. For $f(t) = 1 + \sigma_1 t + \cdots + \sigma_n t^n$ we have

$$f(t) = (1 + x_1 t) \cdots (1 + x_n t).$$

Taking the logarithmic derivative:

$$-t\frac{(d/dt)f(t)}{f(t)} = -t\frac{d}{dt}\log f(t) = -t\sum_{i=1}^n \frac{x_i}{1 + x_i t}.$$

Expanding each term as a geometric series:

$$-t\frac{x_i}{1 + x_i t} = -t x_i \sum_{k \geq 0} (-x_i t)^k = \sum_{k \geq 1} x_i^k (-t)^k.$$

Summing over $i = 1, \ldots, n$:

$$-t\frac{(d/dt)f(t)}{f(t)} = \sum_{k \geq 1} (x_1^k + \cdots + x_n^k)(-t)^k = \sum_{k \geq 1} s_k^n(\sigma_1, \ldots, \sigma_n)(-t)^k.$$

Adding the $k = 0$ term $s_0^n = n$ yields the stated formula. This proves the proposition.
