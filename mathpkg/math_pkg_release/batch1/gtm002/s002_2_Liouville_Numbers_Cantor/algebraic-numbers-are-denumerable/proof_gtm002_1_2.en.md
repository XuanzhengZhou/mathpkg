---
role: proof
locale: en
of_concept: algebraic-numbers-are-denumerable
source_book: gtm002
source_chapter: "1"
source_section: "2"
---

**Proof of Theorem 2.1.** Let us define the weight of a polynomial $f(x) = \sum_{i=0}^n a_i x^i$ to be the number $n + \sum_{i=0}^n |a_i|$. There are only a finite number of polynomials having a given weight. Arrange these in some order, say lexicographically (first in order of $n$, then in order of $a_0$, and so on). Every non-constant polynomial has a weight at least equal to $2$. Taking the polynomials of weight $2$ in order, then those of weight $3$, and so on, we obtain a sequence $f_1, f_2, f_3, \ldots$ in which every polynomial of degree $1$ or more appears just once. Each polynomial has at most a finite number of real zeros. Number the zeros of $f_1$ in some order, then those of $f_2$, and so on, omitting any that have appeared previously. This enumerates all real algebraic numbers. Hence the set of real algebraic numbers is denumerable. $\square$

This gives perhaps the simplest proof of the existence of transcendental numbers. It should be noted that it is not an indirect proof; when all the choices are fixed in advance the construction used to prove Theorem 1.1 defines a specific transcendental number in $[0,1]$. It may be laborious to compute even a few terms of its decimal development, but in principle the number can be computed to any desired accuracy.
