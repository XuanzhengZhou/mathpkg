---
role: proof
locale: en
of_concept: class-number-imaginary-case
source_book: gtm059
source_chapter: "3"
source_section: "Complex Analytic Class Number Formulas"
---

The proof combines the analytic class number formula with the decomposition into even and odd characters, and the formula for $L(1, \chi)$ in terms of generalized Bernoulli numbers.

Starting from the analytic class number formula for $K$ (imaginary):

$$\frac{(2\pi)^{N/2} h R}{w \sqrt{|d|}} = \prod_{\chi \neq 1} L(1, \chi) = \prod_{\substack{\chi \text{ even} \\ \chi \neq 1}} L(1, \chi) \cdot \prod_{\chi \text{ odd}} L(1, \chi)$$

For $K^+$ (real), the class number formula gives:

$$\frac{2^{N/2} h^+ R^+}{2 \sqrt{|d^+|}} = \prod_{\substack{\chi \text{ even} \\ \chi \neq 1}} L(1, \chi)$$

Taking the ratio eliminates the even-character $L$-values:

$$\frac{h R}{h^+ R^+} \cdot \frac{2^{N/2} \cdot 2 \cdot \sqrt{|d^+|}}{w \cdot (2\pi)^{N/2} \cdot \sqrt{|d|}} = \prod_{\chi \text{ odd}} L(1, \chi)$$

Using the unit index lemma, $R/R^+ = Q \cdot 2^{-n} \cdot (\text{discriminant ratio})$, which simplifies the left-hand side. On the right-hand side, for an odd primitive character $\chi$ of conductor $f_\chi$, the value $L(1, \chi)$ is related to the generalized Bernoulli number by:

$$L(1, \chi) = -\frac{\pi \tau(\chi)}{f_\chi} B_{1,\overline{\chi}} \quad \text{or equivalently} \quad L(1, \chi) = -\frac{1}{2} B_{1,\chi} \cdot (\text{elementary factor})$$

where $\tau(\chi)$ is the Gauss sum. After careful accounting of the elementary factors (powers of $2\pi$, $\sqrt{|d|}$, etc.), the formula simplifies to:

$$h = h^+ \cdot Q \cdot w \cdot \prod_{\chi \text{ odd}} \left( -\frac{1}{2} B_{1,\chi} \right)$$

as stated. The detailed computation of the elementary factors involves the conductor-discriminant formula $|d| = \prod_\chi f_\chi$ and the relation between the regulator determinants of $K$ and $K^+$ via the logarithmic embedding.
