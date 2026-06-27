---
role: proof
locale: en
of_concept: compact-gdelta-characterization
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

Since $\{x: f(x) \geq c\} = X - \{x: f(x) < c\}$ is the complement of an open set, it is closed; it is the intersection of the sequence of open sets $\{x: f(x) > c - \frac{1}{n}\}$, hence a $G_{\delta}$. The proofs for the other two sets are similar. Conversely, if $C = \bigcap_{n=1}^{\infty} U_n$ where each $U_n$ is open, then for each $n$ there exists a function $f_n$ in $\mathfrak{F}$ such that $f_n(x) = 0$ for $x$ in $C$ and $f_n(x) = 1$ for $x$ in $X - U_n$. If $f(x) = \sum_{n=1}^{\infty} \frac{1}{2^n} f_n(x)$, then $f \in \mathfrak{F}$ and $C = \{x: f(x) = 0\}$.
