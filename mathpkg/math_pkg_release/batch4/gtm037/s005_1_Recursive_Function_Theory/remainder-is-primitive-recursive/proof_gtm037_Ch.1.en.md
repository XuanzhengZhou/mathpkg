---
role: proof
locale: en
of_concept: remainder-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

Define the auxiliary function $f$ by primitive recursion:

- Base: $f(x, 0) = 0$ (the constant-zero function, primitive recursive).
- Step: $f(x, \delta y) = \delta f(x, y) \cdot \overline{sg}\,|x - \delta f(x, y)|$.

The step function is a composition of the primitive recursive functions $\delta$ (successor), $\cdot$ (multiplication), $\overline{sg}$ (modified sign), and $| \cdot |$ (absolute difference), hence primitive recursive. Therefore $f$ is primitive recursive.

Then the remainder function is defined as $rm(x, y) = f(y, x)$. This is just a permutation of arguments of $f$, which is primitive recursive (via composition with projections). Thus $rm$ is primitive recursive.

The intuition: $f(x, y)$ increments by 1 at each step unless the increment would exceed $x$, in which case it resets to 0 (via $\overline{sg}$). Thus $f(x, y) = y \bmod x$ (with the convention $y \bmod 0 = 0$).
