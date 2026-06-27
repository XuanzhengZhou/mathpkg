---
role: proof
locale: en
of_concept: union-of-finite-sets
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Union of Finite Sets

**Theorem.** If $x$ is finite and each member of $x$ is finite, then $\bigcup x$ is finite.

*Proof.* (From the text following Theorem 167.) Proceed by induction on $P(x)$. Let $s$ be the set of all integers $u$ such that, if $P(x) = u$ and each member of $x$ is finite, then $\bigcup x$ is finite. Clearly $0 \in s$ (the void class has void union, which is finite). If $u \in s$, $P(x) = u + 1$, and each member of $x$ is finite, then split $x$ into two subsets: one of power $u$ and a singleton $\{y\}$. By the induction hypothesis, the union of the subset of power $u$ is finite, and $y$ is finite. The union of two finite sets is finite, hence $\bigcup x$ is finite. Therefore $s = \omega$ by mathematical induction (Theorem 137).
