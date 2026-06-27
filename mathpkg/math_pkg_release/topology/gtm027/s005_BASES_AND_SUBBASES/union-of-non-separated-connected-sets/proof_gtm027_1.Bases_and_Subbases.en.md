---
role: proof
locale: en
of_concept: union-of-non-separated-connected-sets
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Union of Non-Separated Connected Sets is Connected

**Theorem 21.** Let $\alpha$ be a family of connected subsets of a topological space. If no two members of $\alpha$ are separated, then $\bigcup \{A : A \in \alpha\}$ is connected.

**Proof.** Let $C$ be the union of the members of $\alpha$ and suppose that $D$ is both open and closed in $C$ (with the relative topology). For each member $A$ of $\alpha$, the set $A \cap D$ is open and closed in $A$, and since $A$ is connected, either $A \subseteq D$ or $A \subseteq C \setminus D$.

Now suppose, for contradiction, that there exist members $A$ and $B$ of $\alpha$ such that $A \subseteq D$ and $B \subseteq C \setminus D$. Since $D$ is closed in $C$, the closure of $A$ in $C$ is contained in $D$, so $A^{-} \cap B \subseteq D \cap (C \setminus D) = \varnothing$. Similarly, $A \cap B^{-} = \varnothing$ because $C \setminus D$ is also closed in $C$. Thus $A$ and $B$ are separated, contradicting the hypothesis. Therefore all members of $\alpha$ must be contained in the same one of $D$ or $C \setminus D$. Hence either $D = C$ or $D = \varnothing$, which proves that $C$ is connected. $\square$
