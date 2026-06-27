---
role: proof
locale: en
of_concept: closure-equals-double-commutant
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

By the corollary of (6.4), $\bar{A}$ (the strong closure of $A$) is a $W^*$-algebra, and since $A$ is non-degenerate, $\bar{A} \neq \{0\}$. Hence $\bar{A}$ is unital by the corollary of (6.2). Let $p$ denote the unit of $\bar{A}$; then $p$ is a projection in $\mathcal{L}(H)$ satisfying $px = xp = x$ for all $x \in A$.

Because $A$ is non-degenerate (i.e., $A\xi = \{0\}$ implies $\xi = 0$ for $\xi \in H$), we must have $p = e = \mathrm{id}_H$. Thus $\bar{A}$ is a von Neumann algebra containing $e$.

Now $\bar{A} = \bar{A}^{cc}$ by Theorem 7.1. Since $A \subset \bar{A}$, taking double commutants (which is anti-tone and idempotent) yields $A^{cc} \subset \bar{A}^{cc} = \bar{A}$. Conversely, $\bar{A}$ is contained in $A^{cc}$ because the double commutant is strongly closed and contains $A$. Therefore $\bar{A} = A^{cc}$.
