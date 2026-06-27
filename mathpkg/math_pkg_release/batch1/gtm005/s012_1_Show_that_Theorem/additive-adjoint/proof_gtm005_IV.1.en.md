---
role: proof
locale: en
of_concept: additive-adjoint
source_book: gtm005
source_chapter: "IV"
source_section: "1"
---

Let $F: X \to A$ be left adjoint to an additive functor $G: A \to X$, with unit $\eta: I_X \to GF$. For any parallel pair $g, g': m \to n$ in $X$, we must show $F(g + g') = Fg + Fg'$.

Since $\eta$ is natural, $GF(g + g') \circ \eta_m = \eta_n \circ (g + g') = \eta_n g + \eta_n g'$. On the other hand, since $G$ is additive, $G(Fg + Fg') \circ \eta_m = (GFg + GFg') \circ \eta_m = GFg \circ \eta_m + GFg' \circ \eta_m = \eta_n g + \eta_n g'$. The equality of these two results gives $GF(g + g') \circ \eta_m = G(Fg + Fg') \circ \eta_m$.

By the universal property of the unit $\eta_m$ (it is a universal arrow from $m$ to $G$), there is a unique arrow $h: Fm \to Fn$ such that $Gh \circ \eta_m = \eta_n g + \eta_n g'$. But both $F(g + g')$ and $Fg + Fg'$ satisfy this equation. Hence $F(g + g') = Fg + Fg'$, proving $F$ is additive.

The dual statement for right adjoints follows by reversing all arrows and applying the same argument to the opposite categories.
