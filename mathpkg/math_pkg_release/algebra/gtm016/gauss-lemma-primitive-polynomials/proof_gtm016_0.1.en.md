---
role: proof
locale: en
of_concept: gauss-lemma-primitive-polynomials
source_book: gtm016
source_chapter: "0.1"
source_section: "0.1"
---

Let $f^*(X) = \sum_{i=0}^m a_i(x)X^i$ and $g^*(X) = \sum_{j=0}^n b_j(x)X^j$. Let $c(x)$ be an irreducible element of $k[x]$. Let $a_i(x)$ and $b_j(x)$ be the first coefficients of $f^*(X)$ and $g^*(X)$ respectively which are not divisible by $c(x)$. Then the $(i+j)$-th coefficient of $f^*(X)g^*(X)$ is $a_i(x)b_j(x) + \sum_{r=1}^i a_{i-r}(x)b_{j+r}(x) + \sum_{s=1}^j a_{i+s}(x)b_{j-s}(x)$. The latter two sums are divisible by $c(x)$ by the choice of $i$ and $j$, while $a_i(x)b_j(x)$ is not divisible by $c(x)$ since $c(x)$ is irreducible. Thus this coefficient is not divisible by $c(x)$. Since no irreducible element divides all coefficients, $f^*(X)g^*(X)$ is primitive.
