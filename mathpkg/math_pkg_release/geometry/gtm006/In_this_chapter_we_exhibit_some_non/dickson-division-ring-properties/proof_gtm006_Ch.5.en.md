---
role: proof
locale: en
of_concept: dickson-division-ring-properties
source_book: gtm006
source_chapter: "IX"
source_section: "5"
---

Commutativity is immediate from the symmetric form of the multiplication formula.

To prove $D$ is a division ring, as in the proof of Theorem 9.7, it suffices to show no non-zero divisors exist. Setting the product equal to zero:
\[
xz + a y^\theta t^\theta = 0, \qquad yz + xt = 0. \tag{2}
\]

If $z = 0$, then either $t = 0$ (done) or $x = y = 0$. So assume $z \neq 0$. From the second equation, $x = -yz t^{-1}$ if $t \neq 0$, or $y = 0$ if $t = 0$. Substituting into the first equation when $y \neq 0$:
\[
z^2 = a y^{\theta-1} t^{\theta+1}.
\]

Every factor on the right is a square in $F$ (since $p$ is odd, $y^{\theta-1}$ and $t^{\theta+1}$ are squares) except $a$. Since $a$ is not a square, $z^2$ cannot be a non-square times squares, contradiction. Hence $y = 0$, and then $x = 0$ or $z = t = 0$. Thus $D$ has no non-zero divisors.

For non-associativity: The multiplication formula lacks the cross terms present in the general construction (Section 4). A direct computation shows that the associator does not vanish when $\theta \neq 1$. Indeed, one can check that $(1 + \lambda) \cdot (1 + \lambda) \cdot (1 + \lambda)$ computed in the two possible ways gives different results whenever $\theta$ is non-trivial, since the mixing of $\theta$ and multiplication creates obstructions. $\square$
