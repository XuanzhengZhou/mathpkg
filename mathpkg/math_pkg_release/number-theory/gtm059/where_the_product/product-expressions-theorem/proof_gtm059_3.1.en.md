---
role: proof
locale: en
of_concept: product-expressions-theorem
source_book: gtm059
source_chapter: "3"
source_section: "1"
---

The proof uses the functional equations of the Dedekind zeta function and Dirichlet $L$-functions. Under the transformation $s \mapsto 1 - s$, the completed zeta function $\zeta_K^*(s) = \zeta_K(s) \Gamma_{\mathbb{R}}(s)^{r_1} \Gamma_{\mathbb{C}}(s)^{r_2}$ with $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2} \Gamma(s/2)$ and $\Gamma_{\mathbb{C}}(s) = 2(2\pi)^{-s} \Gamma(s)$ satisfies the functional equation $\zeta_K^*(s) = |d_K|^{1/2 - s} \zeta_K^*(1-s)$. 

Similarly, for a primitive Dirichlet character $\chi$ modulo $f_\chi$ with Gauss sum $\tau(\chi)$, the completed $L$-function $L^*(s, \chi) = (f_\chi/\pi)^{s/2} \Gamma(s/2) L(s, \chi)$ (for even $\chi$) satisfies a functional equation with factor $\tau(\chi) / \sqrt{f_\chi}$.

Comparing the functional equation of $\zeta_K(s)$ with the product of functional equations of the $L(s, \chi)$ (via the decomposition $\zeta_K(s) = \prod_\chi L(s, \chi^*)$), one sees that under $s \mapsto 1 - s$, the ratio $\zeta_K(s) / \prod_\chi L(s, \chi)$ is invariant. The discrepancy in gamma factors and powers yields the conductor-discriminant relation $\prod_\chi f_\chi = |d_K|$ and the product formulas for Gauss sums. The case distinction between real and imaginary fields arises from the behavior of even versus odd characters under the functional equation.
