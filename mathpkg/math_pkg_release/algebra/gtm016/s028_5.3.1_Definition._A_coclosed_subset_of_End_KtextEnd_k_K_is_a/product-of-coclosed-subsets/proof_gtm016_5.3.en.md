---
role: proof
locale: en
of_concept: product-of-coclosed-subsets
source_book: gtm016
source_chapter: "5"
source_section: "5.3"
---

Observe that if $x(ab) = \sum_i x(a)x_i(b)$ and $y(ab) = \sum_j y(a)y_j(b)$ for all $a,b \in K$, then $(xy)(ab) = x(y(ab)) = x(\sum_j y(a)y_j(b))$. Using the coclosed property of $x$ on $(y(a), y_j(b))$, we have $x(y(a)y_j(b)) = \sum_i x(y(a)) x_i(y_j(b))$. Hence $(xy)(ab) = \sum_{i,j} x(y(a)) x_i(y_j(b))$ for all $a,b \in K$, showing $H_1 H_2$ is coclosed.
