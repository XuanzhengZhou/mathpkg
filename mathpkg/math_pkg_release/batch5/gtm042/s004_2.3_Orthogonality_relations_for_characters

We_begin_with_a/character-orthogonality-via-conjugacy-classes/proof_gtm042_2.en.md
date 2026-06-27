---
role: proof
locale: en
of_concept: character-orthogonality-via-conjugacy-classes
source_book: gtm042
source_chapter: "2"
source_section: "2.5"
---

Let $f_s$ be the class function equal to $1$ on the conjugacy class of $s$ and equal to $0$ elsewhere. Since $f_s$ is a class function, it can, by Theorem 6, be expanded in the orthonormal basis of irreducible characters:
$$f_s = \sum_{i=1}^{h} \lambda_i \chi_i,$$
where the Fourier coefficients are
$$\lambda_i = (f_s | \chi_i) = \frac{1}{g} \sum_{t \in G} f_s(t)\chi_i(t)^* = \frac{c(s)}{g} \chi_i(s)^*.$$

Thus, for each $t \in G$,
$$f_s(t) = \frac{c(s)}{g} \sum_{i=1}^{h} \chi_i(s)^* \chi_i(t).$$

If $t = s$, then $f_s(s) = 1$, giving (a):
$$1 = \frac{c(s)}{g} \sum_{i=1}^{h} \chi_i(s)^* \chi_i(s), \quad \text{so} \quad \sum_{i=1}^{h} \chi_i(s)^* \chi_i(s) = \frac{g}{c(s)}.$$

If $t$ is not conjugate to $s$, then $f_s(t) = 0$, giving (b):
$$0 = \frac{c(s)}{g} \sum_{i=1}^{h} \chi_i(s)^* \chi_i(t), \quad \text{so} \quad \sum_{i=1}^{h} \chi_i(s)^* \chi_i(t) = 0. \quad \square$$
