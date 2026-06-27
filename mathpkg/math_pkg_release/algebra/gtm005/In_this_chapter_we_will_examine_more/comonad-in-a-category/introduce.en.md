---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A comonad is the formal dual of a monad, obtained by reversing the direction of every arrow in the definition. It consists of an endofunctor $L$ equipped with a counit $\varepsilon: L \to I_A$ and a comultiplication $\delta: L \to L^2$ satisfying coassociativity and counit laws. Just as every adjunction defines a monad on the domain category, it also defines a comonad $\langle FG, \varepsilon, F\eta G \rangle$ on the codomain category.
