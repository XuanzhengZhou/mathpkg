---
role: proof
locale: en
of_concept: coproducts-in-set
source_book: gtm026
source_chapter: "1"
source_section: "1. The Base Category"
---

Define $\coprod_{i \in I} A_i = \{(i, a) : i \in I,\; a \in A_i\}$ and $\text{in}_i(a) = (i, a)$ for $a \in A_i$.

To verify the universal property, let $f_i: A_i \to B$ be a family of functions. Define $f: \coprod A_i \to B$ by $f(i, a) = f_i(a)$. Then for any $a \in A_i$,
$$(\text{in}_i \circ f)(a) = f(\text{in}_i(a)) = f(i, a) = f_i(a),$$
so $\text{in}_i \circ f = f_i$ for all $i \in I$.

For uniqueness, suppose $g: \coprod A_i \to B$ satisfies $\text{in}_i \circ g = f_i$ for all $i$. Then for any $(i, a) \in \coprod A_i$,
$$g(i, a) = g(\text{in}_i(a)) = (\text{in}_i \circ g)(a) = f_i(a) = f(i, a).$$
Thus $g = f$, establishing uniqueness.
