---
role: proof
locale: en
of_concept: well-ordered-set-comparison
source_book: gtm053
source_chapter: "1"
source_section: "5"
---

We divide the argument into several steps.

**(a)** Let $X$ be well-ordered, and let $f: X \to X$ be a monotonic map, i.e., $Z_1 < Z_2 \Rightarrow f(Z_1) < f(Z_2)$. Then for all $Z \in X$ we have $f(Z) \geqslant Z$. In fact, among the elements not having this property there would have to be a least element $Z_0$. But $f(Z_0) < Z_0$ and the monotonicity of $f$ imply that $f(f(Z_0)) < f(Z_0)$, so that we would have an even smaller element in the set of elements not having the desired property.

**(b)** Therefore $X$ is not isomorphic to any of its initial segments $\hat{X}_1$: if $f: X \to \hat{X}_1$, then $f(X_1) < X_1$.

**(c)** Now let $X$ and $Y$ be well-ordered. We set

$$f = \{\langle X_1, Y_1 \rangle \mid X_1 \in X,\; Y_1 \in Y\}$$

(here the text continues the construction of the comparison isomorphism by transfinite recursion; the map $f$ is defined to pair the least elements of $X$ and $Y$, then proceed inductively). The three alternatives correspond to whether the domain of $f$ exhausts $X$, its image exhausts $Y$, or both.
