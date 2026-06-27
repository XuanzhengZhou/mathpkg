---
role: proof
locale: en
of_concept: toral-subcoring-containment-criterion
source_book: gtm016
source_chapter: "5"
source_section: "5.3"
---
One direction is easy. For the other, let $t \in T^0$ and suppose that $t(a) = \varepsilon(t)a$ for all $a \in K^S$. Let $\Delta t = \sum_{i=1}^{n} t_i \otimes t_i = t \otimes I + I \otimes t + \sum_{i=3}^{n} t_i \otimes t_i$ where the ${}_i t, t_i$ are elements of $S^0 = S \cap \operatorname{Kernel} \varepsilon$ for $3 \leq i \leq n$. For $a \in K^S$ and $b \in K$, we have $t(ab) = t(a)b + at(b) + \sum_i t_i(a)t_i(b) = \varepsilon(t)ab + at(b) + \sum_i \varepsilon({}_i t_i)a t_i(b) = a(\sum_i \varepsilon({}_i t_i)t_i)(b) = at(b)$, so that $t \in T \cap H(K/K^S) = T \cap H(K/K^S)^S = T \cap K^S\langle S \rangle$. Since $t$ is semisimple, $t \in \langle S \rangle$.
