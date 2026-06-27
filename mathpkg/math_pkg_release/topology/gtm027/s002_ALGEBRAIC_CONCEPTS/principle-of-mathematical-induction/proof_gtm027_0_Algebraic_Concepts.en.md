---
role: proof
locale: en
of_concept: principle-of-mathematical-induction
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of the Principle of Mathematical Induction

**Principle of Mathematical Induction.** Each inductive subset of $\omega$ is identical with $\omega$.

*Proof.* Recall that an inductive set is a set $A$ of real numbers such that $0 \in A$, and whenever $x \in A$, then $x + 1 \in A$. The set $\omega$ of non-negative integers is defined to be the intersection of the members of the family of all inductive sets. In other words, a real number $x$ is a non-negative integer iff $x$ belongs to every inductive set.

It is evident that $\omega$ is itself an inductive set (since $0$ belongs to every inductive set, and if $x$ belongs to every inductive set then $x+1$ also belongs to every inductive set). Moreover, $\omega$ is a subset of every inductive set by definition. It follows that if $A$ is an inductive subset of $\omega$, then $\omega \subset A \subset \omega$, hence $A = \omega$. Thus each inductive subset of $\omega$ is identical with $\omega$. A proof which relies on this principle is called a proof by induction.
