---
role: proof
locale: en
of_concept: filter-extension-with-set
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

This follows from Proposition 26.29 by taking $K = F \cup \{Z\}$. If $X \in \mathcal{F}_g(F \cup \{Z\})$, then by 26.29 there exist $m \in \omega \setminus \{0\}$ and sets $Y_0, \ldots, Y_{m-1} \in F \cup \{Z\}$ such that $Y_0 \cap \cdots \cap Y_{m-1} \subseteq X$. Let $Y$ be the intersection of those $Y_i$ that belong to $F$. Then $Y \in F$ (since $F$ is a filter) and $Y \cap Z \subseteq X$ (since any $Y_i = Z$ contributes $Z$ to the intersection, and $Y \cap Z$ is contained in the full intersection). Conversely, if $Y \in F$ and $Y \cap Z \subseteq X$, then by taking $m = 2$, $Y_0 = Y$, $Y_1 = Z$ in Proposition 26.29, we get $X \in \mathcal{F}_g(F \cup \{Z\})$.
