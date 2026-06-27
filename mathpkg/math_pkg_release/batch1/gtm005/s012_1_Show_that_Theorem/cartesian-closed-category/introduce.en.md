---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A cartesian closed category (CCC) is a category with finite products and exponentials -- that is, for any two objects $b$ and $c$, there is an object $c^b$ (thought of as the "object of morphisms from $b$ to $c$") with an evaluation map $c^b \times b \to c$ satisfying the universal property that morphisms $a \times b \to c$ correspond bijectively to morphisms $a \to c^b$. The category Set is cartesian closed with $c^b = \hom(b, c)$, and Cat is cartesian closed with exponent $C^B$ being the functor category. Cartesian closed categories provide the categorical semantics for simply typed lambda calculus and are fundamental in theoretical computer science.
