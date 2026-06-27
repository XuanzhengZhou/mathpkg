---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This corollary of Rice's theorem states that the binary relation "y is in the range of the partial recursive function with index x" is not recursive. Equivalently, there is no algorithm to decide, given x and y, whether the x-th partial recursive function ever outputs y. The proof reduces this to Rice's theorem by noting that if this relation were recursive, then the set $\{x : 0 \text{ is in the range of } \varphi^1_x\}$ would also be recursive, which contradicts Rice's theorem since having $0$ in the range is a non-trivial functional property.
