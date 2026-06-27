---
role: exercise
locale: en
chapter: "4"
section: "4.8"
exercise_number: 1
---

# Exercise 4.8

Prove Lemma 4.8: $d^2 = 0$ for every $k$; that is, if $\omega^k \in \wedge^k(\Omega)$ for arbitrary $k$, then $d(d\omega^k) = 0$.

1. First verify the case $k = 0$: For $f \in C^\infty(\Omega)$, show that
   $$d(df) = \sum_{i<j} \left(\frac{\partial^2 f}{\partial x_i \partial x_j} - \frac{\partial^2 f}{\partial x_j \partial x_i}\right) dx_i \wedge dx_j = 0$$
   by equality of mixed partial derivatives.

2. Extend to general $k$: Write $\omega^k = \sum_{i_1 < \cdots < i_k} C_{i_1 \cdots i_k} dx_{i_1} \wedge \cdots \wedge dx_{i_k}$. Apply the definition of $d$ and the graded Leibniz rule
   $$d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^{\deg \alpha} \alpha \wedge d\beta$$
   to show that $d(d\omega^k) = 0$.

**Hint:** Use that $d(dC) = 0$ (from step 1) and $d(dx_j) = d^2(x_j) = 0$ for each coordinate function.
