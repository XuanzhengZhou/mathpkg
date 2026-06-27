---
role: proof
locale: en
of_concept: ideal-sum-relatively-prime-characterization
source_book: gtm023
source_chapter: "12"
source_section: "4. The structure of factor algebras"
---

To prove the first part of the proposition we notice that

$$\Gamma(\bar{t}) = \sum_i I_i$$

is equivalent to

$$\Phi(1) = \sum_i I_i = \Phi\left(\bigvee_i f_i\right).$$

Since $\Phi$ is a lattice isomorphism, this is equivalent to $\bigvee_i f_i = 1$, i.e., the polynomials $f_i$ are relatively prime.

For the second part we observe that the sum is direct if and only if

$$I_j \cap \sum_{i \neq j} I_i = 0 \quad (j = 1, \ldots, m).$$

Since

$$I_j \cap \sum_{i \neq j} I_i = \Phi\left(f_j \wedge \left(\bigvee_{i \neq j} f_i\right)\right)$$

this is equivalent to

$$f_j \wedge \left(\bigvee_{i \neq j} f_i\right) = f \quad (j = 1, \ldots, m).$$
