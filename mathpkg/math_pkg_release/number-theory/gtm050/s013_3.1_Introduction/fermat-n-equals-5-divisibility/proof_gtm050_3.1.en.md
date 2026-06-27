---
role: proof
locale: en
of_concept: fermat-n-equals-5-divisibility
source_book: gtm050
source_chapter: "3"
source_section: "3.1"
---

Reformulate the statement in the more symmetrical form: if $x, y, z$ are integers such that $x^5 + y^5 + z^5 = 0$, then one of them must be divisible by $5$ (since $0$ is divisible by $5$).

The first step is to rewrite the equation as
$$-x^5 = (y + z)(y^4 - y^3z + y^2z^2 - yz^3 + z^4).$$

Assume $x, y, z$ are pairwise relatively prime (otherwise a common factor could be divided out). Then the two factors on the right are relatively prime, because if $p$ is any prime dividing $y + z$, then $y \equiv -z \pmod{p}$ and
$$y^4 - y^3z + y^2z^2 - yz^3 + z^4 \equiv 5y^4 \pmod{p}.$$
If $p$ divides both factors, then either $p = 5$ (in which case $x$ is divisible by $5$, as was to be shown), or $p$ divides $y$, contradicting relative primality.

Since the two factors are relatively prime $n$th powers, they must each be $5$th powers. Set
$$y + z = a^5, \quad y^4 - y^3z + y^2z^2 - yz^3 + z^4 = \alpha^5,$$
and similarly by symmetry obtain $b, \beta, c, \gamma$ for the other two variables.

Now suppose $x, y, z$ are pairwise relatively prime and prime to $5$. Then $a, \alpha, b, \beta, c, \gamma$ can be found as above. One of the numbers $x, y, z$ must be divisible by $11$. Assume without loss of generality that it is $x$. Then $2x = b^5 + c^5 + (-a)^5$ is divisible by $11$, and one of $a, b, c$ must be divisible by $11$. But $b$ cannot be divisible by $11$ because $x$ is divisible by $11$ and this would make $x$ and $z$ share the common factor $11$, contradicting relative primality. Similarly $c$ cannot be divisible by $11$. Thus $a$ must be divisible by $11$. But this too is impossible: then $y \equiv -z \pmod{11}$ gives $\alpha^5 \equiv 5y^4 \pmod{11}$, while $x \equiv 0$ gives $\gamma^5 \equiv y^4$, so $\alpha^5 \equiv 5 \cdot \gamma^5$. Since the fifth powers modulo $11$ are $0, \pm 1$, this implies $\alpha \equiv \gamma \equiv 0$, contradicting the assumption that $x$ and $z$ are relatively prime.

Thus the assumption that none of $x, y, z$ is divisible by $5$ leads to a contradiction, completing the proof.
