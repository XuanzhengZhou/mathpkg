---
role: proof
locale: en
of_concept: orthogonal-set-summability-criterion
source_book: gtm036
source_chapter: ""
source_section: ""
---

By orthogonality, for any finite subset $C \subset A$:
$$\left\|\sum_{\alpha \in C} x_\alpha\right\|^2 = \sum_{\alpha \in C} \|x_\alpha\|^2.$$

If $\{x_\alpha\}$ is summable, then by the Cauchy criterion, for $e > 0$, there is a finite $B \subset A$ such that for finite $C \subset A \setminus B$, $\|\sum_{\alpha \in C} x_\alpha\|^2 = \sum_{\alpha \in C} \|x_\alpha\|^2 < e^2$, so $\{\|x_\alpha\|^2\}$ satisfies the Cauchy criterion for summability in $\mathbb{R}$.

Conversely, if $\{\|x_\alpha\|^2\}$ is summable, then for any $e > 0$, there exists finite $B \subset A$ such that for finite $C \subset A \setminus B$, $\sum_{\alpha \in C} \|x_\alpha\|^2 < e^2$. By orthogonality, $\|\sum_{\alpha \in C} x_\alpha\|^2 = \sum_{\alpha \in C} \|x_\alpha\|^2 < e^2$, so $\{x_\alpha\}$ satisfies the Cauchy criterion and is summable.

For the norm identity: let $x$ be the sum. For any finite $F \subset A$, $\|x\|^2 = \|x - \sum_{\alpha \in F} x_\alpha\|^2 + \|\sum_{\alpha \in F} x_\alpha\|^2$ (by orthogonality). Taking the limit over the net of finite subsets yields $\|x\|^2 = \sum \|x_\alpha\|^2$.
