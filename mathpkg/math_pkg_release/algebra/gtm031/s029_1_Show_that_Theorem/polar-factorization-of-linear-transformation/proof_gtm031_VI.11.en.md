role: proof
locale: en
of_concept: polar-factorization-of-linear-transformation
source_book: gtm031
source_chapter: "VI"
source_section: "11"
---
This result follows from the polar factorization theorem in conjunction with the previous result that every unitary transformation can be expressed as $\exp(iH)$ with $H$ hermitian.

By the polar factorization theorem, any linear transformation $A$ can be written as $A = PU$ where $P$ is a positive semi-definite hermitian transformation and $U$ is unitary. (The transformation $P$ is uniquely determined as $\sqrt{AA^*}$, and when $A$ is non-singular, $U = P^{-1}A$.)

Applying the result $U = \exp(iH)$ established above to the unitary factor $U$, there exists a hermitian transformation $H$ such that $U = \exp(iH)$. Substituting this into the polar decomposition yields

$$A = P \exp(iH),$$

where $P$ is positive semi-definite hermitian and $H$ is hermitian. This factorization clearly generalizes the representation $\alpha = |\alpha| \exp(i\eta)$ of a complex number, with $P$ corresponding to the modulus $|\alpha|$ and $H$ corresponding to the argument $\eta$.
