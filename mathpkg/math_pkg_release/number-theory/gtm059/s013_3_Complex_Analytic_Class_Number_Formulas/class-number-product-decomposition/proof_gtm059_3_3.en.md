---
role: proof
locale: en
of_concept: class-number-product-decomposition
source_book: gtm059
source_chapter: "3"
source_section: "Complex Analytic Class Number Formulas"
---

The proof uses the functional equation of the Dedekind zeta function and Dirichlet $L$-functions. Consider the functions obtained from $\zeta_K(s)$ and $L(s, \chi)$ under the substitution $s \mapsto 1-s$. For $K$ real, the combination

$$A(s) = \zeta_K(s) \cdot \prod_{\chi \neq 1} L(s, \chi)^{-1}$$

is invariant under $s \mapsto 1-s$. For $K$ imaginary, one separates even and odd characters. Under the transformation $s \mapsto 1-s$ and complex conjugation $\chi \mapsto \overline{\chi}$, functions of the form $L(s, \chi)$ for even $\chi$ pick up a factor involving Gauss sums:

$$\sqrt{\frac{f_\chi}{\pi}} \cdot \tau(\chi)$$

where $f_\chi$ is the conductor and $\tau(\chi)$ the Gauss sum. Dividing the functional equation of $\zeta_K$ by those of the $L$-series, one finds that under $s \mapsto 1-s$, the quotient

$$\frac{h R}{w \sqrt{|d|}} \cdot \frac{2^{r_1}(2\pi)^{r_2}}{\prod_{\chi \neq 1} L(1, \chi)}$$

transforms by a factor expressible in terms of the generalized Bernoulli numbers $B_{1,\chi}$. Evaluating at $s=1$ and using $L(1, \chi) = -\frac{\tau(\chi)}{f_\chi} B_{1,\overline{\chi}}$ for odd $\chi$ yields the stated product decomposition. The detailed derivation appears in [L], Chapter XII and [C], Chapter XII.
