---
role: proof
locale: en
of_concept: castelnuovos-bound
source_book: gtm052
source_chapter: "IV"
source_section: "6"
---

Given $X$, let $D$ be its hyperplane section. The idea of the proof is to estimate $\dim|nD| - \dim|(n-1)D|$ for any $n$, and then add. First of all, we choose the hyperplane section $D = P_1 + \ldots + P_d$ in such a way that no three of the points $P_i$ are collinear. This is possible because not every secant of $X$ is a multisecant (3.8), (3.9), (Ex. 3.9).

Now one claims for each $i = 1, 2, \ldots, \min(d, 2n+1)$, that $P_i$ is not a base point of $|nD - P_1 - \ldots - P_{i-1}|$. This geometric claim is proved by considering the projection from $P_i$ and using the choice of $D$ to avoid trisecants. Iterating this argument yields the dimension estimate

$$\dim|nD| \geqslant \sum_{j=1}^{n} \min(d, 2j+1).$$

On the other hand, by Riemann–Roch, $\dim|nD| = nd + 1 - g$ for $n$ sufficiently large (since $nD$ becomes nonspecial). Comparing these two expressions and evaluating the sum gives the Castelnuovo bound.

When equality holds, the dimension estimates must all be tight, which forces the curve to lie on a quadric surface. The curves achieving equality are exactly the divisors of type $(a,b)$ on a nonsingular quadric surface, or their limits on a quadric cone.
