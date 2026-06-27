---
role: proof
locale: en
of_concept: classification-of-quadratic-forms-over-qp
source_book: gtm007
source_chapter: "IV"
source_section: "§2. Quadratic forms over Q_p"
---

That equivalent forms have the same invariants follows from the definitions. For the converse, let $f$ and $g$ be two quadratic forms of rank $n$ with the same discriminant and $arepsilon$-invariant. We proceed by induction on $n$ (the case $n = 0$ being trivial).

By the corollary to Theorem 6, $f$ and $g$ represent exactly the same elements of $k^*/k^{*2}$. In particular, they both represent some common element $a \in k^*/k^{*2}$. Hence we can write
$$
f \sim a Z^2 + f_1, \quad g \sim a Z^2 + g_1
$$
where $f_1$ and $g_1$ have rank $n-1$. The discriminants satisfy
$$
d(f) = a \cdot d(f_1), \quad d(g) = a \cdot d(g_1)
$$
in $k^*/k^{*2}$, so $d(f_1) = d(g_1)$. Similarly, one computes
$$
arepsilon(f) = (a, d(f_1)) \cdot arepsilon(f_1), \quad arepsilon(g) = (a, d(g_1)) \cdot arepsilon(g_1),
$$
which gives $arepsilon(f_1) = arepsilon(g_1)$. By the induction hypothesis, $f_1 \sim g_1$, and therefore $f \sim g$.
