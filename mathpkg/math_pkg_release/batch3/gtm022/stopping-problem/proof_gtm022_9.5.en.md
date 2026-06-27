---
role: proof
locale: en
of_concept: stopping-problem
source_book: gtm022
source_chapter: "IX"
source_section: "5"
---

Suppose $f(n) = 1$ if $f_n(n)$ exists (i.e., $M_n$ halts on input $n$), $f(n) = 0$ otherwise, is recursive. Define $g(n) = f_n(n) + 1$ if $f_n(n)$ exists, $g(n) = 0$ otherwise. Then $g$ is recursive. Let $g = f_m$. Then $g(m) = f_m(m) = g(m)$, but also $g(m) = f_m(m) + 1$ if $f_m(m)$ exists. This is a contradiction, so $f$ cannot be recursive.
