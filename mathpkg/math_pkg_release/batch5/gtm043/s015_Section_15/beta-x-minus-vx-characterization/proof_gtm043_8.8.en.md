---
role: proof
locale: en
of_concept: beta-x-minus-vx-characterization
source_book: gtm043
source_chapter: "8"
source_section: "8.8"
---

If $p \in \beta X \setminus vX$, then by condition (4) of Theorem 8.4, there exists $f \in C(X)$ such that $f^*(p) = 0$ but $M^p(f) \neq 0$. Since $f^*(p) = 0$, we have $|f|^* \wedge 1$ also vanishing at $p$; replacing $f$ by this bounded function gives $f \in C^*(X)$. That $M^p(f) \neq 0$ means $f$ is not in the maximal ideal $M^p$, so $Z(f) = \emptyset$ (otherwise $f$ would belong to some zero-set in $Z[M^p]$, contradicting $f \notin M^p$). Thus $f$ is a unit of $C$ with $Z(f) = \emptyset$ while $f^\beta(p) = 0$.

Conversely, if $f \in C^*(X)$ is a unit of $C$ (so $Z(f) = \emptyset$) but not a unit of $C^*$, then $f^\beta$ must vanish somewhere on $\beta X$. Let $p \in \beta X$ be such that $f^\beta(p) = 0$. If $p$ were in $vX$, then by condition (4) of Theorem 8.4, $M^p(f) = 0$, contradicting $Z(f) = \emptyset$. Hence $p \in \beta X \setminus vX$.
