---
role: proof
locale: en
of_concept: closed-open-in-union-of-separated-sets
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Closed and Open Sets in a Union of Separated Complements

**Corollary 19.** Let $X$ be a topological space which is the union of subsets $Y$ and $Z$ such that $Y \sim Z$ and $Z \sim Y$ are separated. Then a subset $A$ of $X$ is closed (open) if $A \cap Y$ is closed (open) in $Y$ and $A \cap Z$ is closed (open) in $Z$.

**Proof.** If $A \cap Y$ and $A \cap Z$ are closed in $Y$ and $Z$ respectively, then, by the preceding theorem, $A^- = [(A \cap Y)^- \cap Y] \cup [(A \cap Z)^- \cap Z] = (A \cap Y) \cup (A \cap Z) = A$. Hence $A$ is closed in $X$.

For the open case, suppose $A \cap Y$ and $A \cap Z$ are open in $Y$ and $Z$ respectively. Then $Y \sim (A \cap Y) = (X \sim A) \cap Y$ is closed in $Y$, and similarly $(X \sim A) \cap Z$ is closed in $Z$. By the closed case just proved, $X \sim A$ is closed in $X$, so $A$ is open in $X$. $\square$