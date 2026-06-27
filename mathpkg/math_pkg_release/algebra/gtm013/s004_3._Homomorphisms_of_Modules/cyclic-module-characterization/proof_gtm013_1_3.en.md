---
role: proof
locale: en
of_concept: cyclic-module-characterization
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** Given $x \in M$, the right multiplication map $\rho_x: R \to Rx$ defined by $\rho_x(r) = rx$ is a left $R$-homomorphism from ${}_R R$ onto the cyclic submodule $Rx$. Its kernel is precisely the left annihilator $l_R(x) = \{r \in R \mid rx = 0\}$. By the First Isomorphism Theorem (3.7.1),
$$R / l_R(x) \cong Rx.$$

Conversely, if $I$ is a left ideal of $R$, then $R/I$ is a cyclic left $R$-module spanned by the coset $1 + I$, and one readily checks that $l_R(1 + I) = I$.

Thus, a left $R$-module is cyclic if and only if it is isomorphic to $R/I$ for some left ideal $I$ of $R$. $\square$
