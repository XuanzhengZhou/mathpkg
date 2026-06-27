---
role: proof
locale: en
of_concept: factorization-via-a2-plus-3b2
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

Assume $p^2 + 3q^2$ is a cube, and $\gcd(p, q) = 1$. Euler's argument uses the identity
$$(a^2 + 3b^2)^3 = (a^3 - 9ab^2)^2 + 3(3a^2b - 3b^3)^2,$$
which shows that the set of numbers of the form $x^2 + 3y^2$ is closed under multiplication and cubing.

Assuming unique factorization in the ring $\mathbb{Z}[\sqrt{-3}]$ (the point where Euler's original proof was incomplete), one can deduce that if $p^2 + 3q^2$ is a cube, then there exist integers $a, b$ such that
$$p + q\sqrt{-3} = (a + b\sqrt{-3})^3.$$

Expanding $(a + b\sqrt{-3})^3$:
$$(a + b\sqrt{-3})^3 = a^3 + 3a^2b\sqrt{-3} + 3ab^2(-3) + b^3(-3)\sqrt{-3} = (a^3 - 9ab^2) + (3a^2b - 3b^3)\sqrt{-3}.$$

Equating real and imaginary parts:
$$p = a^3 - 9ab^2 = a(a^2 - 9b^2) = a(a - 3b)(a + 3b),$$
$$q = 3a^2b - 3b^3 = 3b(a^2 - b^2) = 3b(a - b)(a + b).$$

If $a$ and $b$ had a common factor $d$, then $d$ would divide both $p$ and $q$, contradicting $\gcd(p, q) = 1$. Hence $a$ and $b$ are coprime. The parity condition follows from the fact that if $a$ and $b$ had the same parity, then $p$ and $q$ would both be even.
