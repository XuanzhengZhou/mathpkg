---
role: proof
locale: en
of_concept: theorem-16-countable-range
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 16: Image of a Countable Set is Countable

**Theorem 16.** If the domain of a function is countable, then the range is also countable.

*Proof.* It is sufficient to show that, if $A$ is a subset of $\omega$ and $f$ is a function on $A$ onto $B$, then $B$ is countable. Let $C$ be the set of all members $x$ of $A$ such that, if $y \in A$ and $y < x$, then $f(x) \neq f(y)$; that is, $C$ consists of the smallest member of each of the sets $f^{-1}[y]$ for $y$ in $B$. Then $f \mid C$ maps $C$ onto $B$ in a one-to-one fashion, and since $C$ is countable by Theorem 15, so is $B$.
