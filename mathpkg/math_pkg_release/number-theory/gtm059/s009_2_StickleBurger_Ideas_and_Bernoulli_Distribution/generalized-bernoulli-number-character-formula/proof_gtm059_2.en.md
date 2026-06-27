---
role: proof
locale: en
of_concept: generalized-bernoulli-number-character-formula
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

Write the Bernoulli distribution as $dE_1 = dE_{1,c} + c^k \sigma_c dE_{1,c}$, or equivalently $dE_{1,c} = dE_1 - c^k dE_1(c^{-1}x)$. By the definition of the integral and the properties of the Bernoulli distribution, the integral of $\psi(x) x^{k-1}$ against $dE_{1,c}$ equals $(1 - \psi(c)c^k)$ times the integral against $dE_1$. Since $\psi$ is a character of conductor dividing a $p$-power, the integral against $dE_{1,c}$ converges $p$-adically and yields the generalized Bernoulli number. Rearranging gives the stated formula.

Specifically, from $E_{1,c}(x) = E_1(x) - c E_1(c^{-1}x)$ and the definition $B_{k,\psi} = k \int \psi(x) x^{k-1} dE_1(x)$, the change of variable $x \mapsto c^{-1}x$ under $\sigma_c$ gives the relation.
