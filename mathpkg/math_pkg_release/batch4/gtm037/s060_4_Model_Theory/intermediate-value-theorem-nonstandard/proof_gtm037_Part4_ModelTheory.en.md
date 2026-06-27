---
role: proof
locale: en
of_concept: intermediate-value-theorem-nonstandard
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

Let $c = \inf \{x \in [a, b] : f(x) \geq 0\}$. Thus
\begin{align}
&\forall x (x < c \implies f(x) < 0), \\
&\forall x (c < x \implies \exists y (c \leq y < x \text{ and } f(y) \geq 0)).
\end{align}

Let $i$ be a positive infinitesimal. By $(1)$, $^*f(c - i) < 0$. By $(2)$, choose $y$ so that $c \leq y < c + i$ and $^*f(y) \geq 0$. Now $c - i \simeq c$ and $y \simeq c$. Since $f$ is continuous at $c$, the nonstandard characterization of continuity (Proposition 20.9) yields $^*f(c - i) \simeq f(c)$ and $^*f(y) \simeq f(c)$. Since $^*f(c - i) < 0$ and $^*f(y) \geq 0$, taking standard parts gives $f(c) \leq 0$ and $f(c) \geq 0$. Hence $f(c) = 0$.
