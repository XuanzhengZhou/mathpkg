---
role: proof
locale: en
of_concept: fermat-2n-plus-1-prime-power-of-2
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---

If $n$ is not a power of 2, write $n = km$ where $k > 1$ is odd. Then:

$$2^n + 1 = 2^{km} + 1 = (2^m)^k + 1.$$

Since $k$ is odd, $x^k + 1$ factors as $(x + 1)(x^{k-1} - x^{k-2} + \cdots - x + 1)$ with $x = 2^m$:

$$2^{km} + 1 = (2^m + 1)(2^{m(k-1)} - 2^{m(k-2)} + \cdots + 2^{2m} - 2^m + 1).$$

Both factors are integers greater than 1 (since $m \geq 1$ and $k > 1$). Therefore $2^n + 1$ is composite whenever $n$ has an odd factor greater than 1. Thus if $2^n + 1$ is prime, $n$ must be a power of 2. The converse is false: $n = 2^5 = 32$ is a power of 2 but $2^{32} + 1$ is divisible by 641 (Euler).
