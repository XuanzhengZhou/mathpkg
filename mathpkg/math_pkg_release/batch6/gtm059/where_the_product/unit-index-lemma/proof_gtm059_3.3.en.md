---
role: proof
locale: en
of_concept: unit-index-lemma
source_book: gtm059
source_chapter: "3"
source_section: "3"
---

The proof compares the analytic class number formulas for $K$ and $K^+$. For $K^+$ (totally real of degree $N/2$), the class number formula reads

$$\frac{2^{N/2} h^+ R^+}{2 \sqrt{|d^+|}} = \prod_{\chi \text{ even, } \chi \neq 1} L(1, \chi).$$

For $K$ (CM field of degree $N$), the formula gives

$$\frac{2^{N/2} (2\pi)^{N/2} h R}{w \sqrt{|d|}} = \prod_{\chi} L(1, \chi).$$

The product of $L$-values for $K$ factors as the product over even characters times the product over odd characters. The product over even characters (excluding the trivial character) appears in the formula for $K^+$. The ratio $\sqrt{|d|}/\sqrt{|d^+|}$ is related to the relative discriminant.

Computing the regulator of the units of $K^+$ with respect to $K$ involves the determinant of the logarithmic embedding. The local factors of the regulator determinant for $K$ differ from those for $K^+$ by the index $Q = (E : \mu_K E^+)$. Specifically, the regulator $R$ of $K$ satisfies $R = Q^{-1} \cdot 2^{N/2} \cdot R^+$ up to factors arising from the relative discriminant. Substituting into the class number formulas and comparing yields the stated relation for $h/h^+$.
