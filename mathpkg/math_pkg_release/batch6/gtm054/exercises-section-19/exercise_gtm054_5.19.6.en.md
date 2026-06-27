---
role: exercise
locale: en
chapter: "5"
section: "19"
exercise_number: 6
---

Prove that $(V, k_1, k_2)$ admits a feasible flow if and only if $k(U) \geq 0$ for all $U \subseteq V$. [Hint: construct a new doubly-capacitated network as follows. Let $x_0, y_0$ be two vertices not in $V$ and let $V' = V + \{x_0, y_0\}$. Let

$$k_1'(e) = \begin{cases} k_1(e) & \text{if } e \in W; \\ 0 & \text{otherwise;} \end{cases}$$

$$k_2'(e) = \begin{cases} k_2(e) & \text{if } e \in W; \\ \mu & \text{if } e = (y_0, x_0), (x_0, x), \text{or } (x, y_0) \text{ for } x \in V; \\ 0 & \text{otherwise;} \end{cases}$$

where $\mu$ is a

and

$$k_2(e) = \begin{cases} 
1 & \text{if } k_1(e) = 1; \\
|X| & \text{if } e = (x_0, x^1) \text{ or } (x^2, y_0) \text{ for some } x \in X; \\
|X| & \text{if } e = (y_0, x_0); \\
|X| & \text{if } e = (x^2, y^1) \text{ for } x, y \in X \text{ and } x < y; \\
0 & \text{otherwise.}
\end{cases}$$

(For example, let $X = \{x, y, z\}$ and suppose $x < y < z$. In Figure G8 the directed graph $(V, \sigma(k_2))$ is shown where the integer beside the edge $e$ represents $k_2(e)$.)
