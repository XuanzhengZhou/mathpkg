---
role: proof
locale: en
of_concept: kuratowski-lemma
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 25(d): Kuratowski Lemma

**Kuratowski Lemma (25d).** Each chain in a (partially) ordered set is contained in a maximal chain.

*Proof.* Suppose $B$ is a chain in the partially ordered set $A$. Let $\alpha$ be the family of all chains in $A$ which contain $B$. If $\pi$ is a nest in $\alpha$, then it can be directly verified that $\bigcup \{N : N \in \pi\}$ is again a member of $\alpha$ (a chain containing $B$), so that $\alpha$ satisfies the hypothesis of (25a) and consequently has a maximal member, which is a maximal chain containing $B$.
