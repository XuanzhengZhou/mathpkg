---
role: proof
locale: en
of_concept: dual-of-order-topology
source_book: gtm003
source_chapter: "V"
source_section: "6"
---

A linear form $f$ on $L$ is continuous for $\mathfrak{T}_O$ if and only if $f$ is bounded on some $0$-neighborhood $W$. Since $W$ absorbs every order interval, $f$ is bounded on every order interval, i.e., $f \in L^b$.

Conversely, if $f \in L^b$, then for each order interval $I$ there exists $\lambda > 0$ such that $|f(x)| \leq \lambda$ for $x \in I$. The set $W = \{x : |f(x)| \leq 1\}$ is convex and absorbs every order interval, hence is a $0$-neighborhood for $\mathfrak{T}_O$, so $f$ is continuous.
