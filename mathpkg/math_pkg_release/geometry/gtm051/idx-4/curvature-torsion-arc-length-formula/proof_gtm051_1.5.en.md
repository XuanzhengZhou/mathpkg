---
role: proof
locale: en
of_concept: curvature-torsion-arc-length-formula
source_book: gtm051
source_chapter: "1"
source_section: "1.5"
---
We know that $\dot{c}(t) = e_1(t)$, $e_2(t) = \ddot{c}(t)/|\ddot{c}(t)|$, and $e_3(t) = e_1(t) \times e_2(t) = \dot{c}(t) \times \ddot{c}(t)/|\ddot{c}(t)|$ (where $\times$ denotes the cross-product in $\mathbb{R}^3$). Thus $\kappa(t) = |\ddot{c}(t)|$, which implies $\ddot{c}(t) = \kappa(t) e_2(t)$. The Frenet equations imply

$$\dddot{c}(t) = \dot{\kappa}(t) e_2(t) + \kappa(t) \dot{e}_2(t) = \dot{\kappa}(t) e_2(t) + \kappa(t)(-\kappa(t) e_1(t) + \tau(t) e_3(t)).$$

Therefore

$$\det(\dot{c}(t), \ddot{c}(t), \dddot{c}(t)) = \det(e_1, \kappa e_2, -\kappa^2 e_1 + \dot{\kappa} e_2 + \kappa \tau e_3) = \kappa^2 \tau,$$

which gives $\tau(t) = \det(\dot{c}(t), \ddot{c}(t), \dddot{c}(t)) / \kappa^2(t)$.
