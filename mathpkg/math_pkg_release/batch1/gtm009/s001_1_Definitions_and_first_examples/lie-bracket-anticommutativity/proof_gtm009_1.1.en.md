---
role: proof
locale: en
of_concept: lie-bracket-anticommutativity
source_book: gtm009
source_chapter: "I. Basic Concepts"
source_section: "1. Definitions and first examples"
---

From axioms (L1) (bilinearity) and (L2) ($[xx] = 0$ for all $x \in L$), apply to $[x+y, x+y]$:

$$[x+y, x+y] = 0$$

Expand using bilinearity:

$$[xx] + [xy] + [yx] + [yy] = 0$$

By (L2), $[xx] = 0$ and $[yy] = 0$, so:

$$[xy] + [yx] = 0$$

Hence $[xy] = -[yx]$.

Conversely, if $\operatorname{char} F \neq 2$ and $[xy] = -[yx]$ holds for all $x, y$, then setting $y = x$ gives $[xx] = -[xx]$, so $2[xx] = 0$, which implies $[xx] = 0$ since 2 is invertible in $F$.
