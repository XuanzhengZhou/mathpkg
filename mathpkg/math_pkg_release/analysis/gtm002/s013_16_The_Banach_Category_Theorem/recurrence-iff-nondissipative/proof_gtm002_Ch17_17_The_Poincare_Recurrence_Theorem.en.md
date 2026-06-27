---
role: proof
locale: en
of_concept: recurrence-iff-nondissipative
source_book: gtm002
source_chapter: "17"
source_section: "17. The Poincare Recurrence Theorem"
---

Suppose $T$ is nondissipative. Consider any $E \in \mathcal{S}$, and let $F = E - \bigcup_{k=1}^{\infty} T^{-k}E$. Since $T$ is $\mathcal{S}$-measurable and $\mathcal{S}$ is a $\sigma$-ring, $F$ belongs to $\mathcal{S}$. The set $F$ is wandering: for $i < j$, $T^{-i}F \cap T^{-j}F = \emptyset$ by construction. Since $T$ is nondissipative, $F \in \mathcal{I}$. The set $D(E)$ can be expressed as $D(E) = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} (E - T^{-k}E)$, which is contained in a countable union of wandering sets, hence $D(E) \in \mathcal{I}$.

Conversely, if $T$ has the recurrence property and $E$ is a wandering set in $\mathcal{S}$, then $D(E) = E$ (no point of a wandering set can return to $E$ infinitely often), so $E \in \mathcal{I}$. Thus $T$ is nondissipative.

