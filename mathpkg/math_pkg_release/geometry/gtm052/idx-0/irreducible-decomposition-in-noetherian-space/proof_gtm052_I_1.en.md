---
role: proof
locale: en
of_concept: irreducible-decomposition-in-noetherian-space
source_book: gtm052
source_chapter: "I"
source_section: "§1"
---
First we show the existence of such a representation. Let $\mathfrak{S}$ be the set of nonempty closed subsets of $X$ which cannot be written as a finite union of irreducible closed subsets. If $\mathfrak{S}$ is nonempty, then by the descending chain condition it has a minimal element $Z$. Since $Z \in \mathfrak{S}$, $Z$ is not irreducible, so $Z = Z_1 \cup Z_2$ with $Z_1, Z_2$ proper closed subsets of $Z$. By minimality of $Z$, both $Z_1$ and $Z_2$ can be written as finite unions of irreducible closed subsets, hence $Z$ can also, contradiction. Thus $\mathfrak{S}$ is empty.

For uniqueness, suppose $Y = Y_1 \cup \ldots \cup Y_r = Y'_1 \cup \ldots \cup Y'_s$ with no inclusions among the $Y_i$ or among the $Y'_j$. For each $i$, $Y_i = \bigcup_j (Y_i \cap Y'_j)$, so since $Y_i$ is irreducible, $Y_i \subseteq Y'_j$ for some $j$. Similarly $Y'_j \subseteq Y_k$ for some $k$, hence $Y_i = Y'_j = Y_k$, forcing $r = s$ and $\{Y_i\} = \{Y'_j\}$ as sets.
