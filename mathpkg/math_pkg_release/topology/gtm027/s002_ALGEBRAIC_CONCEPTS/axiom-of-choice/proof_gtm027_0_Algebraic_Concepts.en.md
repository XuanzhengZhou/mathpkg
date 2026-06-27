---
role: proof
locale: en
of_concept: axiom-of-choice
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 25(f): Axiom of Choice

**Axiom of Choice (25f).** If $X_a$ is a non-void set for each member $a$ of an index set $A$, then there is a function $c$ on $A$ such that $c(a) \in X_a$ for each $a$ in $A$.

*Proof.* Recall that a function is a set of ordered pairs such that no two members have the same first coordinate. Let $\mathfrak{F}$ be the family of all functions $f$ such that the domain of $f$ is a subset of $A$ and $f(a) \in X_a$ for each $a$ in the domain of $f$. (The members of $\mathfrak{F}$ are "fragments" of the function we seek.) The following argument shows that $\mathfrak{F}$ is a family of finite character. If $f$ is a member of $\mathfrak{F}$, then every subset of $f$, and in particular every finite subset, is also a member of $\mathfrak{F}$. On the other hand, if $f$ is a set, each finite subset of which belongs to $\mathfrak{F}$, then $f$ is a function (since no two pairs in $f$ can have the same first coordinate, otherwise a finite subset would violate this), its domain is a subset of $A$, and $f(a) \in X_a$ for each $a$ in the domain. Hence $f \in \mathfrak{F}$. By the Tukey lemma (25c), $\mathfrak{F}$ has a maximal member $c$. If the domain of $c$ is not all of $A$, say $a \in A$ is not in the domain, then choosing any $x \in X_a$, we could extend $c$ to $c \cup \{(a, x)\}$, which is a member of $\mathfrak{F}$ properly containing $c$, contradicting maximality. Hence the domain of $c$ is $A$ and $c$ is the required choice function.
