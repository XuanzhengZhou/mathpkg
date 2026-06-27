---
role: proof
locale: en
of_concept: purely-transcendental-is-separable
source_book: gtm016
source_chapter: "4"
source_section: "4.3"
---

Since any finite subset of $K$ is contained in $k(x_1, \ldots, x_d)$ where $x_1, \ldots, x_d$ are suitable algebraically independent elements of $K$ over $k$, it suffices to show that such a $k(x_1, \ldots, x_d)/k$ is separable. Thus, let $L$ be an algebraically closed field containing $k(x_1, \ldots, x_d)$. Obviously, $k(x_1, \ldots, x_d)$ and $k^{p^{-1}}$ are linearly disjoint over $k$ if and only if $k[x_1, \ldots, x_d]$ and $k^{p^{-1}}$ are linearly disjoint over $k$. The set of monomials

$$M = \{ x_1^{e_1} \cdots x_d^{e_d} \mid e_i \geq 0 \text{ for } 1 \leq i \leq d \}$$

form a $k$-basis for $k[x_1, \ldots, x_d]$ over $k$. Since the set $M^p = \{x^p \mid x \in M\}$ is a subset of $M$, $M^p$ is a $k$-linearly independent set. It follows as in the proof of 4.3.14 that $M$ is $k^{p^{-1}}$-linearly independent, hence $k[x_1, \ldots, x_d]$ and $k^{p^{-1}}$ are linearly disjoint over $k$. Therefore $k(x_1, \ldots, x_d)/k$ is separable. $\square$

[Note: The final portion of this proof references the argument from 4.3.14. The stitched source text was truncated mid-sentence.]
