---
role: proof
locale: en
of_concept: theorem-23-countable-subset-omega-prime
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 23: Countable Subset of $\Omega'$ has Bounded Supremum

**Theorem 23.** If $A$ is a countable subset of $\Omega'$ and $\Omega \notin A$, then the supremum of $A$ is less than $\Omega$.

*Proof.* Assume that $A$ is a countable subset of $\Omega'$ and that $\Omega \notin A$. For each member $a$ of $A$ the set $\{x : x \leq a\}$ is countable (by property of $\Omega'$ that every proper initial segment is countable) and hence the union of all such sets is countable (by Theorem 17). This union is $\{x : x \leq a \text{ for some } a \text{ in } A\}$, and the supremum $b$ of the union is therefore an upper bound for $A$. The point $b$ has only a countable number of predecessors relative to the ordering, and hence $b \neq \Omega$. It follows that the supremum of $A$ is less than $\Omega$.
