---
role: proof
locale: en
of_concept: algebraic-numbers-denumerable
source_book: gtm002
source_chapter: "2"
source_section: "2. Liouville Numbers"
---

Define the **weight** of a polynomial $f(x) = \sum_{i=0}^{n} a_i x^i$ with integer coefficients to be the number

$$w(f) = n + \sum_{i=0}^{n} |a_i|.$$

There are only finitely many polynomials having a given weight. Arrange these in some order, say lexicographically (first in order of $n$, then in order of $a_0$, and so on). Every non-constant polynomial has weight at least $2$. Taking the polynomials of weight $2$ in order, then those of weight $3$, and so on, we obtain a sequence $f_1, f_2, f_3, \ldots$ in which every polynomial of degree $1$ or more appears exactly once.

Each polynomial $f_k$ has at most a finite number of real zeros. Numbering the zeros of $f_1$, then the zeros of $f_2$, and so on (skipping any that have already appeared), we obtain an enumeration of all real algebraic numbers. Thus the set of real algebraic numbers is denumerable.
