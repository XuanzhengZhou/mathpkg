---
role: proof
locale: en
of_concept: montgomery-masley-class-number-inequalities
source_book: gtm059
source_chapter: "3"
source_section: "7"
---

The proof refines the determinant method of Carlitz and Olson. Starting from Theorem 7.1, one has

$$h_p^+ = |\det D_p|$$

where $D_p$ is a matrix of size $r = \frac{p-3}{2}$ with entries bounded by $1$. Montgomery and Masley obtain a sharper estimate by analyzing the eigenvalues of $D_p$ or its associated group determinant. The Dedekind determinant factorization (Theorem 6.1) expresses $\det D_p$ as a product over even characters:

$$\det D_p = \prod_{\substack{\chi \text{ even} \\ \chi \neq 1}} \sum_{g \in S} \chi(g) \cdot (R(g) - R(-g)).$$

Each factor $\sum \chi(g) R(g) = \sum \chi(g)(R(g) - R(-g))/2$ can be related to Gauss sums, yielding an estimate of the form $|\sum \chi(g) R(g)| \approx \sqrt{p}$. The lower bound uses the fact that the factors are not too small, while the upper bound follows from a more careful application of Hadamard or from estimating each character sum individually. The proof is valid for $p \geq 200$, where the analytic estimates become uniform.
