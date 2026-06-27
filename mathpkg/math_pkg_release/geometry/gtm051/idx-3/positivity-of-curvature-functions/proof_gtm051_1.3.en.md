---
role: proof
locale: en
of_concept: positivity-of-curvature-functions
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

The positivity of $\kappa_i$ for $i < n-1$ follows from the construction of the distinguished Frenet frame via the Gram-Schmidt process applied to the derivatives $\dot{c}(t), \ddot{c}(t), \dots, c^{(n)}(t)$. By condition (1.2.2), these derivatives are linearly independent at each $t$. The Gram-Schmidt orthonormalization ensures that $\dot{e}_i(t)$ has a nonzero component in the direction of $e_{i+1}(t)$, and by the definition of the distinguished frame this component is positive. Since $\kappa_i = \omega_{i,i+1}/|\dot{c}| = \dot{e}_i \cdot e_{i+1} / |\dot{c}|$, we have $\kappa_i > 0$ for $i < n-1$. The last curvature $\kappa_{n-1} = \dot{e}_{n-1} \cdot e_n / |\dot{c}|$ may be positive or negative since there is no constraint on the sign of the projection onto the final basis vector.
