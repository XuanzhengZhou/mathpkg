---
role: proof
locale: en
of_concept: mobius-circle-preserving
source_book: gtm041
source_chapter: "2"
source_section: "2.1"
---

Consider the general equation of a circle or line:
$$Az\bar{z} + Bz + \bar{B}\bar{z} + C = 0,$$
where $A$ and $C$ are real. Points on a circle satisfy this with $A \neq 0$, and points on a line satisfy this with $A = 0$.

Apply the Möbius transformation $z = f(w) = \frac{aw+b}{cw+d}$ (or equivalently, replace $z$ by the inverse transformation). Substituting $z = \frac{aw+b}{cw+d}$ and $\bar{z} = \frac{\bar{a}\bar{w}+\bar{b}}{\bar{c}\bar{w}+\bar{d}}$ into the equation:
$$A\left(\frac{aw+b}{cw+d}\right)\!\left(\frac{\bar{a}\bar{w}+\bar{b}}{\bar{c}\bar{w}+\bar{d}}\right) + B\left(\frac{aw+b}{cw+d}\right) + \bar{B}\left(\frac{\bar{a}\bar{w}+\bar{b}}{\bar{c}\bar{w}+\bar{d}}\right) + C = 0.$$

Multiplying by $(cw+d)(\bar{c}\bar{w}+\bar{d})$ and collecting terms, the result can be written as
$$A' w\bar{w} + B' w + \bar{B}' \bar{w} + C' = 0,$$
where $A'$ and $C'$ are real. This equation has the same form as the original. Therefore $w$ satisfies the equation of a circle (if $A' \neq 0$) or a line (if $A' = 0$). Hence every Möbius transformation maps circles and straight lines onto circles and straight lines.
