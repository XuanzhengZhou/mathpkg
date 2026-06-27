---
role: proof
locale: en
of_concept: spanier-whitehead-theorem
source_book: gtm020
source_chapter: "16"
source_section: "2"
---

The idea of the proof is to show that

$$S: [X, Y] \to [S(X), S(Y)] = [X, \Omega S(Y)]$$

is a bijection under the stated hypotheses. If $X$ is a CW-complex of dimension $n$ and $Y$ is $r$-connected with $n - 1 < 2r - 1$, then these conditions also hold for $S(X)$ and $S(Y)$.

The bijective character of $[X, Y] \to [X, \Omega S(Y)]$ is established using a Wang-type exact sequence over $S(Y)$ for the fibration

$$ES(Y) \to S(Y)$$

where $ES(Y)$ is the path space over $S(Y)$. The Wang sequence relates the homotopy groups and homotopy classes of the total space $ES(Y)$, the base $S(Y)$, and the fibre $\Omega S(Y)$. Combined with the connectivity and dimension assumptions, this yields that the adjunction map $Y \to \Omega S(Y)$ induces a bijection on homotopy classes from $X$, which gives the bijectivity of the suspension map and consequently the bijectivity of the natural map $[X, Y] \to \{X, Y\}$.