---
role: proof
locale: en
of_concept: unit-index-lemma
source_book: gtm059
source_chapter: "3"
source_section: "Complex Analytic Class Number Formulas"
---

The proof follows by comparing the analytic class number formula for $K$ and its maximal real subfield $K^+$.

For $K$ (imaginary), we have $r_1 = 0$, $r_2 = N/2$, and:
$$\frac{(2\pi)^{r_2} h R}{w \sqrt{|d|}} = \prod_{\chi \neq 1} L(1, \chi)$$

Separating the product into even and odd characters:
$$\frac{(2\pi)^{r_2} h R}{w \sqrt{|d|}} = \prod_{\chi \text{ even, } \chi \neq 1} L(1, \chi) \cdot \prod_{\chi \text{ odd}} L(1, \chi)$$

For $K^+$ (real), we have $r_1 = N/2$, $r_2 = 0$, $w^+ = 2$, and:
$$\frac{2^{r_1} h^+ R^+}{w^+ \sqrt{|d^+|}} = \prod_{\chi \text{ even, } \chi \neq 1} L(1, \chi)$$

The even characters of $K$ correspond exactly to the non-trivial characters of $K^+$. Taking the ratio:
$$\frac{h R}{h^+ R^+} \cdot \frac{2^{r_1} w^+ \sqrt{|d^+|}}{w (2\pi)^{r_2} \sqrt{|d|}} = \prod_{\chi \text{ odd}} L(1, \chi)$$

The regulator $R$ can be expressed in terms of the logarithmic embedding. Comparing the regulators of $E$ and $W \cdot E^+$, one finds that $R/R^+ = Q \cdot (\text{local factor})$, which yields the index formula. The computation of the regulator index is done by examining the determinant expressing the regulator in $K$ and $K^+$, where the additional local factors of $2$ appear in each row of the determinant for $K$ relative to $K^+$. This gives $(E : W \cdot E^+) = 2^{n} h R / (h^+ R^+)$.
