---
role: proof
locale: en
of_concept: primary-ideal-criterion
source_book: gtm028
source_chapter: "III"
source_section: "§9"
---

Assume (a), (b), and (c). That $\mathfrak{Q}$ is primary follows from (c) and (b). From (b) we conclude that $\mathfrak{P} \subseteq \sqrt{\mathfrak{Q}}$. To show $\sqrt{\mathfrak{Q}} \subseteq \mathfrak{P}$, suppose $b \in \sqrt{\mathfrak{Q}}$, so that $b^m \in \mathfrak{Q}$; let $m$ be the least exponent such that $b^m \in \mathfrak{Q}$. If $m = 1$, this gives $b \in \mathfrak{Q} \subseteq \mathfrak{P}$; and if $m > 1$, then $b^{m-1} \cdot b = b^m \in \mathfrak{Q}$ and $b^{m-1} \notin \mathfrak{Q}$ (by minimality of $m$), so by (c), $b \in \mathfrak{P}$. Thus $\sqrt{\mathfrak{Q}} = \mathfrak{P}$.

Conversely, assume $\mathfrak{Q}$ is primary and $\mathfrak{P} = \sqrt{\mathfrak{Q}}$. Then (a) holds since $\mathfrak{Q} \subseteq \sqrt{\mathfrak{Q}} = \mathfrak{P}$. (b) holds since $\mathfrak{P} = \sqrt{\mathfrak{Q}}$ means every element of $\mathfrak{P}$ has some power in $\mathfrak{Q}$. For (c), if $ab \in \mathfrak{Q}$ and $a \notin \mathfrak{Q}$, then by the definition of primary, $b^m \in \mathfrak{Q}$ for some $m$, hence $b \in \sqrt{\mathfrak{Q}} = \mathfrak{P}$.
