---
role: proof
locale: en
of_concept: linear-dependence-of-two-vectors
source_book: gtm023
source_chapter: "I"
source_section: "§1. Vector spaces"
---

This follows directly from the characterization of linear dependence for families of two or more vectors.

If $y = \lambda x$, then $1 \cdot y - \lambda \cdot x = 0$ is a nontrivial linear relation (the coefficient of $y$ is $1 \neq 0$), so $x$ and $y$ are linearly dependent. The symmetric case $x = \lambda y$ yields $-\lambda y + 1 \cdot x = 0$.

Conversely, if $x$ and $y$ are linearly dependent, there exist scalars $\alpha, \beta \in \Gamma$, not both zero, such that $\alpha x + \beta y = 0$. If $\beta \neq 0$, then $y = -\beta^{-1} \alpha x$, so $y = \lambda x$ with $\lambda = -\beta^{-1} \alpha$. If $\beta = 0$, then $\alpha \neq 0$ and the relation reduces to $\alpha x = 0$, giving $x = 0$, whence $x = 0 \cdot y$, so $x = \lambda y$ with $\lambda = 0$.
