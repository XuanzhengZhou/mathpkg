---
role: proof
locale: en
of_concept: convexity-fore-cone-past-cone
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

Assume that $z_1 \in T^+$ and $z_2 \in T^+$. By definition of the equivalence relation $\sim$,
$$(z_1, z_1) < 0, \quad (z_2, z_2) < 0, \quad \text{and} \quad (z_1, z_2) < 0.$$

For $0 \leq t \leq 1$, let $z(t) = (1 - t)z_1 + t z_2$. Then
\begin{align*}
(z(t), z(t)) &= ((1-t)z_1 + t z_2, (1-t)z_1 + t z_2) \\
&= (1-t)^2 (z_1, z_1) + 2t(1-t)(z_1, z_2) + t^2 (z_2, z_2).
\end{align*}

Each term is negative: $(1-t)^2(z_1, z_1) < 0$, $2t(1-t)(z_1, z_2) < 0$, and $t^2(z_2, z_2) < 0$. Hence $(z(t), z(t)) < 0$, so $z(t)$ is time-like. Moreover, for any $z_3 \in T^+$, the inner product $(z(t), z_3) = (1-t)(z_1, z_3) + t(z_2, z_3) < 0$, so $z(t) \in T^+$. Therefore $T^+$ is convex. The same argument applies to $T^-$.
