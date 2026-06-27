---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.2"
proof_technique: duality
locale: en
content_hash: ""
written_against: ""
---
Choose bases such that $f$ has a simple form. Let $r = \operatorname{rank} f$. By Corollary IV.2.14, there exist bases $X = \{u_1, \ldots, u_n\}$ of $E$ and $Y = \{v_1, \ldots, v_m\}$ of $F$ such that $f(u_i) = v_i$ for $i = 1, 2, \ldots, r$ and $f(u_i) = 0$ for $i = r+1, \ldots, n$. Extend to a basis $T = \{t_1, \ldots, t_m\}$ where $t_i = v_i$ for $i \le r$. Computing $\bar{f}$ on the dual basis $T^*$ shows $\bar{f}(t_i^*) = u_i^*$ for $i = 1, \ldots, r$ and $\bar{f}(t_i^*) = 0$ for $i = r+1, \ldots, m$. Thus $\operatorname{Im} \bar{f}$ is spanned by $\{u_1^*, \ldots, u_r^*\}$, which is linearly independent, so $\operatorname{rank} \bar{f} = r = \operatorname{rank} f$.
