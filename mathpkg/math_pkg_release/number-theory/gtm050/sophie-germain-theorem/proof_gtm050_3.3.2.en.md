---
role: proof
locale: en
of_concept: sophie-germain-theorem
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---
Reformulate FLT as $x^n + y^n + z^n = 0$ (by moving $z^n$ to the other side, since $n$ is odd). Assume $x, y, z$ are pairwise relatively prime and none is divisible by $n$.

From $(-x)^n = y^n + z^n = (y+z)(y^{n-1} - y^{n-2}z + \cdots + z^{n-1})$, the two factors on the right are relatively prime (if a prime $q$ divides both, then $y \equiv -z \pmod{q}$ and the second factor is $\equiv ny^{n-1} \pmod{q}$; since $n$ is prime to $x$, any common factor would divide $n$, and if $q = n$ then $x$ would be divisible by $n$, contradiction). Thus both are $n$-th powers: $y+z = a^n$ and $y^{n-1} - y^{n-2}z + \cdots + z^{n-1} = \alpha^n$.

By symmetry, $x+y = b^n$, $z+x = c^n$ with corresponding $\beta^n, \gamma^n$. From these: $2x = b^n + c^n - a^n$.

Now let $p$ be the auxiliary prime. Modulo $p$, condition (1) says $a^n + (-b)^n + c^n \equiv 0$ implies one of $a, b, c \equiv 0 \pmod{p}$. If $x \equiv 0 \pmod{p}$, then $b^n + c^n \equiv a^n \pmod{p}$. Through a careful case analysis using condition (2), one derives contradictions unless one of $x, y, z \equiv 0 \pmod{p}$. Then descent arguments produce a contradiction to the existence of solutions in Case I.
