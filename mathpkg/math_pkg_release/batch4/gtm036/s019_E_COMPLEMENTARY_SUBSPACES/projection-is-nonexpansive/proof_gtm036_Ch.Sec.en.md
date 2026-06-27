---
role: proof
locale: en
of_concept: projection-is-nonexpansive
source_book: gtm036
source_chapter: ""
source_section: "I"
---

From the projection inequality, $\operatorname{Re}(x - Px, Py - Px) \leq 0$ and $\operatorname{Re}(y - Py, Px - Py) \leq 0$. Adding:
$$\operatorname{Re}(x - Px - y + Py, Py - Px) \leq 0.$$

Let $u = Px - Py$ and $v = x - y$. Then $x - Px - y + Py = v - u$, and the inequality becomes $\operatorname{Re}(v - u, -u) \leq 0$, or $\operatorname{Re}(v - u, u) \geq 0$, so $\operatorname{Re}(v, u) \geq \|u\|^2$.

Then $\|v\| \|u\| \geq \operatorname{Re}(v, u) \geq \|u\|^2$, whence $\|u\| \leq \|v\|$, i.e., $\|Px - Py\| \leq \|x - y\|$.
