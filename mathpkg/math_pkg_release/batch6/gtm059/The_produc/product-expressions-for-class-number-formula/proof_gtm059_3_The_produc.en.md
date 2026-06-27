---
role: proof
locale: en
of_concept: product-expressions-for-class-number-formula
source_book: gtm059
source_chapter: "3"
source_section: "Complex Analytic Class Number Formulas"
---

The proof proceeds by decomposing the $L$-series into its additive form and then applying the multiplicative product expansion. For the case $K = \mathbb{Q}(\zeta_m)$, one expresses the Dedekind zeta function as
$$\zeta_K(s) = \prod_{\chi} L(s, \chi)$$
where the product runs over all primitive Dirichlet characters $\chi$ modulo $m$. This follows from the decomposition of the prime ideals in $K$ and the factorization of the Euler product at each prime $p$.

For each prime $p$ not dividing $m$, let $p\mathcal{O}_K = \mathfrak{p}_1 \cdots \mathfrak{p}_g$ be the decomposition into prime ideals, with $N\mathfrak{p}_i = p^f$ where $f$ is the residue class degree. The Euler factor at $p$ for $\zeta_K(s)$ is
$$\prod_{i=1}^{g} \left(1 - \frac{1}{N\mathfrak{p}_i^s}\right)^{-1} = (1 - p^{-fs})^{-g}.$$

On the other hand, the product of $L$-series at $p$ yields
$$\prod_{\chi} \left(1 - \frac{\chi(p)}{p^s}\right)^{-1}$$
where the product runs over all characters. The identity of the Euler factors reduces to the orthogonality relations of characters: the values $\chi(p)$ for $\chi$ running over all characters correspond to the $f$-th roots of unity, each occurring with multiplicity $g$.

The product expressions (i)-(iii) then follow by comparing the functional equations. Under the transformation $s \mapsto 1-s$, the quotient $\zeta_K(s)/\zeta_{K^+}(s)$ transforms by the factor $\sqrt{|d_K/d_{K^+}|}$ multiplied by appropriate gamma factors. Separating the even and odd parts of this ratio, one obtains the stated expressions for the class number formula in the real and imaginary cases respectively.
