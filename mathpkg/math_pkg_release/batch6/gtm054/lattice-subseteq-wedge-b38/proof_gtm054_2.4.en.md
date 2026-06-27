---
role: proof
locale: en
of_concept: lattice-subseteq-wedge-b38
source_book: gtm054
source_chapter: "2"
source_section: "IIC"
---

By definition,
$$x \wedge y = \max\{z \in U : z \leq x; z \leq y\}
\geq \max\{z \in W : z \leq x; z \leq y\} \geq x \wedge y,$$
since $x \wedge y \in W$. The argument for $x \vee y$ is analogous.

When $(U, \leq)$ is a distributive lattice, we shall write $x_1 \oplus x_2 \oplus \dots \oplus x_m$ for $x_1 \vee x_2 \vee \dots \vee x_m$ if $x_i \wedge x_j = 0$ for $1 \leq i < j \leq m$. Clearly if $x \oplus y = 1$, then $x$ and $y$ are complements.
