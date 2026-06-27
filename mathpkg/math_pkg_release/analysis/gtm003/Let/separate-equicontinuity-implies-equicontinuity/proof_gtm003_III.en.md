---
role: proof
locale: en
of_concept: separate-equicontinuity-implies-equicontinuity
source_book: gtm003
source_chapter: "III"
source_section: "5.1"
---

In view of the identity $f(x, y) - f(x_0, y_0) = f(x - x_0, y - y_0) + f(x - x_0, y_0) + f(x_0, y - y_0)$ and the separate equicontinuity of $B$, it suffices to prove equicontinuity at $(0, 0)$. Let $\{U_n\}$, $\{V_n\}$ be decreasing 0-neighborhood bases in $E, F$. For each $n$, set $W_n = \{x \in E: f(x, V_n) \subset W\}$ for a given 0-neighborhood $W$ in $G$. The separate equicontinuity implies $E = \bigcup_n W_n$. If $E$ is a Baire space, some $\overline{W}_n$ has interior, and a standard argument shows $f(U_n \times V_n) \subset W$ for large $n$, establishing equicontinuity.
