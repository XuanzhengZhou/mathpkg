---
role: proof
locale: en
of_concept: bhaskara-cyclic-method
source_book: gtm050
source_chapter: "1"
source_section: "1.9"
---

The cyclic method (chakravala) is illustrated with the example $A = 67$. Start with the approximation $8^2 - 67 \cdot 1^2 = -3$, which is close to the desired $1$. The fundamental identity used is:

$$(a^2 - 67b^2)(c^2 - 67d^2) = (ac + 67bd)^2 - 67(ad + bc)^2.$$

Applying this to $8^2 - 67 \cdot 1^2 = -3$ and $r^2 - 67 \cdot 1^2 = s$ yields:

$$(8r + 67)^2 - 67(r + 8)^2 = -3s.$$

The key insight is to choose $r$ so that $r + 8$ is divisible by 3, while keeping $|s|$ minimal. Then $8r + 67$ is also divisible by 3, and the equation can be divided by $3^2 = 9$, yielding a new case with a new right-hand side.

Continuing this process for $A = 67$ yields the sequence:

$$1^2 - 67 \cdot 0^2 = 1$$
$$8^2 - 67 \cdot 1^2 = -3$$
$$41^2 - 67 \cdot 5^2 = 6$$
$$90^2 - 67 \cdot 11^2 = -7$$
$$221^2 - 67 \cdot 27^2 = -2$$
$$1889^2 - 67 \cdot 232^2 = -7$$
$$3577^2 - 67 \cdot 437^2 = 6$$
$$9053^2 - 67 \cdot 1106^2 = -3$$
$$48842^2 - 67 \cdot 5967^2 = 1$$

A shortcut is available when $k = -2$: squaring $221^2 - 67 \cdot 27^2 = -2$ yields $(221^2 + 67 \cdot 27^2)^2 - 67(2 \cdot 27 \cdot 221)^2 = 4$, and after dividing by $2^2$ one obtains $48842^2 - 67 \cdot 5967^2 = 1$.

In general, at stage $n$ with $p^2 - Aq^2 = k$, multiply by $r^2 - A = s$ using the identity to obtain $(pr + qA)^2 - A(p + qr)^2 = ks$. Choose $r$ so that $p + qr \equiv 0 \pmod{k}$ and $|s|$ is minimal. Then $pr + qA \equiv 0 \pmod{k}$ as well, and dividing by $k^2$ gives the next stage with $K = s/k$. Continue until $k = \pm 1$, then square if needed to reach $k = 1$.

That this process always terminates is not obvious; the first proof was given by Lagrange.
