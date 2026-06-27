---
role: proof
locale: en
of_concept: gauss-lemma-primitive-polynomials
source_book: gtm016
source_chapter: "0.1"
source_section: "0.1 Basic algebra"
---

Let $f^* = \sum a_i X^i$, $g^* = \sum b_j X^j$. Take irreducible $c(x) \in k[x]$, let $a_i$ and $b_j$ be first coefficients not divisible by $c(x)$. The $(i+j)$-th coefficient is $a_i b_j + \sum_{r=1}^i a_{i-r} b_{j+r} + \sum_{s=1}^j a_{i+s} b_{j-s}$. The sums are divisible by $c(x)$ but $a_i b_j$ is not. So no irreducible divides all coefficients. Hence $f^* g^*$ is primitive.
