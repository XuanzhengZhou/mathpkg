---
role: proof
locale: en
of_concept: prime-representation-as-a-squared-plus-3b-squared
source_book: gtm050
source_chapter: "2"
source_section: "2.6 Addendum on sums of two squares"
---

An exactly analogous procedure to the two-square case can be used to find a representation of a prime of the form $3n + 1$ in the form $a^2 + 3b^2$.

The first step is to compute $2^n \bmod p$. If $2^n$ is one greater than a multiple of $p$ then $p$ divides $2^n - 1$ and $3^n \bmod p$ must be computed. Eventually one must arrive at an integer $c$ such that $c^n$ is not $1$ greater than a multiple of $p$ but $(c-1)^n$ is.

Then, since $p$ divides

$$c^{3n} - (c-1)^{3n},$$

$p$ must divide

$$c^{2n} + c^n(c-1)^n + (c-1)^{2n}.$$

This provides the starting point for constructing a representation of a multiple of $p$ in the form $a^2 + 3b^2$, from which one can divide by successive factors to obtain a representation of $p$ itself, following the same reduction technique as in the two-square case.
