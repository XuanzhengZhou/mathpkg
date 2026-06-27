---
role: proof
locale: en
of_concept: second-countable-implies-separable
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Second Countable Spaces are Separable

**Theorem 14.** A space whose topology has a countable base is separable.

**Proof.** Choose a point out of each non-void member of the base, thus obtaining a countable set $A$. (Since the base is countable, $A$ is countable.) Let $U = X \sim A^-$ be the complement of the closure of $A$. Then $U$ is an open set. If $U$ were non-void, then $U$ would contain some non-void member $B$ of the base (since every open set is a union of basic open sets). But $B \cap A 
eq \emptyset$ by construction (we chose a point from each non-void basic open set), while $B \subset U \subset X \sim A^-$ implies $B \cap A = \emptyset$. This contradiction shows that $U = \emptyset$, i.e., $A^- = X$. Hence $A$ is a countable dense subset and the space is separable. $\square$