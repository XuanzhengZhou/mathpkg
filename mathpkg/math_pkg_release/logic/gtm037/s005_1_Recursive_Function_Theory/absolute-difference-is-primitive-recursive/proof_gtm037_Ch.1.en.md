---
role: proof
locale: en
of_concept: absolute-difference-is-primitive-recursive
source_book: gtm037
source_chapter: "1"
source_section: "Recursive Function Theory"
---

The absolute difference is defined as

$$|x - y| = (x \div y) + (y \div x).$$

Truncated subtraction $\div$ (monus) is a primitive recursive function (established earlier). The addition function $+$ is primitive recursive by item (4). Since the class of primitive recursive functions is closed under composition, the function $(x, y) \mapsto (x \div y) + (y \div x)$ is primitive recursive. Therefore $|x - y|$ is primitive recursive.
