---
role: proof
locale: en
of_concept: adjoint-is-group-homomorphism
source_book: gtm021
source_chapter: "9"
source_section: "Lie Algebras and Tangent Spaces"
---
The invertibility of $\operatorname{Ad} x$ follows directly:
$$(\operatorname{Ad} x)(\operatorname{Ad} x^{-1}) = d(\operatorname{Int} x)_e \circ d(\operatorname{Int} x^{-1})_e = d(\operatorname{Int} x \circ \operatorname{Int} x^{-1})_e = d(\operatorname{Int} e)_e = \operatorname{id}_{\mathfrak{g}}.$$

Multiplicativity:
$$(\operatorname{Ad} x)(\operatorname{Ad} y) = d(\operatorname{Int} x)_e \circ d(\operatorname{Int} y)_e.$$
Since $\operatorname{Int}(xy) = \operatorname{Int} x \circ \operatorname{Int} y$, and by the chain rule for differentials,
$$d(\operatorname{Int} x \circ \operatorname{Int} y)_e = d(\operatorname{Int} x)_{(\operatorname{Int} y)(e)} \circ d(\operatorname{Int} y)_e = d(\operatorname{Int} x)_e \circ d(\operatorname{Int} y)_e,$$
since $(\operatorname{Int} y)(e) = y e y^{-1} = e$. Thus $\operatorname{Ad}(xy) = \operatorname{Ad} x \circ \operatorname{Ad} y$.
