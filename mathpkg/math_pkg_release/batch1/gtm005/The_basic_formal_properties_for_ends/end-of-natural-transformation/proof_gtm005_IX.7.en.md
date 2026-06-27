---
role: proof
locale: en
of_concept: end-of-natural-transformation
source_book: gtm005
source_chapter: "IX"
source_section: "7"
---

For each object $c \in C$, the composite

$$\int_c S(c,c) \xrightarrow{\omega_c} S(c,c) \xrightarrow{\gamma_{c,c}} S'(c,c)$$

defines an arrow from $\int_c S(c,c)$ to $S'(c,c)$. As $c$ varies, these composites constitute a wedge from the constant object $\int_c S(c,c)$ to the bifunctor $S'$, because for any morphism $f: c \to d$ in $C$, the naturality of $\gamma$ and the wedge property of $\omega$ imply that the relevant hexagon commutes.

Since $\langle \int_c S'(c,c), \omega' \rangle$ is the universal wedge over $S'$, there exists a unique arrow

$$g = \int_c \gamma_{c,c}: \int_c S(c,c) \to \int_c S'(c,c)$$

such that $\omega'_c \circ g = \gamma_{c,c} \circ \omega_c$ for all $c \in C$.

The functoriality rule $\int_c (\gamma' \circ \gamma)_{c,c} = (\int_c \gamma'_{c,c}) \circ (\int_c \gamma_{c,c})$ follows from the uniqueness part of the universal property: both sides are arrows $\int_c S(c,c) \to \int_c S''(c,c)$ making the requisite diagram commute with respect to the composite natural transformation $\gamma' \circ \gamma$, hence they must be equal.
