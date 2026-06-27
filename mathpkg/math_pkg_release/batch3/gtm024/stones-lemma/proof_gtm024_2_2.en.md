---
role: proof
locale: en
of_concept: stones-lemma
source_book: gtm024
source_chapter: "§2"
source_section: "2.B"
---

Let $\mathcal{C}$ be the class of all convex sets in $X$ disjoint from $B$ and containing $A$. Partially order $\mathcal{C}$ by inclusion and apply Zorn's lemma to obtain a maximal element $C \in \mathcal{C}$. Set $D = X \setminus C$. If $D$ were not convex, there would exist $x, z \in D$ and $v \in (x, z) \cap C$. By maximality of $C$, both $C \cup \{x\}$ and $C \cup \{z\}$ would intersect $B$, leading via convexity to the contradiction $B \cap C \neq \emptyset$.