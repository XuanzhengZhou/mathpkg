---
role: proof
locale: en
of_concept: existence-uniqueness-of-projection
source_book: gtm036
source_chapter: ""
source_section: "I"
---

Let $d = \inf\{\|x - z\| : z \in F\}$. Choose a minimizing sequence $\{z_n\} \subset F$ with $\|x - z_n\| \to d$. By the parallelogram law:
$$\|z_n - z_m\|^2 = 2\|x - z_n\|^2 + 2\|x - z_m\|^2 - 4\|x - \frac{z_n + z_m}{2}\|^2.$$

Since $F$ is convex, $(z_n + z_m)/2 \in F$, so $\|x - (z_n + z_m)/2\| \geq d$. Therefore:
$$\|z_n - z_m\|^2 \leq 2\|x - z_n\|^2 + 2\|x - z_m\|^2 - 4d^2 \to 2d^2 + 2d^2 - 4d^2 = 0.$$

Thus $\{z_n\}$ is a Cauchy sequence. Since $H$ is complete and $F$ is closed, $z_n \to P(x) \in F$, and by continuity of the norm, $\|x - P(x)\| = d$.

For uniqueness: if $y_1, y_2 \in F$ both satisfy $\|x - y_1\| = \|x - y_2\| = d$, the same argument with $z_n = y_1, z_m = y_2$ gives $\|y_1 - y_2\|^2 \leq 2d^2 + 2d^2 - 4d^2 = 0$, so $y_1 = y_2$.
