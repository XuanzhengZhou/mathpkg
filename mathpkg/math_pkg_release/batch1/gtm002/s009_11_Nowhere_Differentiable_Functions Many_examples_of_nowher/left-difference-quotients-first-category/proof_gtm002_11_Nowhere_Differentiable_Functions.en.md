---
role: proof
locale: en
of_concept: left-difference-quotients-first-category
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

This follows from the main theorem by symmetry. Consider the isometry $T : C[0,1] \to C[0,1]$ induced by the substitution of $1 - x$ for $x$, i.e.,

$$(Tf)(x) = f(1 - x).$$

This mapping is an isometry of the uniform metric and interchanges right and left difference quotients: a function $f$ has a bounded right difference quotient at $x_0$ if and only if $Tf$ has a bounded left difference quotient at $1 - x_0$. Since the set of functions with bounded right difference quotients is of first category in $C[0,1]$, its image under the isometry $T$ — which is precisely the set of functions with bounded left difference quotients — is also of first category.
