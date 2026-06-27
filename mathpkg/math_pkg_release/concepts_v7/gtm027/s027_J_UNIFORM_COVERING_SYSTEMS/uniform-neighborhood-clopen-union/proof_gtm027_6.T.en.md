---
role: proof
locale: en
of_concept: uniform-neighborhood-clopen-union
source_book: gtm027
source_chapter: "6"
source_section: "T"
---

# Proof: Uniform Neighborhoods Yield Clopen Unions

Let $(X, \mathfrak{U})$ be a uniform space and let $U \in \mathfrak{U}$ be a symmetric entourage.

For each $A \subset X$, define the iterated $U$-neighborhood:

$$\bigcup_{n \in \omega} U^n[A]$$

where $U^1[A] = U[A] = \{y : (x, y) \in U \text{ for some } x \in A\}$ and inductively $U^{n+1}[A] = U[U^n[A]]$.

Claim: This set is both open and closed.

**Open:** For any $y$ in this union, say $y \in U^n[A]$, we have $U[y] \subset U^{n+1}[A]$, so $y$ is an interior point.

**Closed:** Suppose $z$ is in the closure of $\bigcup_n U^n[A]$. Then $U[z]$ intersects the union, so there exists $n$ with $U[z] \cap U^n[A] \neq \emptyset$. Hence $z \in U[U^n[A]] = U^{n+1}[A]$, so $z$ belongs to the union. Thus the set is also closed.

This is essentially the chain argument of 5.T, showing that the iterated $U$-neighborhood of any set yields a clopen set. The argument applies to any $U \in \mathfrak{U}$.
