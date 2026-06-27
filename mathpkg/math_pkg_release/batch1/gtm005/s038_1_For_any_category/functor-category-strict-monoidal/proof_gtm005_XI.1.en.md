---
role: proof
locale: en
of_concept: functor-category-strict-monoidal
source_book: gtm005
source_chapter: "XI"
source_section: "1"
---

If $(M, \otimes, I)$ is a strict monoidal category, then the functor category $[C, M]$ (functors $C \to M$) is strict monoidal with pointwise tensor product:
$$(F \otimes G)(c) = F(c) \otimes G(c), \quad (\alpha \otimes \beta)_c = \alpha_c \otimes \beta_c,$$
and unit $\Delta_I$ (constant functor at $I$).

Since $M$ is strict, $\otimes$ is strictly associative and $I$ is a strict unit. Therefore:
$$((F \otimes G) \otimes H)(c) = (F(c) \otimes G(c)) \otimes H(c) = F(c) \otimes (G(c) \otimes H(c)) = (F \otimes (G \otimes H))(c),$$
and similarly $\Delta_I \otimes F = F = F \otimes \Delta_I$. No coherence isomorphisms are needed, making $[C, M]$ strict monoidal.
