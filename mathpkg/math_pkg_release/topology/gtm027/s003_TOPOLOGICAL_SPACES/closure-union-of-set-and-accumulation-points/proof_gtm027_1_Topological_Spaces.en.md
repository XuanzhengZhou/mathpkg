---
role: proof
locale: en
of_concept: closure-union-of-set-and-accumulation-points
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof that the Closure Equals the Union of a Set and Its Accumulation Points

**Theorem.** For any subset $A$ of a topological space $(X, \mathfrak{J})$, the closure $A^-$ is the union of $A$ and the set $A'$ of all accumulation points of $A$. That is, $A^- = A \cup A'$.

*Proof.* ($A \cup A' \subseteq A^-$) Every accumulation point of $A$ is an accumulation point of each set containing $A$, and is therefore a member of each closed set containing $A$. Since $A^-$ is the intersection of all closed sets containing $A$, every accumulation point of $A$ belongs to $A^-$. Clearly $A \subseteq A^-$ as well. Hence $A \cup A' \subseteq A^-$.

($A^- \subseteq A \cup A'$) By the preceding theorem, the set $A \cup A'$ is closed. Moreover, $A \cup A'$ contains $A$. Since $A^-$ is the *smallest* closed set containing $A$, we must have $A^- \subseteq A \cup A'$.

Combining both inclusions yields $A^- = A \cup A'$. $\square$
