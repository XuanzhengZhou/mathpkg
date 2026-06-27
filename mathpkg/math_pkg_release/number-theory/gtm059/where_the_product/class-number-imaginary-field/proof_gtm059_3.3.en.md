---
role: proof
locale: en
of_concept: class-number-imaginary-field
source_book: gtm059
source_chapter: "3"
source_section: "3"
---

The proof proceeds by applying the analytic class number formula to both $K$ and its maximal real subfield $K^+$.

For the totally real field $K^+$ of degree $N/2$, the class number formula gives

$$\frac{2^{N/2} h^+ R^+}{2 \sqrt{|d^+|}} = \prod_{\chi \text{ even}, \chi \neq 1} L(1, \chi),$$

where the product runs over all non-trivial even primitive characters. For the CM field $K$, the class number formula reads

$$\frac{2^{N/2} (2\pi)^{N/2} h R}{w \sqrt{|d|}} = \prod_{\chi} L(1, \chi) = \prod_{\chi \text{ even}} L(1, \chi) \cdot \prod_{\chi \text{ odd}} L(1, \chi).$$

Taking the ratio of the two formulas, the even-character $L$-values cancel, and the discriminant factors combine via the conductor-discriminant formula $\prod_\chi f_\chi = |d_K|$. The factor involving the regulators satisfies $R / R^+ = 2^{N/2} / Q$, which follows from the definition of the unit index $Q = (E : \mu_K E^+)$ and the comparison of regulator determinants for $K$ and $K^+$.

Substituting these relations and simplifying yields the stated formula for $h/h^+$. The odd characters correspond precisely to the "minus" eigenspace under complex conjugation, giving the decomposition into first and second factors.
