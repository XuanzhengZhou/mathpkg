---
role: proof
locale: en
of_concept: galois-group-maximal-p-extension
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

By class field theory, the Artin reciprocity map gives an isomorphism

$$
\operatorname{Gal}(M/K) \cong \mathbf{J}_K / \overline{K^\times U_p}
$$

where $\mathbf{J}_K$ is the idele group of $K$ and $U_p = \prod_{\mathfrak{p} \nmid p} U_\mathfrak{p}$. The $p$-Hilbert class field $H$ corresponds to the subgroup $\overline{K^\times} \prod_{\mathfrak{p}} U_\mathfrak{p}$ (the product over all primes), so

$$
\operatorname{Gal}(M/H) \cong \frac{\overline{K^\times U_p}}{\overline{K^\times} \prod_{\mathfrak{p}} U_\mathfrak{p}} \cong \frac{U_p}{U_p \cap \overline{K^\times} \prod_{\mathfrak{p}} U_\mathfrak{p}}.
$$

By the Unit Group and Idele Lemma (Lemma above),

$$
U_p \cap \overline{K^\times} = \overline{E}.
$$

Thus $\operatorname{Gal}(M/H)$ is isomorphic (up to a finite kernel from the $p$-adic regulator) to $U_p / \overline{E} \prod_{\mathfrak{p}\mid p} U_\mathfrak{p}$. The group $U_p / \prod_{\mathfrak{p}\mid p} U_\mathfrak{p}$ is isomorphic to $\prod_{\mathfrak{p}\mid p} \mathcal{O}_{K_\mathfrak{p}}^\times$, which by the $p$-adic logarithm is isomorphic to an open subgroup of $\prod_{\mathfrak{p}\mid p} \mathcal{O}_{K_\mathfrak{p}} \cong \mathbb{Z}_p^{[K:\mathbb{Q}]}$.

The global units $E$ embed diagonally into this product via the regulator map. By Dirichlet's unit theorem, $E$ has $\mathbb{Z}$-rank $r_1 + r_2 - 1$, so the $\mathbb{Z}_p$-rank of $\overline{E}$ is at most $r_1 + r_2 - 1$. The quotient therefore has $\mathbb{Z}_p$-rank at least

$$
[K:\mathbb{Q}] - (r_1 + r_2 - 1) = (r_1 + 2r_2) - (r_1 + r_2 - 1) = r_2 + 1.
$$

This establishes the rank bound, and the Leopoldt conjecture asserts that the rank is exactly $r_2 + 1$, i.e., that the closure $\overline{E}$ has maximal possible rank $r_1 + r_2 - 1$.
