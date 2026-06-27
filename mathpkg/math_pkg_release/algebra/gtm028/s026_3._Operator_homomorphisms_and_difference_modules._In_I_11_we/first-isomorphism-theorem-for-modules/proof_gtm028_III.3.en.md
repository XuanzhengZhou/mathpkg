---
role: proof
locale: en
of_concept: first-isomorphism-theorem-for-modules
source_book: gtm028
source_chapter: "III"
source_section: "3"
---

Let $T$ be the natural $R$-homomorphism of $M$ onto $M - N$ and let $S$ be the given $R$-homomorphism of $M$ onto $M'$. Consider the transformation $s = S^{-1}T$ of $M'$ onto $M - N$. Explicitly, for $x' \in M'$, choose $x \in M$ such that $xS = x'$; then $x's = xT = x+N$. To show $s$ is well-defined, if $x, y \in M$ satisfy $xS = yS = x'$, then $(x-y)S = 0$, so $x-y \in N$, hence $x+N = y+N$. Thus $s$ is a bijection between $M'$ and $M-N$. Moreover, if $x', y' \in M'$ with $xS = x'$, $yS = y'$, then $(x'+y')s = (xS + yS)s = ((x+y)S)s = (x+y)+N = (x+N)+(y+N) = x's + y's$, and for $a \in R$, $(ax')s = (a(xS))s = ((ax)S)s = ax+N = a(x+N) = a(x's)$. Hence $s$ is an $R$-isomorphism.
