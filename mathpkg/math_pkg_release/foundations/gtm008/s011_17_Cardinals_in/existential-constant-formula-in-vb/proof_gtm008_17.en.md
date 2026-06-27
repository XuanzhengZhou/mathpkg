---
role: proof
locale: en
of_concept: existential-constant-formula-in-vb
source_book: gtm008
source_chapter: "17"
source_section: "Cardinals in V^{(B)}"
---

This corollary follows from Theorem 17.8 in the same manner that Corollary 13.23 was derived from Theorem 13.22.

Theorem 17.8 establishes the representation of $[Const(u)]$ as $\sum_{x \in L} [u = \check{x}]$, where $L$ is the constructible universe. Then:

$$
[(\exists u)[Const(u) \land \varphi(u)]] = \sum_{u \in V^{(B)}} [Const(u)] \cdot [\varphi(u)]
$$

$$
= \sum_{u \in V^{(B)}} \sum_{x \in L} [u = \check{x}] \cdot [\varphi(u)]
$$

$$
= \sum_{x \in L} \sum_{u \in V^{(B)}} [u = \check{x}] \cdot [\varphi(u)]
$$

$$
= \sum_{x \in L} [\varphi(\check{x})].
$$

The last equality follows from the equality axioms for $V^{(B)}$, which give $[u = \check{x}] \cdot [\varphi(u)] \leq [\varphi(\check{x})]$ and the fact that $[\check{x} = \check{x}] = 1$.
