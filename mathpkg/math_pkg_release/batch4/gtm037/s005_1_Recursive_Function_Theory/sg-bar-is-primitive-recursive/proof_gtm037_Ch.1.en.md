---
role: proof
locale: en
of_concept: sg-bar-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

The function $\overline{sg}$ is defined as $\overline{sg}(x) = 1 \div x$. The constant function $K_1(x) = 1$ is primitive recursive (as $C_1^1 x$ or via composition $S \circ C_0^1$). Truncated subtraction $\div$ is primitive recursive (established earlier as a primitive recursive function). Since $\overline{sg}$ is the composition of these two primitive recursive functions, it is primitive recursive.

Explicitly: $\overline{sg}(0) = 1 \div 0 = 1$, and for $x > 0$, $\overline{sg}(x) = 1 \div x = 0$. Thus $\overline{sg}$ acts as the "zero test" indicator, returning 1 at zero and 0 elsewhere.
