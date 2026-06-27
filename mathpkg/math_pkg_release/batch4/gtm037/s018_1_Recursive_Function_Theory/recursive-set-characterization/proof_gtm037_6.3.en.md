---
role: proof
locale: en
of_concept: recursive-set-characterization
source_book: gtm037
source_chapter: "6"
source_section: "6.3"
---

$(ii) \Rightarrow (i)$ is the main part of 6.6. Assume $(ii)$. We may suppose $\emptyset \neq A \neq \omega$. Then let $f$ and $g$ be recursive functions with $\operatorname{Rng} f = A$, $\operatorname{Rng} g = \omega \setminus A$. To determine whether $x \in A$ or not, list out $f0, g0, f1, g1, \ldots$. Eventually $x$ will appear in the list; if $x = fn$ for some $n$, then $x \in A$, while if $x = gn$ for some $n$, then $x \notin A$.

Hence for all $y \in \omega$,

$$\chi_A y = 1 \quad \text{if } \exists x \leq y (fx = y),$$
$$\chi_A y = 0 \quad \text{otherwise},$$

as desired. $\square$
