---
role: proof
locale: en
of_concept: "prop-x-decidable-for-validity"
source_book: gtm022
source_chapter: "III"
source_section: "3"
---
Proof. We give an algorithm for deciding if $w \in P(X)$ is valid. The element $w$ is a word $w(x_1, \ldots, x_n)$ in some finite set $x_1, \ldots, x_n$ of variables. Let $\bar{w} = w(u_1, \ldots, u_n)$ be the associated truth function. For each $(a_1, \ldots, a_n) \in \mathbb{Z}_2^n$, we calculate $\bar{w}(a_1, \ldots, a_n)$. By definition, $w$ is valid if and only if all these values are $1$. Since there are $2^n$ tuples to check and each calculation is finite, the truth-table method is an effective decision procedure for validity. $\square$
