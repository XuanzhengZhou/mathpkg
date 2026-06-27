---
role: proof
locale: en
of_concept: irreducible-decomposition
source_book: gtm052
source_chapter: "I"
source_section: "1"
---

First we show existence. Let $\mathscr{S}$ be the set of nonempty closed subsets of $X$ which cannot be written as a finite union of irreducible closed subsets. If $\mathscr{S}$ is nonempty, then by the descending chain condition (noetherian property), $\mathscr{S}$ has a minimal element $Y$. Since $Y \in \mathscr{S}$, $Y$ is not irreducible, so $Y = Y_1 \cup Y_2$ where $Y_1, Y_2$ are proper closed subsets of $Y$. By minimality of $Y$, both $Y_1$ and $Y_2$ can be written as finite unions of irreducible closed subsets. But then $Y$ itself is such a union, contradiction. Hence $\mathscr{S}$ is empty.

For uniqueness, suppose $Y = Y_1 \cup \ldots \cup Y_r = Y_1' \cup \ldots \cup Y_s'$ are two representations with $Y_i \nsubseteq Y_j$ and $Y_i' \nsubseteq Y_j'$ for $i \neq j$. Then $Y_1 = \bigcup_j (Y_1 \cap Y_j')$. Since $Y_1$ is irreducible, $Y_1 = Y_1 \cap Y_j'$ for some $j$, i.e., $Y_1 \subseteq Y_j'$. By symmetry, $Y_j' \subseteq Y_i$ for some $i$, so $Y_1 \subseteq Y_i$, forcing $i = 1$ by the maximality condition and thus $Y_1 = Y_j'$. Continuing this argument yields $r = s$ and the sets are the same up to reordering.
