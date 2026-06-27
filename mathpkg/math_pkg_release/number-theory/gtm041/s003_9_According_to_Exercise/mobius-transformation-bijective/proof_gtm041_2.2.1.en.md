---
role: proof
locale: en
of_concept: mobius-transformation-bijective
source_book: gtm041
source_chapter: "2"
source_section: "2.1"
---

**Injectivity.** From the difference formula
$$f(w) - f(z) = \frac{(ad-bc)(w-z)}{(cw+d)(cz+d)},$$
if $f(w) = f(z)$ then the left side vanishes. Since $ad-bc \neq 0$, we must have $w = z$. Hence $f$ is one-to-one on $C^*$ (taking proper account of the definitions at the pole and infinity).

**Surjectivity.** Solve $f(z) = w$ for $z$:
$$w = \frac{az+b}{cz+d} \implies w(cz+d) = az+b \implies cwz + dw = az + b \implies (cw-a)z = b - dw.$$
Thus
$$z = \frac{dw - b}{-cw + a},$$
which is defined for all $w \in C^*$ (with appropriate conventions at the pole and infinity). Therefore $f$ maps $C^*$ onto $C^*$.
