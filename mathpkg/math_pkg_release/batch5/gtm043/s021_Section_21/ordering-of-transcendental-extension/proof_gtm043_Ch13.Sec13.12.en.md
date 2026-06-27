---
role: proof
locale: en
of_concept: ordering-of-transcendental-extension
source_book: gtm043
source_chapter: "13"
source_section: "13.12"
---
It suffices to consider $E[x]$, since $\mathfrak{p}(x)/\mathfrak{q}(x) > 0$ iff $\mathfrak{p}(x)\mathfrak{q}(x) > 0$. Let $\mathfrak{p} \in E[x]$ be nonconstant with leading coefficient $1$.

Since $E$ is real-closed, $\mathfrak{p}$ factors into linear and quadratic factors over $E$.

**Case 1:** $\mathfrak{p} = x - c$ ($c \in E$). Then $\mathfrak{p} > 0$ iff $x > c$.

**Case 2:** $\mathfrak{p} = (x - h)^2 + k$ ($h, k \in E$).
- If $k \geq 0$, then $\mathfrak{p} > 0$ for all $x$, since squares are nonnegative in an ordered field.
- If $k < 0$, then $-k$ has a square root $a$ in the real-closed $E$, so $\mathfrak{p} = (x-h-a)(x-h+a)$, reducing to Case 1.

Thus the sign of each factor depends only on the location of $x$ relative to elements of $E$. Hence the cut of $x$ in $E$ determines the ordering of $E(x)$.