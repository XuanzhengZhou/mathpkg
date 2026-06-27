---
role: proof
locale: en
of_concept: cardinality-bound-on-definable-sets
source_book: gtm053
source_chapter: "II"
source_section: "2"
---

If the language has $\leqslant \aleph_0$ variables, then there are at most
$$\operatorname{card}(\text{alphabet of } L) + \aleph_0$$
formulas, since formulas are finite sequences of symbols from the alphabet.

If, on the other hand, the language has an uncountable set of variables, then we note that every definable set can be defined by a formula whose variables belong to a fixed countable subset of the variables, chosen once and for all. This is because a formula, being a finite string, uses only finitely many variables. Thus, the number of definable sets is still bounded by the number of formulas using only the fixed countable variable set, which is at most $\operatorname{card}(\text{alphabet of } L) + \aleph_0$.
