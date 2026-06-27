---
role: proof
locale: en
of_concept: closure-in-union-of-separated-sets
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Closure Decomposition for a Union of Separated Complements

**Theorem 18.** Let $X$ be a topological space which is the union of subsets $Y$ and $Z$ such that $Y \sim Z$ and $Z \sim Y$ are separated. Then the closure of a subset $A$ of $X$ is the union of the closure in $Y$ of $A \cap Y$ and the closure in $Z$ of $A \cap Z$.

**Proof.** The closure of a union of two sets is the union of the closures, and hence

$$A^- = (A \cap Y)^- \cup (A \cap (Z \sim Y))^-.$$

Consequently,

$$A^- \cap Y = [(A \cap Y)^- \cap Y] \cup [(A \cap (Z \sim Y))^- \cap Y].$$

The set $(Z \sim Y)^-$ is disjoint from $Y \sim Z$ (since $Z \sim Y$ and $Y \sim Z$ are separated), hence $(Z \sim Y)^- \subset Z$, and it follows that $(A \cap (Z \sim Y))^- \subset (A \cap Z)^- \cap Z$, so $(A \cap (Z \sim Y))^- \cap Y \subset (A \cap Z)^- \cap Z \cap Y = \emptyset$.

Thus $A^- \cap Y = (A \cap Y)^- \cap Y$. Similarly, $A^- \cap Z$ is the union of $(A \cap Z)^- \cap Z$ and a subset of $(A \cap Y)^- \cap Y$ which is disjoint from $Z$, so $A^- \cap Z = (A \cap Z)^- \cap Z$. Consequently,

$$A^- = (A^- \cap Y) \cup (A^- \cap Z) = [(A \cap Y)^- \cap Y] \cup [(A \cap Z)^- \cap Z],$$

and the theorem is proved. $\square$