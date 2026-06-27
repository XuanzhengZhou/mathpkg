---
role: proof
locale: en
of_concept: zermelo-postulate
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 25(g): Zermelo Postulate

**Zermelo Postulate (25g).** If $\alpha$ is a disjoint family of non-void sets, then there is a set $C$ such that $A \cap C$ consists of a single point for every $A$ in $\alpha$.

*Proof.* Apply the axiom of choice (25f) to the index set $\alpha$ with $X_A = A$ for each $A$ in $\alpha$. The axiom of choice yields a function $c$ on $\alpha$ such that $c(A) \in A$ for each $A$ in $\alpha$. Let $C$ be the range of $c$. Then for each $A \in \alpha$, $A \cap C$ contains $c(A)$, and since the sets in $\alpha$ are disjoint, $A \cap C$ consists of exactly the single point $c(A)$.
