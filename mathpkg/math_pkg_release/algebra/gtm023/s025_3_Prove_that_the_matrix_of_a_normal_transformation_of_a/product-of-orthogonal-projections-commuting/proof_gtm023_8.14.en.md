---
role: proof
locale: en
of_concept: product-of-orthogonal-projections-commuting
source_book: gtm023
source_chapter: "VIII"
source_section: "8.14"
---

Assume first that $\pi_2 \circ \pi_1 = \pi_1 \circ \pi_2$. Then $(\pi_2 \pi_1)^2 = \pi_2 \pi_1 \pi_2 \pi_1 = \pi_2 \pi_2 \pi_1 \pi_1 = \pi_2 \pi_1$, since $\pi_1$ and $\pi_2$ commute and are idempotent. Moreover, $(\pi_2 \pi_1)^{\sim} = \tilde{\pi}_1 \tilde{\pi}_2 = \pi_1 \pi_2 = \pi_2 \pi_1$, using selfadjointness and commutativity. Hence $\pi_2 \pi_1$ is selfadjoint and idempotent, i.e., an orthogonal projection.

If $x \in E_1 \cap E_2$, then $\pi_1 x = x$ and $\pi_2 x = x$, so $\pi_2 \pi_1 x = x$, giving $E_1 \cap E_2 \subset \operatorname{Im}(\pi_2 \pi_1)$. Conversely, if $x = \pi_2 \pi_1 y$, then $x \in \operatorname{Im} \pi_2 = E_2$ and also $x = \pi_1(\pi_2 y) \in \operatorname{Im} \pi_1 = E_1$ (by commutativity), so $x \in E_1 \cap E_2$. Hence $\operatorname{Im}(\pi_2 \pi_1) = E_1 \cap E_2$.

Conversely, if $\pi_2 \pi_1$ is an orthogonal projection, then it is selfadjoint, so $\pi_2 \pi_1 = (\pi_2 \pi_1)^{\sim} = \pi_1 \pi_2$. Thus the projections commute.
