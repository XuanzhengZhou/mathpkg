---
role: proof
locale: en
of_concept: double-orthogonal-inclusion
source_book: gtm049
source_chapter: "5"
source_section: "5.2 Orthogonality"
---

If $a$ is any vector in $M$ and $b$ is any vector in $M^{\perp}$, then by the definition of $M^{\perp}$ we have $\sigma(a, b) = 0$. But this implies that $a$ is an element of $(M^{\perp})^{\top}$ (since $\sigma(a, M^{\perp}) = 0$). Thus $M \subset M^{\perp \top}$.

The other inclusion $M \subset M^{\top \perp}$ is proved similarly: take $a \in M$ and $b \in M^{\top}$. Then by definition $\sigma(M, b) = 0$, so in particular $\sigma(a, b) = 0$. Hence $a \in (M^{\top})^{\perp}$, giving $M \subset M^{\top \perp}$.
