---
role: proof
locale: en
of_concept: regularity-theorem-conditional-probabilities
source_book: gtm046
source_chapter: "VIII"
source_section: "29.2"
---

**Proof.** The proof constructs a regular version of the conditional probability by regularizing the conditional distribution function.

First, select a version of the conditional distribution function $F^\mathfrak{B}(\omega, x) = P^\mathfrak{B}(\omega, [X < x])$ for rational $x$. The countable family of rational arguments ensures that almost-sure properties hold simultaneously outside a $P_\mathfrak{B}$-null set $N_0$.

For pairs of rationals $r < r'$, the monotonicity $F^\mathfrak{B}(\omega, r) \leq F^\mathfrak{B}(\omega, r')$ holds a.s. The countable union

$$N = N_0 \cup \bigcup_{r < r'} N_{rr'} \cup \bigcup_{r'} N_{r'}$$

of $P_\mathfrak{B}$-null sets is $P_\mathfrak{B}$-null. For every $\omega \notin N$, the function $r \mapsto F^\mathfrak{B}(\omega, r)$ on rationals is nondecreasing and bounded between 0 and 1. Define for every real $x$

$$F^\mathfrak{B}(\omega, x) = \lim_{r \uparrow x, r \in \mathbb{Q}} F^\mathfrak{B}(\omega, r), \quad \omega \notin N,$$

and set $F^\mathfrak{B}(\omega, x) = F^\mathfrak{B}(\omega_0, x)$ for $\omega \in N$ with some fixed $\omega_0 \notin N$. The resulting function is a proper distribution function in $x$ for every $\omega$, and by construction it is $\mathfrak{B}$-measurable in $\omega$.

By the correspondence theorem between distribution functions and probability measures on $\mathbb{R}$, the relation

$$Q^\mathfrak{B}(\omega, (-\infty, x)) = F^\mathfrak{B}(\omega, x)$$

determines a probability measure $Q^\mathfrak{B}(\omega, \cdot)$ on the Borel $\sigma$-field of $\mathbb{R}$. It remains to verify $Q^\mathfrak{B}(\omega, S) = P^\mathfrak{B}(\omega, [X \in S])$ up to $P_\mathfrak{B}$-equivalence. This holds for $S = (-\infty, r)$ by construction; by the almost-sure properties of conditional probabilities, it extends to the field of finite unions of intervals; by monotone passages to the limit, it extends to the $\sigma$-field of all Borel sets.

For countable families $X = (X_1, X_2, \ldots)$, the same construction applied to the finite-dimensional conditional distribution functions yields a regular conditional distribution. When the probability space is the sample space of $X$, the construction always works, yielding the existence of a regular conditional probability for any sub-$\sigma$-field $\mathfrak{B} \subset \alpha$.
