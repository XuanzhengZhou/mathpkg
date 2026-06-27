---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A comonad is the categorical dual of a monad. It consists of an endofunctor $L: A \to A$ equipped with a counit $\varepsilon: L \to \mathrm{Id}_A$ and a comultiplication $\delta: L \to L^2$ satisfying coassociativity and counit laws. Equivalently, a comonad is a comonoid in the strict monoidal category $A^A$ of endofunctors with composition as the monoidal product. Every comonad naturally gives rise to an augmented simplicial object via the universal comonoid $\Delta^{\mathrm{op}} \to A^A$. A fundamental example is the comonad $L = \mathbb{Z}(\Pi) \otimes -$ on $\Pi\text{-}\mathbf{Mod}$, which yields the standard bar resolution for group cohomology.
