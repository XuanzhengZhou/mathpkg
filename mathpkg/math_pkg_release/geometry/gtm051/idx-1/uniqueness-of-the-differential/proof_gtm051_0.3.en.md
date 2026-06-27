---
role: proof
locale: en
of_concept: uniqueness-of-the-differential
source_book: gtm051
source_chapter: "0"
source_section: "0.3"
---

Suppose $L$ and $L'$ both satisfy the definition of the differential. Then subtracting the two expansions gives

$$(L - L')(x - x_0) = (F(x) - F(x_0) - L'(x - x_0)) - (F(x) - F(x_0) - L(x - x_0)).$$

Taking absolute values and using the triangle inequality,

$$|(L - L')(x - x_0)| \leq |F(x) - F(x_0) - L(x - x_0)| + |F(x) - F(x_0) - L'(x - x_0)|.$$

Both terms on the right are $o(|x - x_0|)$, so

$$|(L - L')(x - x_0)| = o(|x - x_0|).$$

In particular, let $x - x_0 = r e_i$ where $r > 0$ and $e_i$ is the $i$-th standard basis vector. Let $a_i, a_i'$ be the column vectors of the matrices representing $L, L'$. Then

$$r \cdot |a_i - a_i'| = o(r).$$

Dividing by $r$ and taking the limit $r \to 0$, we obtain $|a_i - a_i'| = 0$, hence $a_i = a_i'$ for all $i$. Therefore $L = L'$.
