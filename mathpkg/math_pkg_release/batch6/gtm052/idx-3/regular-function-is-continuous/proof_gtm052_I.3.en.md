---
role: proof
locale: en
of_concept: regular-function-is-continuous
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

It is enough to show that $f^{-1}$ of a closed set is closed. A closed set of $\mathbf{A}_k^1$ is a finite set of points, so it is sufficient to show that $f^{-1}(a) = \{P \in Y \mid f(P) = a\}$ is closed for any $a \in k$. This can be checked locally: a subset $Z$ of a topological space $Y$ is closed if and only if $Y$ can be covered by open subsets $U$ such that $Z \cap U$ is closed in $U$ for each $U$.

So let $U$ be an open set on which $f$ can be represented as $g/h$, with $g, h \in A = k[x_1, \ldots, x_n]$, and $h$ nowhere $0$ on $U$. Then

$$f^{-1}(a) \cap U = \{P \in U \mid g(P)/h(P) = a\}.$$

But $g(P)/h(P) = a$ if and only if $(g - ah)(P) = 0$. So

$$f^{-1}(a) \cap U = Z(g - ah) \cap U$$

which is closed in $U$. Hence $f^{-1}(a)$ is closed in $Y$.
