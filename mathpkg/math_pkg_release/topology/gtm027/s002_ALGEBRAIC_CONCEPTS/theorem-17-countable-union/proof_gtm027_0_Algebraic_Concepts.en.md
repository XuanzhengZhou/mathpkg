---
role: proof
locale: en
of_concept: theorem-17-countable-union
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 17: Countable Union of Countable Sets

**Theorem 17.** If $\mathfrak{A}$ is a countable family of countable sets, then $\bigcup \{A : A \in \mathfrak{A}\}$ is countable.

*Proof.* Because $\mathfrak{A}$ is countable there is a function $F$ whose domain is a subset of $\omega$ and whose range is $\mathfrak{A}$. Since $F(p)$ is countable for each $p$ in $\omega$, it is possible to find a function $G_p$ on a subset of $\{p\} \times \omega$ whose range is $F(p)$. Consequently there is a function (the union of the functions $G_p$) on a subset of $\omega \times \omega$ whose range is $\bigcup \{A : A \in \mathfrak{A}\}$, and the problem reduces to showing that $\omega \times \omega$ is countable.

The key to this proof is the observation that, if we think of $\omega \times \omega$ as lying in the upper right-hand part of the plane, the diagonals which cross from upper left to lower right contain only a finite number of members of $\omega \times \omega$. Explicitly, for $n$ in $\omega$, let $B_n = \{(p, q) : (p, q) \in \omega \times \omega \text{ and } p + q = n\}$. Then $B_n$ contains precisely $n + 1$ points, and the union $\bigcup \{B_n : n \in \omega\}$ is $\omega \times \omega$. Each $B_n$ is finite and hence countable; the union of countably many finite sets is countable. Therefore $\omega \times \omega$ is countable, and the result follows.
