---
role: proof
locale: en
of_concept: ford-circles-tangency
source_book: gtm041
source_chapter: "5"
source_section: "5.5"
---

The Ford circle $C(a,b)$ has center $(a/b, 1/(2b^2))$ and radius $1/(2b^2)$. Similarly $C(c,d)$ has center $(c/d, 1/(2d^2))$ and radius $1/(2d^2)$.

The square of the distance $D$ between centers is

$$D^2 = \left(\frac{a}{b} - \frac{c}{d}\right)^2 + \left(\frac{1}{2b^2} - \frac{1}{2d^2}\right)^2.$$

The square of the sum of their radii is

$$(r + R)^2 = \left(\frac{1}{2b^2} + \frac{1}{2d^2}\right)^2.$$

The difference $D^2 - (r + R)^2$ equals

$$D^2 - (r + R)^2 = \left(\frac{ad - bc}{bd}\right)^2 + \left(\frac{1}{2b^2} - \frac{1}{2d^2}\right)^2 - \left(\frac{1}{2b^2} + \frac{1}{2d^2}\right)^2$$

$$= \frac{(ad - bc)^2 - 1}{b^2 d^2} \geq 0.$$

Since the distance between centers is at least the sum of radii, the circles are either tangent ($D = r + R$) or disjoint ($D > r + R$). Equality $D = r + R$ occurs precisely when $(ad - bc)^2 = 1$, i.e. $|ad - bc| = 1$. For consecutive Farey fractions, Theorem 5.5 gives $bc - ad = 1$, so their Ford circles are tangent.
