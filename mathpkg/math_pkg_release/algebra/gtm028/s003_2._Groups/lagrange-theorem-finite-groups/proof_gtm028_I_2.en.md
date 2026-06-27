---
role: proof
locale: en
of_concept: lagrange-theorem-finite-groups
source_book: gtm028
source_chapter: "I"
source_section: "2. Groups"
---

Let $G$ be a finite group of order $n$ and $H$ a subgroup of order $m$. Consider the right cosets $Ha$ for $a \in G$. These cosets form a partition of $G$: every element $g \in G$ belongs to the coset $Hg$, and if two cosets $Ha$ and $Hb$ intersect, then $ha = h'b$ for some $h, h' \in H$, which implies $ab^{-1} = h^{-1}h' \in H$, hence $Ha = Hb$.

Moreover, each coset $Ha$ has exactly $m$ elements, since the map $h \mapsto ha$ is a bijection from $H$ onto $Ha$ (injective by the cancellation law, surjective by definition). If there are $k$ distinct cosets, then $n = k \cdot m$, so $m$ divides $n$. The quotient $k = n/m$ is called the index of $H$ in $G$.
