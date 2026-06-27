---
role: proof
locale: en
of_concept: union-of-set-and-accumulation-points-closed
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof that the Union of a Set and Its Accumulation Points Is Closed

**Theorem.** For any subset $A$ of a topological space, the union $A \cup A'$ (where $A'$ denotes the set of accumulation points of $A$) is closed.

*Proof.* Let $x \notin A \cup A'$. Then $x \notin A$ and $x$ is not an accumulation point of $A$. Hence there exists a neighborhood $U$ of $x$ such that $U \cap A = \emptyset$ (since $x \notin A$, the condition $U \cap A \subseteq \{x\}$ for non-accumulation points reduces to $U \cap A = \emptyset$). We may assume $U$ is open.

Now we claim that no point of $U$ is an accumulation point of $A$. Indeed, if $y \in U$ were an accumulation point of $A$, then every neighborhood of $y$ would intersect $A$. But $U$ is an open neighborhood of $y$ that is disjoint from $A$, a contradiction. Hence $U \cap A' = \emptyset$.

Therefore $U \subseteq X \setminus (A \cup A')$. This shows that every point of the complement of $A \cup A'$ has an open neighborhood contained in that complement. Hence $X \setminus (A \cup A')$ is open, so $A \cup A'$ is closed. $\square$
