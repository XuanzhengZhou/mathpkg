---
role: proof
locale: en
of_concept: maximal-principle
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 25(a): Maximal Principle

**Maximal Principle (25a).** There is a maximal member of a family $\alpha$ of sets, provided that for each nest in $\alpha$ there is a member of $\alpha$ which contains every member of the nest.

*Proof.* Choose a maximal nest $\pi$ in $\alpha$ which contains the void nest; such exists by the Hausdorff maximal principle (24). By hypothesis, there is a member $A$ of $\alpha$ which contains every member of $\pi$. The set $A$ is a maximal member of $\alpha$, for if there were a member $B$ of $\alpha$ properly containing $A$, then $\pi \cup \{B\}$ would be a nest in $\alpha$ properly containing the maximal nest $\pi$, which is impossible.
