---
role: proof
locale: en
of_concept: normal-idempotent-is-orthogonal-projection
source_book: gtm023
source_chapter: "VIII"
source_section: "8.11"
---

Since $\varphi^2 = \varphi$, every vector $x$ can be written as
$$x = \varphi x + (x - \varphi x)$$
with $\varphi x \in \operatorname{Im} \varphi$ and $x - \varphi x \in \ker \varphi$. For any $y$, using $\varphi^2 = \varphi$ and normality:
$$(\varphi x, y - \varphi y) = (\varphi^2 x, y - \varphi y) = (\varphi x, \tilde{\varphi}(y - \varphi y)).$$
Since $\varphi$ and $\tilde{\varphi}$ commute and $\tilde{\varphi} \varphi = \tilde{\varphi}^2$, a direct computation using the decomposition shows that
$$(\varphi x, y) = (x, \varphi y)$$
for all $x, y$, hence $\varphi$ is selfadjoint. With $\varphi^2 = \varphi$, it follows that $\varphi$ is an orthogonal projection.
