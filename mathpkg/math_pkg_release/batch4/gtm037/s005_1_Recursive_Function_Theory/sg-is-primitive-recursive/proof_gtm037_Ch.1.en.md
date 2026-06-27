---
role: proof
locale: en
of_concept: sg-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

The sign function $sg$ is defined as $sg(x) = \overline{sg}(\overline{sg}(x))$, i.e., the composition of $\overline{sg}$ with itself. By item (7), $\overline{sg}$ is primitive recursive. Since the class of primitive recursive functions is closed under composition, $sg$ is primitive recursive.

To verify correctness:
- If $x = 0$, then $\overline{sg}(0) = 1 \div 0 = 1$, and $\overline{sg}(1) = 1 \div 1 = 0$. So $sg(0) = 0$.
- If $x > 0$, then $\overline{sg}(x) = 1 \div x = 0$, and $\overline{sg}(0) = 1$. So $sg(x) = 1$.

Thus $sg$ acts as the indicator function for positive numbers.
