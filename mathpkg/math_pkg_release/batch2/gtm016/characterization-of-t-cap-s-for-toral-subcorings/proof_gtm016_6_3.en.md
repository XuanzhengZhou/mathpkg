---
role: proof
locale: en
of_concept: characterization-of-t-cap-s-for-toral-subcorings
source_book: gtm016
source_chapter: "6"
source_section: "6.3"
---

One direction is easy. For the other, let $t \in T^0$ and suppose that $t(a) = \varepsilon(t)a$ for all $a \in K^S$. Let
$$\Delta t = \sum_{i=1}^{n} {}_i t \otimes t_i = t \otimes I + I \otimes t + \sum_{i=3}^{n} {}_i t \otimes t_i$$
where the ${}_i t, t_i$ are elements of $S^0 = S \cap \text{Kernel } \varepsilon$ for $3 \leq i \leq n$. For $a \in K^S$ and $b \in K$, we have
$$t(ab) = t(a)b + a t(b) + \sum_{i=3}^{n} {}_i t(a) t_i(b) = \varepsilon(t)ab + a t(b) + \sum_{i=3}^{n} \varepsilon({}_i t) a t_i(b)$$
$$= a\left(\sum_{i=3}^{n} \varepsilon({}_i t) t_i\right)(b) = a t(b),$$
so that $t \in T \cap H(K/K^S) = T \cap H(K/K^S)^S = T \cap \langle S \rangle$ (see 6.3.6). Since $t$ is semisimple, $t \in \langle S \rangle$ by 6.3.6.
