---
role: proof
locale: en
of_concept: theorem-4-2-regulator-real-cyclic
source_book: gtm059
source_chapter: "13"
source_section: "The Mellin Transform and p-adic L-function"
---

The cyclotomic units are algebraic, and it is a known result that the $p$-adic logarithms of multiplicatively independent algebraic numbers are linearly independent over the algebraic numbers. The proof follows the same pattern as the corresponding result over the complex numbers (see Brouwer [16] or [17]). The factorization of the regulator into the product $\prod_{\chi \neq 1} L_p(1,\chi)$ follows from the determinant formula for the Frobenius determinant:
$$
R_p(\eta_1, \dots, \eta_r) = \det(\log_p \eta_i^{\sigma_j}) = \prod_{\chi \neq 1} \sum_{a=1}^{N} \chi^{-1}(a) \log_p(1 - \zeta_N^a),
$$
where the product is taken over all non-trivial characters of $\mathbb{Z}/N\mathbb{Z}^\times$. This expresses the regulator as a product of terms, each of which is identified with $L_p(1,\chi)$ by the characterization of the $p$-adic $L$-function via the Mellin transform.
