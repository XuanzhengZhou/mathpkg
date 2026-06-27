---
role: proof
locale: en
of_concept: birkhoff-normal-form-theorem
source_book: gtm060
source_chapter: "Appendix 7"
source_section: "A"
---

The proof is carried out in a complex coordinate system
$$z_l = p_l + i q_l, \quad w_l = p_l - i q_l$$
(upon passing to this coordinate system we must multiply the Hamiltonian by $-2i$). If the terms of degree less than $N$ entering into the normal form are not already killed, then the transformation with generating function $Pq + S_N(P,q)$ (where $S_N$ is a homogeneous polynomial of degree $N$) changes only terms of degree $N$ and higher in the Taylor expansion of the Hamiltonian function.

Under this transformation, the coefficient for a monomial of degree $N$ in the Hamiltonian function having the form
$$z_1^{\alpha_1} \cdots z_n^{\alpha_n} w_1^{\beta_1} \cdots w_n^{\beta_n}$$
changes by a quantity proportional to
$$\sum_{l=1}^{n} \omega_l (\alpha_l - \beta_l).$$
This quantity is non-zero precisely when there is no resonance of order $N = |\alpha| + |\beta|$. By successively choosing $S_N$ for $N = 3, 4, \ldots, s$, all non-resonant terms of degree up to $s$ can be eliminated, leaving only those terms for which $\sum \omega_l(\alpha_l - \beta_l) = 0$, i.e., the resonant terms that constitute the Birkhoff normal form.
