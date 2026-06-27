---
role: proof
locale: en
of_concept: end-of-natural-transformation
source_book: gtm005
source_chapter: "IX"
source_section: "7"
---

The composites $\gamma_{c,c} \circ \omega_c: \int_c S(c,c) \rightarrow S'(c,c)$ for each $c \in C$ define a wedge from the object $e = \int_c S(c,c)$ to the functor $S'$. Indeed, for any arrow $f: c \rightarrow d$ in $C$, the wedge condition for $\omega$ gives $S(1, f) \circ \omega_c = S(f, 1) \circ \omega_d$, and naturality of $\gamma$ yields $\gamma_{d,d} \circ S(1, f) = S'(1, f) \circ \gamma_{c,d}$ and $\gamma_{c,d} \circ S(f, 1) = S'(f, 1) \circ \gamma_{c,c}$. Combining these, the maps $\gamma_{c,c} \circ \omega_c$ satisfy the wedge condition for $S'$.

By the universal property of the end $\langle e', \omega' \rangle$ of $S'$, there exists a unique arrow $g: e \rightarrow e'$ such that $\omega'_c \circ g = \gamma_{c,c} \circ \omega_c$ for all $c \in C$. This $g$ is denoted $\int_c \gamma_{c,c}$ and is called the \textit{end of the natural transformation} $\gamma$.

For the composition rule, given $\gamma': S' \rightarrow S''$ with end $\langle e'', \omega'' \rangle$, the composite natural transformation $\gamma' \cdot \gamma: S \rightarrow S''$ yields, by the same construction, a unique arrow $\int_c (\gamma' \cdot \gamma)_{c,c}: e \rightarrow e''$. By the uniqueness part of the universal property, this arrow must equal $\left[ \int_c \gamma'_{c,c} \right] \circ \left[ \int_c \gamma_{c,c} \right]$, since both arrows make the requisite diagram commute with the wedge $\omega''$.
