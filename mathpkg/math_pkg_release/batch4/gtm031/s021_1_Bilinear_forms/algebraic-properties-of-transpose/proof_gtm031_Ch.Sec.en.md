---
role: proof
locale: en
of_concept: algebraic-properties-of-transpose
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

These properties follow from the previously established properties of the mapping $A \mapsto A^*$ between dual spaces.

(1) For additivity, since $A' = R_2 A^* R_1^{-1}$ and $A^*$ is additive, we have

$$(A + B)' = R_2 (A + B)^* R_1^{-1} = R_2 (A^* + B^*) R_1^{-1} = R_2 A^* R_1^{-1} + R_2 B^* R_1^{-1} = A' + B'.$$

(2) For multiplicativity when the spaces coincide, we use $(AB)^* = B^* A^*$ in the dual setting:

$$(AB)' = R (AB)^* R^{-1} = R (B^* A^*) R^{-1} = (R B^* R^{-1})(R A^* R^{-1}) = B' A'.$$

(3) If $A$ is invertible with inverse $A^{-1}$, then $I' = (A A^{-1})' = (A^{-1})' A'$, and similarly $I' = A' (A^{-1})'$. Since $I' = I$, it follows that $(A')^{-1} = (A^{-1})'$.
