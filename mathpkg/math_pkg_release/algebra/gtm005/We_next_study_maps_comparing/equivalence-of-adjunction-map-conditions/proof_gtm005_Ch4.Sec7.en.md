---
role: proof
locale: en
of_concept: equivalence-of-adjunction-map-conditions
source_book: gtm005
source_chapter: "IV"
source_section: "7"
---

Given the hom-set diagram (3) commutative, set $a = Fx$ and chase the identity arrow $1 : Fx \to Fx$ around (3) to obtain the units $\eta, \eta'$ and the equality $L\eta = \eta'L$.

Specifically, starting from $1_{Fx}$ in the upper-left corner $A(Fx, Fx)$:
- Applying $\varphi$ yields $\eta_x \in X(x, GFx)$.
- Applying $L$ yields $L\eta_x \in X'(Lx, LGFx)$.
- Going the other way: $K$ applied to $1_{Fx}$ gives $1_{KFx}$, which under the vertical equalities corresponds to $1_{F'Lx}$ in $A'(F'Lx, KFx)$. Then $\varphi'$ sends this to $\eta'_{Lx}$.

The commutativity of the diagram forces $L\eta_x = \eta'_{Lx}$ for all $x$, i.e., $L\eta = \eta'L$.

Conversely, the condition $\varepsilon'K = K\varepsilon$ is obtained by a dual argument. Set $x = Ga$ and chase the identity $1_{Ga}$ in the hom-set diagram, using the description of $\varphi$ and $\varphi'$ by the counit.
