---
role: proof
locale: en
of_concept: open-measure-zero-covering-by-base
source_book: gtm002
source_chapter: "16"
source_section: "The Banach Category Theorem"
---

Let $\mathcal{B}_0$ be the family of all members of a given base for $X$ that are contained in some member of $\mathcal{G}$. For each $B \in \mathcal{B}_0$, select a $G_B \in \mathcal{G}$ with $B \subset G_B$. Since each $G_B$ has measure zero, $\mu(B) = 0$ for all $B \in \mathcal{B}_0$.

The union $\bigcup \mathcal{B}_0$ is contained in $\bigcup \mathcal{G}$, and the difference $\bigcup \mathcal{G} - \bigcup \mathcal{B}_0$ is disjoint from every basic open set contained in a member of $\mathcal{G}$, hence has measure zero. Therefore $\mu(\bigcup \mathcal{G}) = \mu(\bigcup \mathcal{B}_0)$.

Applying Theorem 16.3 to the family $\mathcal{B}_0$ (whose cardinality is at most that of the base), we obtain $\mu(\bigcup \mathcal{B}_0) = 0$, provided the base has cardinality of measure zero. $\square$
