---
role: exercise
locale: en
chapter: "1"
section: "1.4"
exercise_number: 18
---

A Kleisli algebra is a pair $(M, \mathbf{T})$ where $M$ is a monoid (qua one-object category) and $\mathbf{T}$ is an algebraic theory in $M$.

(a) Show that a Kleisli algebra is the same thing as a quintuple $(M, \cdot, e; \circ, \eta)$ where $(M, \cdot, e)$ and $(M, \circ, \eta)$ are monoids satisfying the law $(x \cdot \eta) \circ y = x \cdot y$ for all $x, y$. [Hint: clone form!]

(b) Show that $(M, +, 0; \circ, \eta)$ is a Kleisli algebra if $(M, +, 0)$ is an abelian monoid, $\eta + \eta = 0$ and $x \circ y = x + y + \eta$. In this case, show that $T$ is the identity functor and that $\mu = \eta$.
