---
role: proof
locale: en
of_concept: range-membership-not-recursive
source_book: gtm037
source_chapter: "5"
source_section: "1. Recursive Function Theory"
---

If the given set $\{(x, y) : y \text{ is in the range of } \varphi^1_x\}$ is recursive, then clearly so is

$$\{x : 0 \text{ is in the range of } \varphi^1_x\},$$

since $0$ is a fixed number and the set is obtained by fixing the second coordinate. But the property "has $0$ in its range" is a non-trivial property of partial recursive functions (some functions have $0$ in their range and some do not). By Rice's theorem (5.17), the index set of functions with $0$ in their range is not recursive, a contradiction.
