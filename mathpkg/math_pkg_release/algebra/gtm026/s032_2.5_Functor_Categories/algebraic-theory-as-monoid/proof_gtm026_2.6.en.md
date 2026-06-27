---
role: proof
locale: en
of_concept: algebraic-theory-as-monoid
source_book: gtm026
source_chapter: "2"
source_section: "2.6"
---

By the definition in 2.3, a monoid in the strict monoidal category $(\mathcal{K}^\mathcal{K}, \mathrm{comp}, \mathrm{id}_\mathcal{K})$ consists of an object $T: \mathcal{K} \to \mathcal{K}$ (an endofunctor), a multiplication $\mu: TT \to T$ (a natural transformation), and a unit $\eta: \mathrm{id}_\mathcal{K} \to T$ (a natural transformation), satisfying the associativity and unit axioms:
$$
\mu \cdot (\mu \cdot \mathrm{id}_T) = \mu \cdot (\mathrm{id}_T \cdot \mu), \qquad
\mu \cdot (\eta \cdot \mathrm{id}_T) = \mathrm{id}_T = \mu \cdot (\mathrm{id}_T \cdot \eta).
$$
But these are precisely the axioms of an algebraic theory $(T, \eta, \mu)$ in monoid form as defined in 1.3.17. Since the monoids of any monoidal category themselves form a category (2.4), it follows that the algebraic theories in $\mathcal{K}$ form a category, namely the category of monoids in $(\mathcal{K}^\mathcal{K}, \mathrm{comp}, \mathrm{id}_\mathcal{K})$.
