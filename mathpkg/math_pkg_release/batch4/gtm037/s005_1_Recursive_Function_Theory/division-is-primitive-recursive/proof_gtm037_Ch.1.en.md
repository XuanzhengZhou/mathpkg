---
role: proof
locale: en
of_concept: division-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

Define the auxiliary function $f$ by primitive recursion:

- Base: $f(x, 0) = 0$ (constant-zero function, primitive recursive).
- Step: $f(x, \delta y) = f(x, y) + \overline{sg}\,|x - \delta\, rm(x, y)|$.

The right-hand side is built from primitive recursive functions ($+$, $\overline{sg}$, $| \cdot |$, $\delta$, $rm$) by composition, so the step function is primitive recursive. Hence $f$ is primitive recursive.

Then $[x/y] = f(y, x)$ is primitive recursive by permutation of arguments.

The intuition: $\overline{sg}\,|x - \delta\, rm(x, y)|$ equals 1 when the remainder has just wrapped around (i.e., exactly when the counter reaches a multiple of the divisor), and 0 otherwise. Thus $f(x, y)$ counts the number of complete cycles of the remainder, which is precisely $\lfloor y / x \rfloor$ (with the convention $[x/0] = f(0, x) = 0$).
