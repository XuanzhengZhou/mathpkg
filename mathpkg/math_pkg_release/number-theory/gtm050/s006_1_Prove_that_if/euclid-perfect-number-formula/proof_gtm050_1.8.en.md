---
role: proof
locale: en
of_concept: euclid-perfect-number-formula
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---

(Euclid's direction) If $2^p - 1$ is prime, the proper divisors of $n = 2^{p-1}(2^p - 1)$ are:

$$1, 2, 4, \ldots, 2^{p-1}$$
and
$$(2^p - 1), 2(2^p - 1), 4(2^p - 1), \ldots, 2^{p-2}(2^p - 1).$$

The sum of the first sequence is $2^p - 1$. The sum of the second is $(2^{p-1} - 1)(2^p - 1)$. Adding: $(2^p - 1) + (2^{p-1} - 1)(2^p - 1) = 2^{p-1}(2^p - 1) = n$. Thus $n$ is perfect.

(Euler's converse) Let $n$ be an even perfect number. Write $n = 2^{k-1}m$ where $m$ is odd and $k \geq 2$. Since $n$ is perfect, $\sigma(n) = 2n$. By multiplicativity, $\sigma(n) = \sigma(2^{k-1})\sigma(m) = (2^k - 1)\sigma(m)$. Setting $(2^k - 1)\sigma(m) = 2^k m$, we have $\sigma(m) = m + \frac{m}{2^k - 1}$. Since $\sigma(m)$ and $m$ are integers, $m/(2^k - 1)$ must be an integer divisor of $m$. But the only proper divisor of $m$ that is this large is 1, so $m/(2^k - 1) = 1$, hence $m = 2^k - 1$ and $\sigma(m) = m + 1$. This means $m$ is prime, so $n = 2^{k-1}(2^k - 1)$ with $2^k - 1$ prime.
