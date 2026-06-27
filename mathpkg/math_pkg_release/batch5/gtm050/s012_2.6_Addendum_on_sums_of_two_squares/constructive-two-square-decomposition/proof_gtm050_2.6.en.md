---
role: proof
locale: en
of_concept: constructive-two-square-decomposition
source_book: gtm050
source_chapter: "2"
source_section: "2.6 Addendum on sums of two squares"
---

Step (5) of Euler's proof is constructive: if $4n+1$ is prime then at least one of the numbers $1^{2n} + 2^{2n}, 2^{2n} + 3^{2n}, \ldots, (4n-1)^{2n} + (4n)^{2n}$ must be divisible by $4n+1$.

For Fermat's example $p = 53 = 4 \cdot 13 + 1$, one finds $2^6 = 64 \equiv 11 \pmod{53}$, $2^{12} \equiv 11^2 = 121 \equiv 15 \pmod{53}$, $2^{13} \equiv 30 \pmod{53}$, $2^{26} \equiv 30^2 = 900 \equiv -1 \pmod{53}$, so $2^{26} + 1$ is divisible by $53$. This yields $53 \cdot 17 \cdot 17 = 53 \cdot 289 = 30^2 + 1^2$.

The division step uses the Brahmagupta-Fibonacci identity:

$$(a^2 + b^2)(c^2 + d^2) = (ac \mp bd)^2 + (ad \pm bc)^2.$$

For $k = 17 = 1^2 + 4^2$, one computes

$$17 \cdot 17 \cdot 53 = (1^2 + 4^2)(30^2 + 1^2) = (30 \mp 4)^2 + (1 \pm 120)^2,$$

and choosing signs to make division by $17$ possible gives

$$53 = \left(\frac{34}{17}\right)^2 + \left(\frac{119}{17}\right)^2 = 2^2 + 7^2.$$

A superior general method avoids factoring $k$ by dividing by $k$ at the cost of multiplying by a smaller number $n$: if $a^2 + b^2 = kp$, find $c \equiv a \cdot b^{-1} \pmod{k}$ with $c^2 \equiv -1 \pmod{k}$, set $c = a - mk$ so that $c^2 + 1^2 = nk$ with $n < k$, then

$$nk \cdot kp = (c^2 + 1^2)(a^2 + b^2) = (ca \mp b)^2 + (cb \pm a)^2,$$

from which $p = ((ca \mp b)/k)^2 + ((cb \pm a)/k)^2$, reducing the problem to a smaller multiplier $n$.

For $p = 229$, one finds $2^{57} \equiv 122 \pmod{229}$ and $122^2 + 1 = 65 \cdot 229$. With $c = 122 - 2 \cdot 65 = -8$, one gets $8^2 + 1^2 = 65$, and then

$$65 \cdot 65 \cdot 229 = (8^2 + 1^2)(122^2 + 1^2) = (976 \mp 1)^2 + (8 \pm 122)^2,$$

yielding $229 = (975/65)^2 + (130/65)^2 = 15^2 + 2^2$.
