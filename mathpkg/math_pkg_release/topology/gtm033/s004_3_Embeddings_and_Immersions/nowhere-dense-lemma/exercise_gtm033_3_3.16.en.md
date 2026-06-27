---
role: exercise
locale: en
chapter: "3. Embeddings and Immersions"
section: "3"
exercise_number: 16
---

# Exercise 16

Embeddings of $P^n$ in $S^{n+k}$ can be constructed as follows (Hopf [1], James [1]). Let $h: \mathbb{R}^{n+1} \times \mathbb{R}^{n+1} \rightarrow \mathbb{R}^{n+1}$ be a symmetric bilinear map such that $h(x,y) \neq 0$ if $x \neq 0$ and $y \neq 0$. Define $g: S^n \rightarrow S^{n+k}$ by $g(x) = h(x,x)/|h(x,x)|$.

(a) $g(x) = g(y)$ if and only if $x = \pm y$. [Hint: consider $h(x + \lambda y, x - \lambda y)$ if $h(x,x) = \lambda^2 h(y,y)$.]

(b) $g$ induces an analytic embedding of $P^n$ into $S^{n+k}$.
