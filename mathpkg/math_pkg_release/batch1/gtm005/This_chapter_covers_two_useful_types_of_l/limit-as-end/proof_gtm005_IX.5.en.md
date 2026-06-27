---
role: proof
locale: en
of_concept: limit-as-end
source_book: gtm005
source_chapter: "IX"
source_section: "5"
---

For $T: C \to X$, define $S: C^{\mathrm{op}} \times C \to X$ by $S(a, b) = T(b)$ (dummy in the first variable). Then the end $\int_c S(c, c)$ is the limit of $T$:
$$\int_c T(c) \cong \varprojlim_{c \in C} T(c).$$

A dinatural wedge $\tau: x \xrightarrow{\bullet} S$ has components $\tau_c: x \to S(c, c) = T(c)$. Dinaturality: for $f: b \to c$, the hexagon reduces to $T(f) \circ \tau_b = \tau_c$ since $S$ is constant in the first argument. This is exactly the cone condition. Universality of the end-wedge corresponds to universality of the limit-cone, giving the isomorphism.
