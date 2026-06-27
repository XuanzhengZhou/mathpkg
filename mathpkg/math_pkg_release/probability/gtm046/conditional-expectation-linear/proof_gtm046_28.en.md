---
role: proof
locale: en
of_concept: conditional-expectation-linear
source_book: gtm046
source_chapter: "VIII"
source_section: "28"
---
These properties follow at once from the definition of conditional expectations and properties of integrals. The linearity of the ordinary integral implies, for every $B \in \mathfrak{B}$,
$$\int_B E^{\mathfrak{B}}(cX + c'X') \, dP = \int_B (cX + c'X') \, dP = c\int_B X \, dP + c'\int_B X' \, dP$$
$$= c\int_B E^{\mathfrak{B}}X \, dP + c'\int_B E^{\mathfrak{B}}X' \, dP = \int_B (cE^{\mathfrak{B}}X + c'E^{\mathfrak{B}}X') \, dP.$$
Since the indefinite integrals of the $\mathfrak{B}$-measurable functions coincide, the integrands are $P_{\mathfrak{B}}$-equivalent, giving the a.s. linearity. The special cases for $P^{\mathfrak{B}}$ follow by taking $X = I_\Omega$, $X = I_\emptyset$, and applying linearity to simple functions.
