---
role: proof
locale: en
of_concept: primary-representation-under-extension
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

Since extension commutes with finite intersections, we have
$$\mathfrak{a}^e = \left(\bigcap_{i=1}^{n} \mathfrak{q}_i\right)^e = \bigcap_{i=1}^{n} \mathfrak{q}_i^e.$$

For $r+1 \leq i \leq n$, we have $\mathfrak{q}_i \cap M \neq \emptyset$, so by Theorem 15(b) (or Corollary 2 to Theorem 15), $\mathfrak{q}_i^e = R_M$. Thus these components contribute nothing to the intersection, and
$$\mathfrak{a}^e = \bigcap_{i=1}^{r} \mathfrak{q}_i^e.$$

For $1 \leq i \leq r$, we have $\mathfrak{q}_i \cap M = \emptyset$, and by Theorem 16(b), each $\mathfrak{q}_i^e$ is primary in $R_M$ with radical $\mathfrak{p}_i^e$, where $\mathfrak{p}_i$ is the radical of $\mathfrak{q}_i$. Moreover, the irredundance of the original representation implies that no $\mathfrak{q}_i^e$ ($1 \leq i \leq r$) contains the intersection of the others. For if $\mathfrak{q}_i^e \supset \bigcap_{j \neq i} \mathfrak{q}_j^e$, then contracting would give $\mathfrak{q}_i \supset \bigcap_{j \neq i} \mathfrak{q}_j$ (since the $\mathfrak{q}_i$ are contracted for $i \leq r$ by Theorem 16(a)), contradicting irredundance. Thus the representation $\mathfrak{a}^e = \bigcap_{i=1}^{r} \mathfrak{q}_i^e$ is irredundant.
