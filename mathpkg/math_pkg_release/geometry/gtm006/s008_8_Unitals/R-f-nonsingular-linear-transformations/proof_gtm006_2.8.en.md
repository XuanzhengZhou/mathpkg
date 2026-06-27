---
role: proof
locale: en
of_concept: R-f-nonsingular-linear-transformations
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* Non-singularity: The map $R_f$ is injective because if $x f = y f$, multiplying on the right by $f^{-1}$ gives $x = y$. It is surjective because for any $y \in F$, $y = (y f^{-1}) f = R_f(y f^{-1})$.

Linearity over $K$: For all $x, y \in F$ and $k \in K$,
$$(x + y)R_f = (x + y)f = x f + y f = x R_f + y R_f,$$
$$(k x)R_f = (k x)f = k (x f) = k (x R_f),$$
using the left vector space structure of $F$ over $K$. $\square$