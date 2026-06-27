---
role: exercise
locale: en
chapter: "27"
section: "APPLICATIONS TO ANALYSIS"
exercise_number: 5
---

Following R. Bucy, prove the following strengthened form of T25.1: A set $B$ is transient if and only if there exists a function $u \geq 0$ on $B$ such that
$$\sum_{y \in B} G(x, y)u(y) = 1, \quad x \in B.$$

Hint: Suppose there is such a function $u$ and that $B$ is recurrent. Let $T_n$ be the time of the first visit to $B$ after time $n$. Then, for $x \in B$,
$$1 = E_x \sum_{k=0}^{\infty} u(x_k) = E_x \sum_{k=0}^{n} u(x_k) + E_x \sum_{k=T_n}^{\infty} u(x_k).$$
Now let $n \to \infty$ to arrive at the contradiction that $1 = 2$.
