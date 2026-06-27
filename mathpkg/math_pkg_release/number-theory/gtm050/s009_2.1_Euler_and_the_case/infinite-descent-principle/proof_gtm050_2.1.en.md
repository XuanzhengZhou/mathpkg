---
role: proof
locale: en
of_concept: infinite-descent-principle
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

The principle of infinite descent is a consequence of the well-ordering of the positive integers. Suppose a Diophantine equation admits a solution in positive integers, and suppose that from any such solution one can construct another solution in strictly smaller positive integers. Then, starting from an initial solution, one obtains an infinite strictly decreasing sequence
$$a_1 > a_2 > a_3 > \cdots > 0$$
of positive integers. But the set of positive integers is well-ordered: every nonempty subset has a least element. The infinite decreasing sequence has no least element, which is impossible. Hence the original assumption that a solution exists must be false.

In Euler's proof, this principle is applied to the cubic equation $x^3 + y^3 = z^3$: the existence of a hypothetical solution $(x, y, z)$ yields a strictly smaller solution $(\alpha, \beta, \gamma)$ with $|\alpha\beta\gamma|^3 < z^3$. Iterating this construction produces an impossible infinite descent.
