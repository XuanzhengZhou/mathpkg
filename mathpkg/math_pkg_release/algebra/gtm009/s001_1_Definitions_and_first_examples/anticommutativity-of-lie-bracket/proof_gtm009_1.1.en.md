---
role: proof
locale: en
of_concept: anticommutativity-of-lie-bracket
source_book: gtm009
source_chapter: "1"
source_section: "1.1"
---

Apply axioms (L1) (bilinearity) and (L2) ($[xx] = 0$) to $[x+y, x+y]$:

$$0 = [x+y, x+y] = [xx] + [xy] + [yx] + [yy] = 0 + [xy] + [yx] + 0 = [xy] + [yx].$$

Therefore $[xy] = -[yx]$, which is (L2').

Conversely, if $\operatorname{char} F \neq 2$ and (L2') holds, then setting $y = x$ gives $[xx] = -[xx]$, so $2[xx] = 0$, hence $[xx] = 0$, which is (L2).
