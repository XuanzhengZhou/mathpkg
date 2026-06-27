---
role: proof
locale: en
of_concept: iterated-exponential-addition-inequality
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

The section text is truncated and does not contain the full proof of Lemma 2.40. The statement asserts that for $m > 1$ and all $n, p \in \omega$:

$$a(m, n) + a(m, p) \leq a(m, \max(n, p) + 1).$$

The proof would proceed by noting that by Lemma 2.38 (strict monotonicity in the second argument), both $a(m, n) \leq a(m, \max(n, p))$ and $a(m, p) \leq a(m, \max(n, p))$. Then

$$a(m, n) + a(m, p) \leq 2 \cdot a(m, \max(n, p)).$$

Since $m > 1$, one can show that $2 \cdot a(m, k) \leq m^{a(m, k)} = a(m, k + 1)$ for any $k$, which yields the desired inequality with $k = \max(n, p)$.
