---
role: proof
locale: en
of_concept: kernel-equals-orthogonal-of-dual-image
source_book: gtm023
source_chapter: "II"
source_section: "2.26"
---

For any two vectors $x \in \ker \varphi$ and $y^* \in F^*$, we have

$$\langle \varphi^* y^*, x \rangle = \langle y^*, \varphi x \rangle = 0,$$

since $\varphi x = 0$. This shows that $x \in (\operatorname{Im} \varphi^*)^\perp$, hence $\ker \varphi \subset (\operatorname{Im} \varphi^*)^\perp$.

Conversely, if $x \in (\operatorname{Im} \varphi^*)^\perp$, then for every $y^* \in F^*$,

$$\langle \varphi^* y^*, x \rangle = \langle y^*, \varphi x \rangle = 0.$$

Since the scalar product is non-degenerate, this implies $\varphi x = 0$, i.e., $x \in \ker \varphi$. Thus $(\operatorname{Im} \varphi^*)^\perp \subset \ker \varphi$, and equality holds.
