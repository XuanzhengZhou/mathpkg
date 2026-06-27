---
role: proof
locale: en
of_concept: cosets-partition-group
source_book: gtm030
source_chapter: "2"
source_section: "13"
---

The congruence relation $x \equiv y \pmod{\mathfrak{H}}$ is an equivalence relation on $\mathfrak{G}$: it is reflexive since $x = x \cdot 1$ with $1 \in \mathfrak{H}$, symmetric since $y = xh$ implies $x = yh^{-1}$ with $h^{-1} \in \mathfrak{H}$, and transitive since $y = xh_1$ and $z = yh_2$ give $z = x(h_1h_2)$ with $h_1h_2 \in \mathfrak{H}$. The equivalence class of $x$ under this relation is precisely the right coset $x\mathfrak{H} = \{xh : h \in \mathfrak{H}\}$. Therefore, the right cosets form a partition of $\mathfrak{G}$: every element belongs to some coset (namely its own), and two cosets are either identical (if their representatives are congruent) or disjoint (if they are not).
