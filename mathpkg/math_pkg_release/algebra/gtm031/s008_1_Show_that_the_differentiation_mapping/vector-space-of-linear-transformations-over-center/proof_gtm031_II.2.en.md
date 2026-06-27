---
role: proof
locale: en
of_concept: vector-space-of-linear-transformations-over-center
source_book: gtm031
source_chapter: "II"
source_section: "2"
---

For $\gamma \in \Phi$ and $A \in \mathfrak{L}(\mathfrak{R}_1, \mathfrak{R}_2)$, define $\gamma A = \gamma_l \circ A$, so $x(\gamma A) = \gamma(xA)$. The mapping $\gamma A$ is a linear transformation since both $\gamma_l$ and $A$ are linear and composition preserves linearity.

We verify the vector space axioms:
- $\gamma(A + B) = \gamma A + \gamma B$: $x(\gamma(A + B)) = \gamma\,x(A + B) = \gamma(xA + xB) = \gamma(xA) + \gamma(xB) = x(\gamma A) + x(\gamma B) = x(\gamma A + \gamma B)$.
- $(\gamma + \delta)A = \gamma A + \delta A$: $x((\gamma + \delta)A) = (\gamma + \delta)(xA) = \gamma(xA) + \delta(xA) = x(\gamma A + \delta A)$.
- $(\gamma\delta)A = \gamma(\delta A)$: clear from associativity of scalar multiplication in $\Delta$.
- $1_\Phi \cdot A = A$: $x(1_\Phi A) = 1_\Phi(xA) = xA$.

Thus $\mathfrak{L}(\mathfrak{R}_1, \mathfrak{R}_2)$ is a vector space over $\Phi$.
