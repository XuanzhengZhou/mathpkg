---
role: proof
locale: en
of_concept: distance-function-distance-decreasing
source_book: gtm026
source_chapter: "1"
source_section: "Exercise 20"
---

By the triangle inequality applied to the metric $d$,
$$d(x, y) \leq d(x, z) + d(z, y) = d(x, z) + d(y, z).$$
Hence
$$d(x, y) - d(x, z) \leq d(y, z).$$

Exchanging $y$ and $z$ yields
$$d(x, z) - d(x, y) \leq d(y, z).$$

Combining the two inequalities gives
$$|d(x, y) - d(x, z)| \leq d(y, z).$$

Since the right-hand side is exactly $d_{\mathbb{R}}(d(x, y), d(x, z))$ (the usual metric on $\mathbb{R}$), the map $d(x, -)$ is distance decreasing.
