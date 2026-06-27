---
role: proof
locale: en
of_concept: homomorphism-preserves-zero-one-order
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.**

1. $f(0) = f(0 \cdot (-0)) = f(0) \cdot (-f(0)) = 0$.

2. $f(1) = f(1 + (-1)) = f(1) + (-f(1)) = 1$.

3. $x \leq y \rightarrow x = xy \rightarrow f(x) = f(x)f(y) \rightarrow f(x) \leq f(y)$.
