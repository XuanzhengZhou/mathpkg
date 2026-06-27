---
role: proof
locale: en
of_concept: uncountable-subsets-second-countable
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Uncountable Subsets in Second Countable Spaces Have Accumulation Points

**Theorem 13.** If $A$ is an uncountable subset of a space whose topology has a countable base, then some point of $A$ is an accumulation point of $A$.

**Proof.** Suppose that no point of $A$ is an accumulation point of $A$. Then for each $x \in A$ there exists an open neighborhood $U_x$ of $x$ such that $U_x \cap A = \{x\}$. Let $\mathcal{B}$ be a countable base for the topology. For each $x \in A$, since $U_x$ is open, there exists a member $B_x \in \mathcal{B}$ such that $x \in B_x \subset U_x$. Then $B_x \cap A = \{x\}$.

The mapping $x \mapsto B_x$ from $A$ to $\mathcal{B}$ is injective: if $x 
eq y$ and $B_x = B_y$, then $B_x \cap A$ would contain both $x$ and $y$, contradicting $B_x \cap A = \{x\}$. But $\mathcal{B}$ is countable while $A$ is uncountable, so no such injection exists. This contradiction shows that some point of $A$ must be an accumulation point of $A$. $\square$