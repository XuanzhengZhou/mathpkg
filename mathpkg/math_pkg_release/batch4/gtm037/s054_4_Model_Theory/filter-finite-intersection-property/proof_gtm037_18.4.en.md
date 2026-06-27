---
role: proof
locale: en
of_concept: filter-finite-intersection-property
source_book: gtm037
source_chapter: "18"
source_section: "4"
---

The proposition is obvious from the definition of a filter. (i) If $\emptyset \notin F$, then for any $a, b \in F$, we have $a \cap b \in F$ since $F$ is closed under finite intersections, and $a \cap b \neq \emptyset$ because otherwise $\emptyset \in F$, contradiction. By induction, any finite intersection of members of $F$ is nonempty, so $F$ has the finite intersection property. (ii) $I \in F$ follows from the fact that $F$ is nonempty and closed under supersets: take any $a \in F$, then $a \subseteq I$, so $I \in F$. (iii) If $\emptyset \in F$, then for any $b \subseteq I$, we have $\emptyset \subseteq b$, so $b \in F$ by upward closure, hence $F = \mathcal{P}(I)$. Conversely, if $F = \mathcal{P}(I)$, then trivially $\emptyset \in F$.
