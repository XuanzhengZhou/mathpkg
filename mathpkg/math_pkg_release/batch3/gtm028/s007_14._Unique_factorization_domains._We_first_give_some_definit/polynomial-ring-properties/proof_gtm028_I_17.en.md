---
role: proof
locale: en
of_concept: polynomial-ring-properties
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

The set $S$ of all finite sequences with addition defined componentwise and multiplication defined by the Cauchy product $c_k = \sum_{i+j=k} a_i b_j$ is immediately seen to form a ring. The zero element is $\{0, 0, 0, \cdots\}$ and $-f = \{-a_0, -a_1, -a_2, \cdots\}$.

The map $a \mapsto (a, 0, 0, \cdots)$ is a ring homomorphism embedding $R$ into $S$ as a subring. If $R$ has identity $1$, then $1' = (1, 0, 0, \cdots)$ is the identity of $S$: for any $f = \{a_i\}$, we have $f \cdot 1' = \{a_i\}$ by the product formula. Conversely, if $S$ has an identity, then restricting to the embedded copy of $R$ shows $R$ must have an identity.

For the degree property: let $f = \{a_i\}$ have $\partial f = n$ (so $a_n \neq 0$) and $g = \{b_j\}$ have $\partial g = m$ (so $b_m \neq 0$). In the product $fg = \{c_k\}$ where $c_k = \sum_{i+j=k} a_i b_j$, the term with $k = n+m$ is $c_{n+m} = a_n b_m$ (all other terms in the sum have either $i > n$ or $j > m$, making $a_i = 0$ or $b_j = 0$). For $k > n+m$, every term has $i > n$ or $j > m$, so $c_k = 0$. Thus either $fg = 0$ (if $a_n b_m = 0$) or $\partial(fg) = n + m$. Therefore $\partial(fg) \leq \partial f + \partial g$, with equality holding if and only if the product of leading coefficients $a_n b_m \neq 0$, in which case $a_n b_m$ is the leading coefficient of $fg$.

If $R$ is an integral domain, then $a_n b_m \neq 0$ whenever $a_n \neq 0$ and $b_m \neq 0$, so $fg \neq 0$ for any non-zero $f, g$. Thus $S$ is an integral domain. Moreover, if $f = \{a_i\}$ is a unit in $S$, then there exists $g = \{b_j\}$ such that $fg = 1' = (1, 0, 0, \cdots)$. Taking degrees, $0 = \partial(1') = \partial(fg) = \partial f + \partial g$ (since $R$ is an integral domain), which forces $\partial f = \partial g = 0$. Thus $f = (a_0, 0, 0, \cdots)$ with $a_0$ a unit in $R$. This shows the units of $S$ are exactly the images of the units of $R$ under the embedding.
