---
role: proof
locale: en
of_concept: fatous-lemma
source_book: gtm055
source_chapter: "7"
source_section: "9"
---

Define $g_n(x) = \inf_{k \geq n} f_k(x)$. Then $\{g_n\}$ is a monotone increasing sequence of nonnegative measurable functions converging pointwise to $\liminf_n f_n$. By the Monotone Convergence Theorem,
$$\int_X (\liminf_n f_n) d\mu = \lim_n \int_X g_n d\mu.$$
Since $g_n \leq f_k$ for all $k \geq n$, we have $\int_X g_n d\mu \leq \inf_{k \geq n} \int_X f_k d\mu$. Taking limits as $n \to \infty$ yields
$$\int_X (\liminf_n f_n) d\mu \leq \liminf_n \int_X f_n d\mu.$$
The integrability of $\liminf_n f_n$ follows from the boundedness hypothesis.
