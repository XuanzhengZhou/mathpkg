---
role: proof
locale: en
of_concept: euler-even-perfect-number
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---

Let $n$ be an even perfect number. Write $n = 2^{k-1}m$ where $m$ is odd and $k \geq 2$. Since $n$ is perfect, $\sigma(n) = 2n$. By multiplicativity of $\sigma$ for coprime factors, $\sigma(n) = \sigma(2^{k-1})\sigma(m) = (2^k - 1)\sigma(m)$. Set $(2^k - 1)\sigma(m) = 2^k m$, so $\sigma(m) = m + \frac{m}{2^k - 1}$. Since $\sigma(m)$ and $m$ are integers, $m/(2^k-1)$ must be an integer divisor $d$ of $m$. Then $\sigma(m) = m + d$. But $\sigma(m)$ is at least $m + d + \text{(other divisors)}$ unless $d = 1$ and $m$ has no other proper divisors. Hence $m = 2^k - 1$ is prime and $n = 2^{k-1}(2^k - 1)$ is of Euclid's form.
