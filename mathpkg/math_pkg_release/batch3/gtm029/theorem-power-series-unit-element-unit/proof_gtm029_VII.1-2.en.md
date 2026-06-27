---
role: proof
locale: en
of_concept: theorem-power-series-unit-element-unit
source_book: gtm029
source_chapter: "VII"
source_section: "1-2"
---

If $fg = 1$, with $g = (g_0, g_1, \cdots, g_q, \cdots)$, then $f_0g_0 = 1$, and hence $f_0$ is a unit in $A$. Conversely, if $f_0$ is a unit in $A$, then we can find successively forms $g_0, g_1, \cdots, g_q, \cdots$, where $g_q$ is either zero or a form of degree $q$, such that $g_0f_0 = 1, g_1f_0 + g_0f_1 = 0, \cdots, g_qf_0 + g_{q-1}f_1 + \cdots + g_0f_q = 0, \cdots$. In fact, we have $g_0 = f_0^{-1}$. Assuming that $g_0, g_1, \cdots, g_{q-1}$ have already been determined and that each $g_i$ is either zero or a form of degree $i$ ($0 \leq i \leq q-1$), we set $g_q = -f_0^{-1}(g_{q-1}f_1 + \cdots + g_0f_q)$, and it is clear that $g_q$ is then either zero or a form of degree $q$. If we now set $g = (g_0, g_1, \cdots, g_q, \cdots)$ then we find, by (2), that $fg = 1$. This completes the proof.
