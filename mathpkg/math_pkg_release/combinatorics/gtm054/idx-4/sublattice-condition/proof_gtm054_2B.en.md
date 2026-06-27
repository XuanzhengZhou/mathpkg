---
role: proof
locale: en
of_concept: sublattice-condition
source_book: gtm054
source_chapter: "II"
source_section: "B"
---

By definition,

$$x \wedge_U y = \max\{z \in U : z \leq x \text{ and } z \leq y\}$$
$$\geq \max\{z \in W : z \leq x \text{ and } z \leq y\} \geq x \wedge_W y,$$

since $x \wedge_W y \in W$. But $x \wedge_U y$ is also in $W$ by hypothesis, and is a lower bound of $\{x, y\}$ in $W$, so $x \wedge_U y \leq x \wedge_W y$. Hence $x \wedge_U y = x \wedge_W y$. The argument for $x \vee y$ is analogous.
