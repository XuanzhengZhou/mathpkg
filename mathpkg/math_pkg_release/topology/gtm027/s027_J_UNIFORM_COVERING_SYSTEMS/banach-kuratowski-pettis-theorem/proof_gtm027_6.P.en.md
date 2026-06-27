---
role: proof
locale: en
of_concept: banach-kuratowski-pettis-theorem
source_book: gtm027
source_chapter: "6"
source_section: "P"
---

# Proof of the Banach-Kuratowski-Pettis Theorem

Assume $A$ contains a non-meager almost open subset of a topological group $X$ (so in particular $X$ itself is non-meager, and each non-void open subset of $X$ is non-meager).

For each almost open subset $B$ of $X$, define $B^*$ to be the union of all open sets $U$ such that $U \setminus B$ is meager. Equivalently, $B^* = \operatorname{int}(B \cup M)^c$ for some maximal meager $M$; it is the "regular open core modulo meager sets."

Key properties for almost open $B, C$:
- $(xB)^* = xB^*$ (translation invariance);
- $(B \cap C)^* = B^* \cap C^*$;
- If $B^*$ is non-void then $B$ is non-meager.

Now consider $A^*$. Since $A$ is non-meager, $A^*$ is non-void. Note that

$$A^*(A^*)^{-1} = \{x \in G : xA^* \cap A^* \neq \emptyset\}.$$

If $x \in A^*(A^*)^{-1}$, then $xA^* \cap A^* \neq \emptyset$, hence

$$(xA \cap A)^* = (xA)^* \cap A^* = xA^* \cap A^* \neq \emptyset,$$

which implies $xA \cap A \neq \emptyset$, so $x \in AA^{-1}$. Therefore

$$A^*(A^*)^{-1} \subset AA^{-1}.$$

But $A^*$ is a non-void open set (by definition). In a topological group, the product of a non-void open set with its inverse contains a neighborhood of the identity. Hence $AA^{-1}$ is a neighborhood of $e$.
