---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The remainder function $rm(x, y)$ computes the remainder when dividing $y$ by $x$ (with $rm(x,0) = 0$). It is defined via an auxiliary function $f$ that increments a counter until it reaches the dividend, resetting when the absolute difference exceeds the divisor. The construction uses primitive recursion together with the previously established primitive recursive functions: successor, multiplication, modified sign $\overline{sg}$, and absolute difference.
