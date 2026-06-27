---
role: proof
locale: en
of_concept: uncountable-well-ordered-set
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Summary 22: Uncountable Well-Ordered Set $\Omega'$

**Summary 22.** There is an uncountable set $\Omega'$, which is linearly ordered by a relation $<$ in such a way that:

(a) Every non-void subset of $\Omega'$ has a first element (a least member);
(b) $\Omega'$ is uncountable;
(c) Every proper initial segment of $\Omega'$ is countable;
(d) $\Omega'$ has a greatest element, denoted $\Omega$;
(e) Every element of $\Omega'$ has an immediate successor.

Thus $\Omega'$ is a well-ordered set whose proper initial segments are all countable, while $\Omega'$ itself is uncountable.

*Proof.* The construction of $\Omega'$ and the verification of its properties are carried out in the Appendix (on ordinal numbers). In particular:

- The existence of an uncountable well-ordered set follows from the well-ordering principle (Theorem 25h), which guarantees that any set can be well ordered. Starting from an uncountable set (e.g., given by Cantor's theorem), one obtains an uncountable well-ordered set.
- By standard ordinal theory, there exists a smallest uncountable ordinal, which is precisely $\Omega'$.
- Property (a) holds by definition of a well ordering.
- Property (b) holds because $\Omega'$ was chosen to be uncountable.
- Property (c) holds because $\Omega'$ is the *smallest* uncountable well-ordered set; any proper initial segment corresponds to a smaller ordinal and must therefore be countable.
- Property (d) holds because one can adjoin a greatest element $\Omega$ to $\Omega'$ while preserving the well-ordering (if $\Omega'$ does not already have one).
- Property (e) holds for all elements of a well-ordered set except possibly the greatest element; for $\Omega'$, each element other than $\Omega$ has an immediate successor.

The first non-finite ordinal, denoted $\omega$, is the first member of $\Omega'$ which does not have a finite number of predecessors. In the construction of the ordinal numbers it turns out that $\omega$ is, in fact, the set of non-negative integers.
