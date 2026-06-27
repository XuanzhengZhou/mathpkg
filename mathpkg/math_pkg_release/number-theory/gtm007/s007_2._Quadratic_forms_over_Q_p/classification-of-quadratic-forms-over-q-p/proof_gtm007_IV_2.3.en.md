---
role: proof
locale: en
of_concept: classification-of-quadratic-forms-over-q-p
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.3"
---

That two equivalent forms have the same invariants follows directly from the definitions of $d(f)$ and $\varepsilon(f)$.

For the converse, we proceed by induction on the rank $n$ of the two forms $f$ and $g$ (the case $n = 0$ being trivial). Assume $f$ and $g$ have the same rank $n$, same discriminant $d$, and same invariant $\varepsilon$.

The corollary to Theorem 6 shows that $f$ and $g$ represent exactly the same elements of $k^*/k^{*2}$, since the representation criterion depends only on $n$, $d$, and $\varepsilon$. In particular, there exists $a \in k^*/k^{*2}$ that is represented by both $f$ and $g$.

By Witt's theorem, we can write:
$$f \sim a X_1^2 + f_1, \qquad g \sim a X_1^2 + g_1,$$
where $f_1$ and $g_1$ are forms of rank $n-1$. Computing their invariants:
$$d(f_1) = a d, \quad \varepsilon(f_1) = (a, d) \varepsilon,$$
and similarly for $g_1$. Thus $f_1$ and $g_1$ have the same invariants (rank $n-1$, discriminant $ad$, and invariant $(a, d)\varepsilon$). By the induction hypothesis, $f_1$ and $g_1$ are equivalent, and therefore $f$ and $g$ are equivalent.
