---
role: proof
locale: en
of_concept: constructive-decomposition-for-a-squared-plus-3b-squared
source_book: gtm050
source_chapter: "2"
source_section: "2.6 Addendum on sums of two squares"
---

The procedure is exactly analogous to the two-square case.

First compute $2^n \bmod p$. If $2^n$ is one greater than a multiple of $p$, then $p$ divides $2^n - 1$; in this case compute $3^n \bmod p$ next. Continue this process until one arrives at an integer $c$ such that $c^n$ is not $1$ greater than a multiple of $p$ but $(c-1)^n$ is.

At this point, since $p$ divides the difference

$$c^{3n} - (c-1)^{3n},$$

and since

$$x^3 - y^3 = (x-y)(x^2 + xy + y^2),$$

it follows that $p$ must divide

$$c^{2n} + c^n(c-1)^n + (c-1)^{2n}.$$

This congruence can be rewritten to give a relation of the form

$$u^2 + 3v^2 \equiv 0 \pmod{p},$$

which provides a representation of some multiple $kp$ as $a^2 + 3b^2$. The multiplier $k$ can then be reduced step by step using the identity

$$(x^2 + 3y^2)(u^2 + 3v^2) = (xu \mp 3yv)^2 + 3(xv \pm yu)^2,$$

until $k=1$ is reached, yielding the desired representation of $p$.
