---
role: proof
locale: en
of_concept: negation-multiplication-rules
source_book: gtm030
source_chapter: "2"
source_section: "1"
---

First, we prove $(-a)b = -ab$. Using the distributive law:
$$0 = 0b = (a + (-a))b = ab + (-a)b.$$

Since $ab + (-a)b = 0$, the element $(-a)b$ is the additive inverse of $ab$. By the uniqueness of additive inverses in a group:
$$(-a)b = -ab.$$

Next, we prove $a(-b) = -ab$ by a symmetric argument using the other distributive law:
$$0 = a0 = a(b + (-b)) = ab + a(-b),$$
which shows $a(-b) = -ab$.

Finally, for $(-a)(-b) = ab$, we apply the previous two results:
$$(-a)(-b) = -(a(-b)) = -(-ab) = ab.$$

The last equality uses the fact that the negative of a negative is the original element in the additive group.
