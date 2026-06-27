---
role: proof
locale: en
of_concept: iterated-exponential-monotonicity-in-first-argument
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

We proceed by induction on $n$:

- Base $n = 0$: $a(m, 0) = m < m + 1 = a(m + 1, 0)$, which holds.

- Inductive step: Assume $a(m, n) < a(m + 1, n)$. Then

$$a(m, n + 1) = m^{a(m, n)} \leq (m + 1)^{a(m, n)}$$
$$< (m + 1)^{a(m + 1, n)} = a(m + 1, n + 1).$$

The first inequality uses $m \leq m + 1$ and monotonicity of exponentiation. The second strict inequality uses the induction hypothesis $a(m, n) < a(m + 1, n)$ together with the fact that $(m+1)^x$ is strictly increasing in $x$ (since $m+1 > 1$). By induction, the result holds for all $n$.
