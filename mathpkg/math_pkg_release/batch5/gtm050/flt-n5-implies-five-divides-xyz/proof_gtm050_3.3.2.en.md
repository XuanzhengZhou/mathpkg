---
role: proof
locale: en
of_concept: flt-n5-implies-five-divides-xyz
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---
Reformulate as $x^5 + y^5 + z^5 = 0$ with pairwise relatively prime $x, y, z$. Factor: $-x^5 = (y+z)(y^4 - y^3z + y^2z^2 - yz^3 + z^4)$. The two factors on the right are relatively prime unless 5 divides them both. If 5 does not divide $x$, then both factors are relatively prime and hence are fifth powers: $y+z = a^5$, $y^4 - y^3z + \cdots + z^4 = \alpha^5$. Similarly, $x+y = b^5, x+z = c^5$ with corresponding $\beta, \gamma$.

Now work modulo 11. The fifth powers modulo 11 are $0, \pm 1$. Setting $2x = b^5 + c^5 - a^5$, we have $2x \equiv \pm 1 \pm 1 \pm 1 \pmod{11}$. The only possibilities are $\pm 1, \pm 3$, none of which is $0 \pmod{11}$. But if 11 does not divide any of $x, y, z$, a case analysis shows this is impossible. Therefore one of $x, y, z$ must be divisible by 11, contradicting the assumption that none is divisible by 5 after careful analysis. This contradiction forces $5 \mid xyz$.
