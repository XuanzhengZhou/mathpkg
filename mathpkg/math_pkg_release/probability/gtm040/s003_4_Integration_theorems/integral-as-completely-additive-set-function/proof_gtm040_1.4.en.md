---
role: proof
locale: en
of_concept: integral-as-completely-additive-set-function
source_book: gtm040
source_chapter: "1"
source_section: "4"
---
If we can prove the theorem for non-negative functions, we can write $f = f^+ - f^-$ and apply our result separately to $f^+$ and $f^-$. We therefore assume that $f$ is non-negative. We must show that if $E = \bigcup_{n=1}^{\infty} E_n$ disjointly, then $\rho(E) = \sum_{n=1}^{\infty} \rho(E_n)$. If $f$ is a characteristic function $\chi_A$, then $\rho(E) = \int_E \chi_A d\mu = \mu(A \cap E)$ and the complete additivity of $\rho$ follows from the complete additivity of $\mu$. For a simple function, the result follows from linearity and the characteristic function case. For general non-negative $f$, for every simple function $s$ with $0 \leq s \leq f$, we have $\int_E s \, d\mu = \sum_{n=1}^{\infty} \int_{E_n} s \, d\mu \leq \sum_{n=1}^{\infty} \rho(E_n)$, hence $\rho(E) \leq \sum_{n=1}^{\infty} \rho(E_n)$. For the reverse inequality, we use finite additivity on unions $E_1 \cup \cdots \cup E_n$ and take limits, using that the integral is defined as a supremum.
