---
role: proof
locale: en
of_concept: entrance-boundary-probability-measure
source_book: gtm040
source_chapter: "11"
source_section: "2"
---

**Proof of Proposition 11-2.** By Theorem 10-48, the $Q$-superregular vector $\bar{\nu}$ admits a representation
$$\bar{\nu} = \int_{S \cup B^e} J(x, \cdot) \, d\beta^\nu(x)$$
for a unique measure $\beta^\nu$ on the Borel sets of $S \cup B^e$. Here $J(x, \cdot)$ is the Martin entrance kernel and Theorem 10-48 guarantees that the representing measure is a probability measure when the superregular vector satisfies the appropriate normalization.

Since $\bar{\nu}_0 = \nu_0 + \delta_{00} = 0 + 1 = 1$, we have $\bar{\nu}_0 = 1$. Evaluating the integral representation at the $0$-coordinate yields
$$\bar{\nu}_0 = \int_{S \cup B^e} J(x, 0) \, d\beta^\nu(x) = 1,$$
which confirms that $\beta^\nu$ is indeed a probability measure.

For states $j \neq 0$, the Martin kernels are related by ${}_0N(x, j) = J(x, j)$ when $\bar{\nu}_0 = 1$ (after accounting for the normalization). Hence the representation for $\bar{\nu}_j = \nu_j + \delta_{0j}$ transfers to
$$\nu_j = \int_{S \cup B^e} {}_0N(x, j) \, d\beta^\nu(x)$$
for all $j$, yielding the stated integral representation of $\nu$.
