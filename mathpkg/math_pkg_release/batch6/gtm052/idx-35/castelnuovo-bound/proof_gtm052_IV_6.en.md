---
role: proof
locale: en
of_concept: castelnuovo-bound
source_book: gtm052
source_chapter: "IV"
source_section: "§6"
---
Given $X$, let $D$ be its hyperplane section. The idea of the proof is to estimate $\dim|nD| - \dim|(n - 1)D|$ for any $n$, and then add. First of all, we choose the hyperplane section $D = P_1 + \ldots + P_d$ in such a way that no three of the points $P_i$ are collinear. This is possible because not every secant of $X$ is a multisecant.

Now one claims for each $i = 1, 2, \ldots, \min(d, 2n + 1)$, that $P_i$ is not a base point of $|nD|$. Using this, one obtains $\dim|nD| - \dim|(n-1)D| \geqslant \min(d, 2n+1)$. Summing these estimates and comparing with the Riemann-Roch formula yields the bound. [The full proof is truncated in the OCR source; see Hartshorne §IV.6 or Castelnuovo's original 1889 paper for the complete argument.]

Equality is attained when the curve lies on a quadric surface, in which case one can check the bound is sharp by explicit computation with the linear systems on the quadric.
