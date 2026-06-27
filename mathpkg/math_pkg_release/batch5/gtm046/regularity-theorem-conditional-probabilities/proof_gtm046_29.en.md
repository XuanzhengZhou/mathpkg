---
role: proof
locale: en
of_concept: regularity-theorem-conditional-probabilities
source_book: gtm046
source_chapter: "VIII"
source_section: "29.1"
---
The proof proceeds by regularizing the conditional distribution function. Let $F^{\mathfrak{B}}(\omega, r) = P^{\mathfrak{B}}[X < r]$ be a version of the conditional distribution function. The countable union
$$N = N_0 \cup \bigcup_{r<r'} N_{rr'} \cup \bigcup_{r'} N_{r'}$$
of $P_{\mathfrak{B}}$-null sets is $P_{\mathfrak{B}}$-null. For every $x$, set
$$F^{\mathfrak{B}}(\omega, x) = \lim_{r \uparrow x} F^{\mathfrak{B}}(\omega, r), \quad \omega \notin N,$$
$$F^{\mathfrak{B}}(\omega, x) = F^{\mathfrak{B}}(\omega_0, x), \quad \omega \in N, \; \omega_0 \notin N.$$

For every $\omega \in \Omega$, the function so defined is a proper distribution function. By the correspondence theorem for distribution functions, the relation
$$Q^{\mathfrak{B}}(\omega, (-\infty, x)) = F^{\mathfrak{B}}(\omega, x)$$
determines a probability $Q^{\mathfrak{B}}(\omega, S)$ on Borel sets $S$. This $Q^{\mathfrak{B}}$ is $\mathfrak{B}$-measurable in $\omega$ and satisfies
$$Q^{\mathfrak{B}}(\omega, S) = P^{\mathfrak{B}}(\omega, [X \in S])$$
up to $P_{\mathfrak{B}}$-equivalence. The assertion holds first for intervals $(-\infty, r)$, then by the a.s. properties of conditional probabilities it extends to the field of finite unions of intervals, and by monotone passages to the limit it extends to the $\sigma$-field of all Borel sets.
