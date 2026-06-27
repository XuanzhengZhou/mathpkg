---
role: proof
locale: en
of_concept: continuity-of-linear-map-at-zero
source_book: gtm003
source_chapter: "III"
source_section: "1"
---

If $V$ is a given $0$-neighborhood in $M$, and $U$ is a $0$-neighborhood in $L$ such that $u(U) \subset V$, then $x - y \in U$ implies $u(x - y) = u(x) - u(y) \in V$. Hence if $u$ is continuous at $0$, it is even uniformly continuous on $L$ into $M$ for the respective uniformities.

For the extension: since $L$ is dense in $\bar{L}$, every point of $\bar{L}$ is a limit of a net in $L$. By uniform continuity of $u$, the image net is Cauchy in the complete space $M$, hence converges. The limit defines $\bar{u}$, and uniqueness follows from the Hausdorff property of $M$. Linearity of $\bar{u}$ follows from continuity of the vector space operations.
