---
role: proof
locale: en
of_concept: iterated-exponential-lower-bound
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

We may assume $m \neq 0$ (the case $m = 0$ is trivial since $0 \leq 0$). We proceed by induction on $n$:

- Base $n = 0$: $a(m, 0) = m$, so $m \leq a(m, 0)$ holds with equality.

- Inductive step: Assume $m \leq a(m, n)$. Then

$$a(m, n + 1) = m^{a(m, n)} \geq m^m \geq m$$

since $m \geq 1$ (the case $m \neq 0$) implies $m^m \geq m$. Thus $m \leq a(m, n + 1)$. By induction, the inequality holds for all $n$.
