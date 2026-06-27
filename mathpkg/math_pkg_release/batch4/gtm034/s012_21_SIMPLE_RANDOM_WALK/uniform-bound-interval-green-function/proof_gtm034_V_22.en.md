---
role: proof
locale: en
of_concept: uniform-bound-interval-green-function
source_book: gtm034
source_chapter: "V"
source_section: "22"
---

From P22.4, \(g_N(x,y) \leq g(x,y) \leq M[1 + \min(x,y)]\) since the interval Green function is bounded by the half-line Green function. By symmetry, \(g_N(x,y) = g_N(N-y, N-x)\), which also gives \(g_N(x,y) \leq M[1 + \min(N-x, N-y)]\). Combining these yields the stated bound.
