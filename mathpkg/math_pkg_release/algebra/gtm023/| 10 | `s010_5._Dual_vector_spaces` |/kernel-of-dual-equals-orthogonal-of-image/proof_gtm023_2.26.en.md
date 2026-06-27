---
role: proof
locale: en
of_concept: kernel-of-dual-equals-orthogonal-of-image
source_book: gtm023
source_chapter: "II"
source_section: "2.26"
---

For any two vectors $y^* \in \ker \varphi^*$ and $x \in E$, we have

$$\langle y^*, \varphi x \rangle = \langle \varphi^* y^*, x \rangle = 0,$$

since $\varphi^* y^* = 0$. This shows that $y^* \in (\operatorname{Im} \varphi)^\perp$, hence $\ker \varphi^* \subset (\operatorname{Im} \varphi)^\perp$.

Conversely, if $y^* \in (\operatorname{Im} \varphi)^\perp$, then for every $x \in E$,

$$\langle \varphi^* y^*, x \rangle = \langle y^*, \varphi x \rangle = 0.$$

Since this holds for all $x \in E$, it follows that $\varphi^* y^* = 0$, i.e., $y^* \in \ker \varphi^*$. Thus $(\operatorname{Im} \varphi)^\perp \subset \ker \varphi^*$, and equality holds.
