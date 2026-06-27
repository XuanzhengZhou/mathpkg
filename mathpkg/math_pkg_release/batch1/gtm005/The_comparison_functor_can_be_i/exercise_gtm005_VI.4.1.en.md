---
role: exercise
locale: en
chapter: "VI"
section: "4"
exercise_number: 1
---

Let $W_0$ be the monad in $\mathbf{Set}$ defined by the forgetful functor $\mathbf{Mon} \to \mathbf{Set}$. Show that a $W_0$-algebra is a set $M$ with a string $v_0, v_1, \ldots$ of $n$-ary operations $v_n$, where $v_0: * \to M$ is the unit element (picking out the identity of the monoid), $v_1 = 1_M$ is the identity on $M$, $v_2 : M \times M \to M$ is an associative binary operation, and for all $n \geq 2$, $v_{n+1} = v_n \circ (v_2 \times 1_M) : M^{n+1} \to M$. Conclude that a $W_0$-algebra is exactly a monoid.
