---
role: proof
locale: en
of_concept: zorn-lemma
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 25(e): Zorn Lemma

**Zorn Lemma (25e).** If each chain in a partially ordered set has an upper bound, then there is a maximal element of the set.

*Proof.* By the Kuratowski lemma (25d), there exists a maximal chain $C$ in the partially ordered set $A$. By hypothesis, $C$ has an upper bound $x$. The element $x$ is a maximal element of $A$, for if there were $y \in A$ with $x < y$, then $C \cup \{y\}$ would be a chain properly containing the maximal chain $C$, which is impossible.
