---
role: proof
locale: en
of_concept: unique-representation-delta
source_book: gtm005
source_chapter: "VII"
source_section: "5"
---

Consider the functor $U: \mathbf{Mon} \to \mathbf{Set}$ sending a monoid to its underlying set. A representation $(F, u)$ of $U$ consists of a monoid $F$ and $u \in U(F)$ such that for every monoid $M$ and $x \in M$, there exists a unique monoid homomorphism $\hat{x}: F \to M$ with $\hat{x}(u) = x$.

The free monoid on one generator $\mathbb{N}$ (under addition) with $u = 1$ is a representation: any $x \in M$ gives a unique homomorphism $\mathbb{N} \to M$ sending $n \mapsto x^n$. For the category $\mathbf{Mon}_{\mathrm{fin}}$ of finite monoids, this fails since $\mathbb{N}$ is infinite, so $U$ restricted to finite monoids is not representable.

Uniqueness of representation: by the Yoneda Lemma, the representing object is unique up to unique isomorphism (with isomorphism preserving the universal element).
