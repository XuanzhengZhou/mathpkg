---
role: exercise
locale: en
chapter: "12"
section: "17"
exercise_number: 1
---

Let $[X, d]$ and $[Y, d']$ be compact metric spaces. Let $G_1, G_2, \ldots$ and $H_1, H_2, \ldots$ be sequences of finite open coverings of $X$ and $Y$ respectively, such that (1) for each $i$, $G_{i+1} \leqslant G_i$ and $H_{i+1} \leqslant H_i$ and (2)
$$\lim_{n \to \infty} \|G_n\| = \lim_{n \to \infty} \|H_n\| = 0.$$
Let $f_1, f_2, \ldots$ be a sequence of surjective functions $f_n: G_n \rightarrow H_n$, such that (3) if $g, g' \in G_n$, and $g$ intersects $g'$, then $f_n(g)$ intersects $f_n(g')$ and (4) if $g \in G_n, g' \in G_{n+1}$, and $g' \subset g$, then $f_{n+1}(g') \subset f_n(g)$. Then there is a surjective mapping $f: X \rightarrow Y$, such that if
$$V_i = \left[ f_i(\text{St} (G_i, P)) \right]^*,
\text{ then }
f(P) = \bigcap_{i=1}^{\infty} \bar{V}_i.$$
