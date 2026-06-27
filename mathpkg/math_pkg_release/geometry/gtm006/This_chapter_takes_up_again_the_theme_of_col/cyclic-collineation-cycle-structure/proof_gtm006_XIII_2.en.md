---
role: proof
locale: en
of_concept: cyclic-collineation-cycle-structure
source_book: gtm006
source_chapter: "XIII"
source_section: "2"
---

Let $\Pi = \langle \pi \rangle$ be a cyclic collineation group. For each $k$, the element $\pi^k$ is a collineation, so by Theorem 13.3, $\pi^k$ fixes equally many points and lines.

Let $p_x$ be the number of point cycles of length $x$ under $\Pi$, and let $l_x$ be the number of line cycles of length $x$. Using the standard formula relating cycle structure to fixed points of powers of a permutation (Result 1.14 applied to $\Pi(P)$ and $\Pi(l)$ respectively), the number of fixed points of $\pi^k$ is:
$$
\sum_{x \mid k} x \cdot p_x
$$
and similarly the number of fixed lines of $\pi^k$ is:
$$
\sum_{x \mid k} x \cdot l_x.
$$

By Theorem 13.3, these are equal for every $k$. A standard Möbius inversion argument then yields $p_x = l_x$ for all $x$. Thus $\Pi(P)$ and $\Pi(l)$ have the same cycle structure.
