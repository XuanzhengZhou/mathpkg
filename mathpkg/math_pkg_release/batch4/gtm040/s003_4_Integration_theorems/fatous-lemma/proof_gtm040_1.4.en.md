---
role: proof
locale: en
of_concept: fatous-lemma
source_book: gtm040
source_chapter: "1"
source_section: "4"
---
Set $g_n(x) = \inf_{k \geq n} f_k(x)$. Then $0 \leq g_1 \leq g_2 \leq \cdots$, $g_n$ is measurable, $g_n \leq f_n$, and $\lim_n g_n = \liminf_n f_n$. By the Monotone Convergence Theorem,
$$\int_E \liminf_n f_n \, d\mu = \int_E \lim_n g_n \, d\mu = \lim_n \int_E g_n \, d\mu.$$
Since $\int_E g_n \, d\mu \leq \int_E f_n \, d\mu$, taking the limit inferior yields the result.
