---
role: proof
locale: en
of_concept: stickelberger-ideal-sum-decomposition
source_book: gtm059
source_chapter: "2"
source_section: "1"
---

Consider $N = N^e$. An element of $I$ can be written in the form

$$
\sum_{i=1}^{k-1} \binom{n}{i} \binom{n}{i-1} p^{i-1} = p\text{-integral}.
$$

The first term corresponds to $i = l$, and the second term is an integer. By the definition of the Stickelberger ideals, $J = I + \mathbb{Z}$ follows directly from the fact that the generators of $J$ differ from those of $I$ by integer constants.

For the second assertion, we use the $p$-adic expansion. Since $J = I + \mathbb{Z}$, we have $J + I = J$. Writing an element of $I$ as $p^{e-1}$ times an element of $J$ (after accounting for the $p$-adic valuations of the Bernoulli numbers involved), we obtain $(J+I)^e = J^e = p^{e-1} J^e$, where the exponent accounts for the power of $p$ appearing in the denominator of the Bernoulli polynomials evaluated at the appropriate level.
