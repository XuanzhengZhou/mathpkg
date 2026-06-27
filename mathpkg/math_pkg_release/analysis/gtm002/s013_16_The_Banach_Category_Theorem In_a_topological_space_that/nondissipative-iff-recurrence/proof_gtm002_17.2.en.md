---
role: proof
locale: en
of_concept: nondissipative-iff-recurrence
source_book: gtm002
source_chapter: "17"
source_section: "The Poincare Recurrence Theorem"
---

**Proof.** Suppose $T$ is nondissipative. Consider any $E \in \mathcal{S}$, and let

$$F = E - \bigcup_{k=1}^{\infty} T^{-k}E.$$

Since $T$ is $\mathcal{S}$-measurable and $\mathcal{S}$ is a $\sigma$-ring, $F$ belongs to $\mathcal{S}$. The sets $T^{-i}F$ ($i = 0,1,2,\ldots$) are mutually disjoint, for if $x \in T^{-i}F \cap T^{-j}F$ for some $i < j$, then $T^j x \in F \subset E$, so $T^i x \in T^{-(j-i)}E$. But $T^i x \in F = E - \bigcup_{k=1}^{\infty} T^{-k}E$, a contradiction. Thus $F$ is a wandering set. Since $T$ is nondissipative, it follows that $F \in \mathcal{I}$.

Now the sets $T^{-i}F$ ($i = 0,1,2,\ldots$) are clearly subsets of $E$, and $x \in D(E)$ if and only if $x = T^i y$ for some $y \in F$ and some $i \geq 0$. Hence

$$D(E) = \bigcup_{i=0}^{\infty} T^{-i}F.$$

Since $\mathcal{I}$ is a $\sigma$-ideal, $D(E) \in \mathcal{I}$. This shows that $T$ has the recurrence property.

Conversely, suppose $T$ has the recurrence property. If $E \in \mathcal{S}$ is a wandering set, then by definition the sets $E, T^{-1}E, T^{-2}E, \ldots$ are mutually disjoint. For any $x \in E$, we have $T^i x \notin E$ for all $i \geq 1$, hence $x \in D(E)$. Therefore $E \subset D(E)$, and $D(E) \in \mathcal{I}$ by the recurrence property. Consequently $E \in \mathcal{I}$, and $T$ is nondissipative. $\square$
