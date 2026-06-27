---
role: exercise
locale: en
chapter: "IV"
section: "G"
exercise_number: 6
---

Prove that a doubly-capacitated network $(V, k_1, k_2)$ admits a feasible flow if and only if $k(U) \geq 0$ for all $U \subseteq V$, where
$$k(U) = \sum_{g_U(e)=1} k_2(e) \; - \!\! \sum_{g_U(e)=-1} k_1(e).$$

**Hint:** Construct a new doubly-capacitated network as follows. Let $x_0, y_0$ be two vertices not in $V$ and let $V' = V + \{x_0, y_0\}$. Define
$$k_1'(e) = \begin{cases} k_1(e) & \text{if } e \in W; \\ 0 & \text{otherwise;} \end{cases}$$
$$k_2'(e) = \begin{cases} k_2(e) & \text{if } e \in W; \\ \mu & \text{if } e = (y_0, x_0), (x_0, x), \text{or } (x, y_0) \text{ for } x \in V; \\ 0 & \text{otherwise;} \end{cases}$$
where $\mu$ is a sufficiently large integer. Then apply Theorem G3 to this augmented network.
