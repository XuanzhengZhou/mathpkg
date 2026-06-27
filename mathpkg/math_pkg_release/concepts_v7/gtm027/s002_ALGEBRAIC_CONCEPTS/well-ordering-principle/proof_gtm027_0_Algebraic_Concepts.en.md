---
role: proof
locale: en
of_concept: well-ordering-principle
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 25(h): Well-Ordering Principle

**Well-Ordering Principle (25h).** Each set can be well ordered.

*Proof.* Suppose that $X$ is the (non-void) set which is to be well ordered. Let $\mathfrak{A}$ be the family of all non-void subsets of $X$, and let $c$ be a choice function for $\mathfrak{A}$; that is, $c$ is a function on $\mathfrak{A}$ such that $c(A) \in A$ for each $A$ in $\mathfrak{A}$. The idea of the proof is to construct an ordering $\leq$ such that for each "initial segment" $A$ the first point which follows $A$ in the ordering is $c(X \setminus A)$.

Define a set $A$ to be a segment relative to an order $<$ iff each point which precedes a member of $A$ is itself a member of $A$. In particular the void set is a segment. Let $\mathfrak{C}$ be the class of all reflexive linear orderings $\leq$ which satisfy the conditions: the domain $D$ of $\leq$ is a subset of $X$, and for each segment $A$ other than $D$, the first point of $D \setminus A$ is $c(X \setminus A)$. It is almost evident that each member of $\mathfrak{C}$ is a well ordering, for if $B$ is a non-void subset of the domain of a member $\leq$ and $A = \{y : y \leq x \text{ and } y \neq x \text{ for each } x \text{ in } B\}$, then $c(X \setminus A)$ is the first member of $B$.

Suppose that $\leq_1$ and $\leq_2$ are members of $\mathfrak{C}$, that $D$ is the domain of $\leq_1$, and that $E$ is the domain of $\leq_2$. Let $A$ be the set of all points $x$ such that the sets $\{y : y \leq_1 x\}$ and $\{y : y \leq_2 x\}$ are identical and such that on these sets the two orderings agree. Then $A$ is a segment relative to both $\leq_1$ and $\leq_2$. If $A$ is not identical with either $D$ or $E$, then $c(X \setminus A)$ is the first point of each of $D \setminus A$ and $E \setminus A$, and it follows that the two orderings agree on $A \cup \{c(X \setminus A)\}$. From this it can be shown that one of $\leq_1$ and $\leq_2$ is an extension of the other. Taking the union of all members of $\mathfrak{C}$ yields a well ordering whose domain is $X$, completing the proof.

This derivation of the well ordering principle from the choice axiom is essentially that of Zermelo. It may be noted that the union of a nest of well orderings is generally not a well ordering, so that a direct application of the maximal principle to the family of well orderings is impossible.
