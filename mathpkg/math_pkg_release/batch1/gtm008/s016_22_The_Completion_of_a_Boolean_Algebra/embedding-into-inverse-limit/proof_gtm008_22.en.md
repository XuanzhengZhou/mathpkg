---
role: proof
locale: en
of_concept: embedding-into-inverse-limit
source_book: gtm008
source_chapter: "22"
source_section: "22. The Completion of a Boolean Algebra"
---

Define $q$ by $(q(y))(\alpha) = q_{\alpha}(y)$. Obviously $q(y) \in X$ and $q_{\alpha} = p_{\alpha} \circ q$. Define $X_0 = \{q(y) \mid y \in Y\}$.

1. $X_0$ is dense in $X$: Let $x \in X$ and let $G$ be an open set with $x \in G$. Then there exist $\alpha < \kappa$ and $G_{\alpha}$ such that $G_{\alpha}$ is open in $X^{\alpha}$ and $x \in \tilde{G}_{\alpha} \subseteq G$. Take $y \in (q_{\alpha}^{-1})``G_{\alpha}$ and define $x_0 = q(y)$. Then $x_0 \in X_0$ and $x_0 \in G$, i.e., $G \cap X_0 \neq 0$.

2. $q: Y \rightarrow X_0$ is o.c.o.: Obvious.

3. If $Y$ satisfies the additional condition, then $q$ is one-to-one. An o.c.o. map is homeomorphic if it is one-to-one.
