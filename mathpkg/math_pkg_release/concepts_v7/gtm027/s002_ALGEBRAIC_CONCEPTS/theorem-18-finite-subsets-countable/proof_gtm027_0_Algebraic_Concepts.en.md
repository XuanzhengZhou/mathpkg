---
role: proof
locale: en
of_concept: theorem-18-finite-subsets-countable
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 18: Finite Subsets Countable, Power Set Uncountable

**Theorem 18.** The family of all finite subsets of a countably infinite set is countable, but the family of all subsets is not.

*Proof.* In view of the remarks preceding the statement of the theorem it is sufficient to show that the set $F$ of all dyadic expansions $a$ with $a_p = 0$ for $p$ negative is uncountable, and that the subset $G$ of $F$ consisting of rational expansions is countable.

Suppose that $f$ is a one-to-one function on $\omega$ with range $F$. Let $a$ be the member of $F$ such that $a_p = 1 - f(p)_p$ for each non-negative integer $p$. That is, the $p$-th digit of $a$ is one minus the $p$-th digit of $f(p)$. Then $a \in F$ and clearly, for each $p$ in $\omega$, $a \neq f(p)$ because $a$ and $f(p)$ differ in the $p$-th digit. It follows that $a$ does not belong to the range of $f$, and this is a contradiction. Hence $F$ is uncountable.

It remains to be proved that $G$ is countable. For $p$ in $\omega$ let $G_p = \{a : a \in G \text{ and } a_q = 0 \text{ for } q > p\}$. Then $G_0$ contains just two elements, and since there are precisely twice as many members in $G_{p+1}$ as in $G_p$, it follows that $G_p$ is always finite. Hence $G = \bigcup \{G_p : p \in \omega\}$ is countable.
