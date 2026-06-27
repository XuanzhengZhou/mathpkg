---
role: exercise
locale: en
chapter: "6"
section: "6.3"
exercise_number: 1
---

# Exercise 1: Stable and Unstable Manifolds

Let $f: M \to \mathbb{R}$ be a $C^r$ Morse function, $2 \leqslant r \leqslant \omega$, and let $z \in M$ be a critical point. Choose a $C^\infty$ Riemannian metric on $M$ which, in a neighborhood of each critical point, is the standard Euclidean metric in Morse coordinates.

Let $\varphi_t$ denote the flow of the gradient vector field $-\operatorname{grad} f$. For $x \in M$, define the omega limit set $L_\omega(x)$ and alpha limit set $L_\alpha(x)$ in the usual way (the sets of limit points of $\varphi_t(x)$ as $t \to +\infty$ and $t \to -\infty$, respectively).

The **stable manifold** of $z$ (also called the *inset*) is

$$W_s(z) = \{ x \in M : L_\omega(x) = z \}$$

while the **unstable manifold** of $z$ (also called the *outset*) is

$$W_u(z) = \{ x \in M : L_\alpha(x) = z \}.$$

Prove the following:

**(a)** $W_s(z)$ and $W_u(z)$ are connected $C^r$ submanifolds, of dimensions $n - k$ and $k$ respectively, where $k = \operatorname{Ind}(z)$.

**(b)** $W_s(z)$ and $W_u(z)$ intersect transversely at $z$ and are otherwise disjoint.

***(c)** If $\partial M = \varnothing$ then $W_s(z) \approx \mathbb{R}^{n-k}$ and $W_u(z) \approx \mathbb{R}^k$.

****(d)** Actually, (a), (b) and (c) are true for any $C^\infty$ Riemannian metric on $M$.
