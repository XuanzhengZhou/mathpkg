---
role: proof
locale: en
of_concept: projection-inequality-characterization
source_book: gtm036
source_chapter: ""
source_section: "I"
---

For any $y \in F$ and $t \in (0,1)$, convexity of $F$ gives $(1-t)P(x) + ty \in F$. By the minimizing property of $P(x)$:
$$\|x - P(x)\|^2 \leq \|x - (1-t)P(x) - ty\|^2 = \|(x - P(x)) - t(y - P(x))\|^2.$$

Expanding:
$$\|x - P(x)\|^2 \leq \|x - P(x)\|^2 - 2t \operatorname{Re}(x - P(x), y - P(x)) + t^2 \|y - P(x)\|^2.$$

Dividing by $t$ and letting $t \to 0^+$ yields $\operatorname{Re}(x - P(x), y - P(x)) \leq 0$.

For a cone $F$: taking $y = 0$ gives $\operatorname{Re}(x - P(x), -P(x)) \leq 0$, so $\operatorname{Re}(x - P(x), P(x)) \geq 0$. Taking $y = 2P(x) \in F$ (since $F$ is a cone) gives the reverse inequality. Hence $\operatorname{Re}(x - P(x), P(x)) = 0$. For any $y \in F$, $\operatorname{Re}(x - P(x), y) = \operatorname{Re}(x - P(x), y - P(x)) \leq 0$.

For a linear subspace $F$: replacing $y$ by $-y$ in the inequality gives both $\operatorname{Re}(x - P(x), y) \leq 0$ and $\operatorname{Re}(x - P(x), -y) \leq 0$, forcing $\operatorname{Re}(x - P(x), y) = 0$. For complex spaces, replacing $y$ by $iy$ yields $\operatorname{Im}(x - P(x), y) = 0$. Thus $(x - P(x), y) = 0$.
