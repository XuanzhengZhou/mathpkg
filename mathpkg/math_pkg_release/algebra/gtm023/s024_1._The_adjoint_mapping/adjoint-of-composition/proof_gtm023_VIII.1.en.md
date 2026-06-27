---
role: proof
locale: en
of_concept: adjoint-of-composition
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

For any $x \in E$, $z \in G$, we compute using the defining relation of the adjoint twice:

$$((\psi \circ \varphi)x, z) = (\psi(\varphi x), z) = (\varphi x, \tilde{\psi} z) = (x, \tilde{\varphi}(\tilde{\psi} z)) = (x, (\tilde{\varphi} \circ \tilde{\psi})z).$$

On the other hand, by definition of the adjoint of $\psi \circ \varphi$:

$$((\psi \circ \varphi)x, z) = (x, \widetilde{\psi \circ \varphi} z).$$

Comparing the two expressions and using the nondegeneracy of the inner product yields $\widetilde{\psi \circ \varphi} = \tilde{\varphi} \circ \tilde{\psi}$.
