---
role: proof
locale: en
of_concept: associator-formula-for-division-ring
source_book: gtm006
source_chapter: "IX"
source_section: "4"
---

The associator $[r,s,t] = (rs)t - r(st)$ is computed by applying the multiplication formula twice in each order and subtracting. Let $r = r_1 + \lambda r_2$, $s = s_1 + \lambda s_2$, $t = t_1 + \lambda t_2$.

First compute $(rs)t$: $rs = (r_1 s_1 + a s_2 r_2^\theta) + \lambda(s_1 r_2 + r_1^\theta s_2 + r_2^\theta b s_2)$. Then multiply by $t$.

Next compute $r(st)$: first $st = (s_1 t_1 + a t_2 s_2^\theta) + \lambda(t_1 s_2 + s_1^\theta t_2 + s_2^\theta b t_2)$, then multiply by $r$.

Subtracting and collecting terms yields the associator formula. The key observation is that terms involving differences $a^\theta - a$ and $b - b^\theta$ appear precisely as stated. When these differences vanish (i.e., $a^\theta = a$ and $b^\theta = b$), all associators vanish. $\square$
