---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The free group monad is the canonical example of a monad arising from an adjunction between a category of algebraic structures and the category of sets. The forgetful functor $G: \mathbf{Grp} \to \mathbf{Set}$ and the free group functor $F: \mathbf{Set} \to \mathbf{Grp}$ form an adjunction, and their composite $T = GF$ is a monad on $\mathbf{Set}$. The functor $T$ sends each set to the underlying set of the free group on that set (reduced words), the unit $\eta$ embeds generators as length-one words, and the multiplication $\mu$ reduces words of words by concatenation and cancellation. This example illustrates how monads capture the algebraic theory of groups purely within the category of sets.
