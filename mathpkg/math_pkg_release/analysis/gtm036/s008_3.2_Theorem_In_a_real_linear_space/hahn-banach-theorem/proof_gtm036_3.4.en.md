---
role: proof
locale: en
of_concept: hahn-banach-theorem
source_book: gtm036
source_chapter: "3"
source_section: "3.4"
---

Consider the linear space $E \times K$, where $K$ is the real field, and let $P$ be the set of all vectors $(x,t)$ which are "above" the graph of $p$; explicitly,
$$P = \{(x,t) : t \geq p(x)\}.$$
It is easy to see that $P$ is a cone and that $P$ is radial at $(0,1)$. For $(x,t)$ in $F \times K$ let
$$g(x,t) = t - f(x).$$
Then $g$ is a linear functional on $F \times K$. If $(x,t) \in P \cap (F \times K)$, then $t \geq p(x) \geq f(x)$, so $g(x,t) = t - f(x) \geq 0$. Hence $g$ is non-negative on $P \cap (F \times K)$. Applying the cone extension principle (Theorem 3.2) to $g$, there exists a linear functional $\overline{g}$ on $E \times K$ which extends $g$ and is non-negative on $P$. Define $\overline{f}$ on $E$ by $\overline{f}(x) = -\overline{g}(x,0)$. Since $\overline{g}(0,1) = g(0,1) = 1$, we have $\overline{g}(x, \overline{f}(x)) = \overline{g}(x,0) + \overline{f}(x) \cdot \overline{g}(0,1) = -\overline{f}(x) + \overline{f}(x) = 0$, so $(x, \overline{f}(x))$ belongs to the null space of $\overline{g}$. Because $\overline{g}$ is non-negative on $P$, we have $\overline{g}(x, p(x)) \geq 0$ for all $x$, which gives $p(x) \geq \overline{f}(x)$. Thus $\overline{f}$ is the required extension.
