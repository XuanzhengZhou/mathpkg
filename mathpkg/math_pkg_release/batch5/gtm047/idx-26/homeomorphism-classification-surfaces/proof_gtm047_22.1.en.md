---
role: proof
locale: en
of_concept: homeomorphism-classification-surfaces
source_book: gtm047
source_chapter: "22"
source_section: "1"
---

$(1) \Rightarrow (2)$: If $M_1$ and $M_2$ are homeomorphic, then their Euler characteristics coincide: $\chi(M_1) = \chi(M_2)$. By Theorem 5, $\chi(M_i) = 2 - (2h_i + m_i)$. Hence $2h_1 + m_1 = 2h_2 + m_2$.

If $m_1, m_2 \in \{0, 2\}$, then $2h_1 + m_1$ and $2h_2 + m_2$ are both even, and parity considerations do not distinguish further. But orientability is a topological invariant: $M_1$ orientable $\iff m_1 = 0$ and $M_2$ orientable $\iff m_2 = 0$, so $m_1 = 0 \iff m_2 = 0$.

If $m_1 = m_2 = 0$, then $2h_1 = 2h_2$ implies $h_1 = h_2$. If $m_1 = m_2 = 2$, then $2h_1 + 2 = 2h_2 + 2$ implies $h_1 = h_2$. If $m_1 = m_2 = 1$, then $2h_1 + 1 = 2h_2 + 1$ implies $h_1 = h_2$.

The remaining case where one surface has $m=0$ and the other $m=2$ with $2h_1 = 2h_2 + 2$ is ruled out by the Betti number: for $m=0$, $p^1 = 2h_1$, while for $m=2$, $p^1 = 2h_2 + 1$. These cannot be equal since one is even and the other odd, contradicting homeomorphism.

Thus in all cases $h_1 = h_2$ and $m_1 = m_2$.

$(2) \Rightarrow (1)$: If $h_1 = h_2 = h$ and $m_1 = m_2 = m$, one constructs an explicit piecewise-linear homeomorphism between the two standard models by identifying corresponding handles and cross-caps. For suggestions, see the problems at the end of the section. $\square$
