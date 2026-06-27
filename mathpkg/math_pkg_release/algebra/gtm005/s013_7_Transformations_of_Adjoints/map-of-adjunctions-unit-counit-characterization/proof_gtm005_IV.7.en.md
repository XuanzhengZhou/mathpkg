---
role: proof
locale: en
of_concept: map-of-adjunctions-unit-counit-characterization
source_book: gtm005
source_chapter: "IV"
source_section: "7. Transformations of Adjoints"
---

Given the hom-set diagram (3) commutative, set $a = Fx$ and chase the identity arrow $1 : Fx 	o Fx$ around the diagram. Starting from the upper left corner:

$$1_{Fx} \in A(Fx, Fx)$$

Applying $K$ gives $K(1_{Fx}) = 1_{KFx} \in A'(KFx, KFx)$.

On the other path, first apply $arphi$ to get $\eta_x : x 	o GFx$ in $X(x, GFx)$, then apply $L$ to get $L\eta_x : Lx 	o LGFx$. But by the commuting square $LG = G'K$, we have $LGFx = G'KFx$. So this is $L\eta_x : Lx 	o G'KFx$.

Applying $arphi'^{-1}$ gives an arrow $F'Lx 	o KFx$. By the other commuting square $KF = F'L$, this is $F'Lx 	o KFx$.

The equality of these two paths yields the identity $L\eta_x = \eta'_{Lx}$, i.e., $L\eta = \eta'L$ as natural transformations.

Dually, setting $x = Ga$ and chasing the identity arrow $1_{Ga}$ from the lower right corner through the diagram yields $arepsilon'_K = Karepsilon$.
