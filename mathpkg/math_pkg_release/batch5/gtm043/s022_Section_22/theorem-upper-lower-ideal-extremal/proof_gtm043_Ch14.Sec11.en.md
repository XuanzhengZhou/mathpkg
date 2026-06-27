---
role: proof
locale: en
of_concept: theorem-upper-lower-ideal-extremal
source_book: gtm043
source_chapter: "14"
source_section: "11"
---

The assertion about the lower ideal follows from the definition (the immediate successor is the smallest).

Let $I$ be an immediate predecessor of an upper ideal $J$; we prove $I$ contains every predecessor $H$ of $J$. Let $\mathfrak{J}$ be a maximal chain containing $I$ (and $J$), and $\mathfrak{H}$ a maximal chain containing $H$ (and $J$). Then $I$ is the immediate predecessor of $J$ in $\mathfrak{J}$.

By Theorem 14.9, $\mathfrak{J} \cap \mathfrak{H}$ has a smallest member $P$, which is a $z$-ideal. Obviously $P \subset J$. By Lemma 14.8, $P$ is not the upper ideal $J$. Therefore $P \subset I$.

Now in chain $\mathfrak{H}$, either $H \subset P$ or $P \subset H$. In the first case, $H \subset I$. If $P \subset H$, then $H$ belongs to $\mathfrak{J}$; since $H \neq J$, this implies $H \subset I$.
