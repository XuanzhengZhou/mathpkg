---
role: proof
locale: en
of_concept: iterated-exponential-strict-monotonicity
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

Since $m > 1$, we have $m^{k} > k$ for any $k \in \omega$ (because $m \geq 2$, and $2^k > k$ for all $k$). Therefore:

$$a(m, n + 1) = m^{a(m, n)} > a(m, n).$$

Thus $a(m, n) < a(m, n + 1)$ for all $n \in \omega$.
