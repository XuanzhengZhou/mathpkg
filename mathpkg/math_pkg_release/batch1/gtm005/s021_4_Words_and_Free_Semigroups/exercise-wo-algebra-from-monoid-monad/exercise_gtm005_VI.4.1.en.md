---
role: exercise
locale: en
chapter: "VI"
section: "4"
exercise_number: 1
---

Let $W_0$ be the monad in $\mathbf{Set}$ defined by the forgetful functor $\mathbf{Mon} \to \mathbf{Set}$ from monoids to sets. Show that a $W_0$-algebra is a set $M$ with a string $v_0, v_1, \ldots$ of $n$-ary operations $v_n : M^n \to M$, where $v_0 : * \to M$ is a constant (the identity element), $v_2$ is an associative binary operation, and for all $n \geq 1$,
$$v_{n+1} = v_n \circ (v_2 \times 1) : M^{n+1} \to M.$$

Conclude that the category of $W_0$-algebras is isomorphic to the category of monoids.
