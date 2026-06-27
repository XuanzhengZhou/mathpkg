---
role: proof
locale: en
of_concept: class-number-formula-for-imaginary-field
source_book: gtm059
source_chapter: "3"
source_section: "Complex Analytic Class Number Formulas"
---

The proof applies the analytic class number formula to both $K$ and its maximal real subfield $K^+$. The Dedekind zeta functions are related by the product decomposition
$$\frac{\zeta_K(s)}{\zeta_{K^+}(s)} = \prod_{\chi \neq 1} L(s, \chi)$$
where the product runs over all non-trivial primitive Dirichlet characters $\chi$ associated to the abelian extension $K/\mathbb{Q}$. Evaluating the analytic class number formula,
$$\lim_{s \to 0} s^{r_1+r_2-1} \zeta_K(s) = -\frac{h_K R_K}{w_K}$$
and similarly for $K^+$ (where the pole order is $r_1 - 1$ since $K^+$ is totally real), one obtains
$$\frac{\lim_{s \to 0} \zeta_K(s)}{\lim_{s \to 0} \zeta_{K^+}(s)} = \frac{h R / w_K}{h^+ R^+ / w_{K^+}} \cdot \frac{2^{r_2}}{\sqrt{|d_K/d_{K^+}|}}.$$

On the other hand, the product of $L$-series at $s = 0$ separates into even and odd characters. The even characters contribute to the regulator factor, while the odd characters yield the product $\prod_{\chi \text{ odd}} L(0, \chi)$. Using the unit index formula from the Lemma,
$$(E : \mu_K \cdot E^+) = \frac{2^{r_2} h R^+}{h^+ R},$$
one can eliminate the regulator ratio $R/R^+$ in favor of the unit index $Q$. Substituting back yields the stated decomposition formula for $h$ in terms of $h^+$, $Q$, and the product of odd $L$-values.
