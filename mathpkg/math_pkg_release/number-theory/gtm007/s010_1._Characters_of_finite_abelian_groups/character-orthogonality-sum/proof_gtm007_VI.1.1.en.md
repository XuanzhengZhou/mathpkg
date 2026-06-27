---
role: proof
locale: en
of_concept: character-orthogonality-sum
source_book: gtm007
source_chapter: "VI"
source_section: "§1.1"
---

This follows from Proposition 3 (or more precisely from the generalized orthogonality relation, Proposition 4) applied to the dual group $\widehat{G}$.

For a finite abelian group $A$, the orthogonality of characters states:
$$\sum_{a \in A} \chi(a) = \begin{cases} |A| & \text{if } \chi = 1 \\ 0 & \text{if } \chi \neq 1. \end{cases}$$

Apply this to $A = \widehat{G}$ and the character on $\widehat{G}$ given by evaluation at $x$, i.e., $\chi \mapsto \chi(x)$. By the bidual isomorphism (Proposition 3), this evaluation character is trivial if and only if $x = 1$. The sum over all $\chi \in \widehat{G}$ of $\chi(x)$ is therefore $|\widehat{G}| = |G|$ when $x = 1$, and $0$ otherwise.
