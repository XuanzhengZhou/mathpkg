---
role: proof
locale: en
of_concept: hilberts-nullstellensatz
source_book: gtm021
source_chapter: "1"
source_section: "1.1"
---
The theorem reduces to the assertion: If $\mathcal{V}(I) = \emptyset$ then $I = K[T]$.

Given $f(T), f_1(T), \ldots, f_s(T)$, introduce a new indeterminate $T_0$ and consider $f_1(T), \ldots, f_s(T), 1 - T_0 f(T)$ in $K[T_0, T_1, \ldots, T_n]$. These have no common zero, so by the assertion they generate the unit ideal. Hence there exist $h_0, h_1, \ldots, h_s \in K[T_0, T_1, \ldots, T_n]$ such that
$$1 = \sum h_i f_i + h_0(1 - T_0 f(T)).$$
Substituting $T_0 = 1/f(T)$ and clearing denominators yields the desired relation $f(T)^r = \sum g_i(T) f_i(T)$.
