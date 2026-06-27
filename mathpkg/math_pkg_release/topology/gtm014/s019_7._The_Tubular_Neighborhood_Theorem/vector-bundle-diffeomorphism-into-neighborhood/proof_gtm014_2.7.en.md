---
role: proof
locale: en
of_concept: vector-bundle-diffeomorphism-into-neighborhood
source_book: gtm014
source_chapter: "2"
source_section: "7"
---

*Proof.* Choose a metric $t$ on $E$. The sets
$$B_x(a) = \{v \in E_x \mid t(x)(v, v) < a\}$$
form a neighborhood basis of $0$ in $E_x$ for $a \in \mathbf{R}^+$.

Since $V \cap E_x$ is an open neighborhood of $0$ in $E_x$, for each $x \in X$ there exists an $a > 0$ such that $B_x(a) \subset V \cap E_x$. Because $t$ is smooth, we may choose, by a partition of unity argument, a smooth function $\delta: X \to (0, 1)$ such that $B_x(\delta(x)) \subset V$ for all $x \in X$.

Define the mapping $h: E \to V$ by
$$h(v) = \frac{\delta(x) \, v}{\sqrt{1 + t(x)(v, v)}}$$
where $x = \pi(v)$. This mapping is well-defined since $\|h(v)\|^2 = \delta(x)^2 \cdot t(x)(v,v) / (1 + t(x)(v,v)) < \delta(x)^2 < \delta(x)$, so $h(v) \in B_x(\delta(x)) \subset V$.

The map $h$ is smooth, fibration-preserving ($\pi \circ h = \pi$ by construction), and its inverse on each fiber is given by
$$h^{-1}(w) = \frac{w}{\sqrt{\delta(x)^2 - t(x)(w, w)}}$$
which is smooth on the image. Hence $h$ is a diffeomorphism of $E$ into $V$. ∎
