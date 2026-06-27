---
role: proof
locale: en
of_concept: germain-prime-divisibility
source_book: gtm050
source_chapter: "3"
source_section: "3.1"
---

The proof proceeds by exactly the same argument as the $n = 5$ case. Reformulate Fermat's Last Theorem for odd $n$ as: $x^n + y^n + z^n = 0$ is impossible in nonzero integers. The theorem to be proved becomes: if $x, y, z$ are integers with $x^n + y^n + z^n = 0$, then $n$ divides $xyz$.

Assume $x, y, z$ are pairwise relatively prime (otherwise divide out any common factor). Factor:
$$(-x)^n = y^n + z^n = (y + z)(y^{n-1} - y^{n-2}z + y^{n-3}z^2 - \cdots + z^{n-1}).$$

If a prime $q$ divides both $y + z$ and the second factor, then $y \equiv -z \pmod{q}$ implies
$$y^{n-1} - y^{n-2}z + \cdots + z^{n-1} \equiv n y^{n-1} \pmod{q}.$$
Since $q$ divides both factors, either $q = n$ (in which case $x$ is divisible by $n$, as desired) or $q$ divides $y$, contradicting pairwise relative primality.

Thus the factors are relatively prime $n$th powers, and one writes
$$y + z = a^n, \quad y^{n-1} - y^{n-2}z + \cdots + z^{n-1} = \alpha^n,$$
with analogous expressions $b, \beta, c, \gamma$ obtained by cyclic permutation.

Now suppose, for contradiction, that none of $x, y, z$ is divisible by $n$. Since $2n + 1 = p$ is prime, one can work modulo $p$. Because the multiplicative group modulo $p$ has order $2n$, the $n$th powers modulo $p$ are precisely $0, \pm 1$.

One of $x, y, z$ must be divisible by $p$. Without loss, suppose $p \mid x$. Then $2x = b^n + c^n + (-a)^n$ is divisible by $p$, so one of $a, b, c$ is divisible by $p$. By relative primality considerations (similar to the $n = 5$ case), the only possibility is $p \mid a$. However, this leads to $\alpha^n \equiv n \cdot \gamma^n \pmod{p}$, which is impossible because $n$th powers modulo $p$ are only $0, \pm 1$.

This contradiction shows that $n$ must divide at least one of $x, y, z$.
