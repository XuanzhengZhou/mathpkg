---
role: proof
locale: en
of_concept: theorem-15-countable-subset
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 15: Subset of a Countable Set is Countable

**Theorem 15.** A subset of a countable set is countable.

*Proof.* Suppose $A$ is countable, $f$ is one-to-one on $\omega$ with range $A$, and that $B \subset A$. Then $f$, restricted to $f^{-1}[B]$, is a one-to-one function on a subset of $\omega$ with range $B$, and if it can be shown that $f^{-1}[B]$ is countable, then a one-to-one function onto $B$ can be constructed by composition. The proof therefore reduces to showing that an arbitrary subset $C$ of $\omega$ is countable.

To show this, let $C$ be an arbitrary subset of $\omega$. Define a function $g$ on $C$ by induction (or simply enumerate the elements of $C$ in increasing order): let $g(0)$ be the smallest element of $C$, and having defined $g(0), \ldots, g(n)$, let $g(n+1)$ be the smallest element of $C$ greater than $g(n)$, if such exists. If $C$ is finite, this process terminates after finitely many steps; if $C$ is infinite, it produces a one-to-one function from $\omega$ onto $C$. In either case, $C$ is countable. Hence $f^{-1}[B]$ is countable and $B$ is countable.
