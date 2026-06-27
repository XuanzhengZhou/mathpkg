---
role: proof
locale: en
of_concept: closure-via-neighborhoods
source_book: gtm015
source_chapter: "5"
source_section: "Uniformity in topological groups"
---

# Proof of Closure expressed via identity neighborhoods

Let $A$ be any subset of a topological group $G$. We prove that $\overline{A} = \bigcap AV = \bigcap VA$, where $V$ runs over any fundamental system of neighborhoods of the neutral element $e$.

Since the intersections are unaffected by the particular choice of fundamental system of neighborhoods, we may assume that $V$ runs over the class $\mathcal{V}$ of all neighborhoods of $e$.

For $V \in \mathcal{V}$, define

$$V_s(A) = \{x : \exists a \in A \ni (a, x) \in V_s\},$$

where $V_s = \{(x, y) : x^{-1}y \in V\}$ is the entourage associated with $V$ (5.3). Then

$$V_s(A) = \{x : \exists a \in A \ni x \in V_s(a)\} = \bigcup_{a \in A} V_s(a) = \bigcup_{a \in A} aV = AV.$$

By the theory of uniform spaces, the closure of a set in the uniform topology is given by $\overline{A} = \bigcap_{V \in \mathcal{V}} V_s(A)$. Hence

$$\overline{A} = \bigcap_{V \in \mathcal{V}} AV.$$

For the right-sided version, note that the inversion mapping $x \mapsto x^{-1}$ is a homeomorphism, and $V \in \mathcal{V}$ if and only if $V^{-1} \in \mathcal{V}$. Therefore, letting $V$ vary over $\mathcal{V}$,

$$\bigcap VA = \bigcap V^{-1}A = \bigcap (A^{-1}V)^{-1} = \left(\bigcap A^{-1}V\right)^{-1} = \left(\overline{A^{-1}}\right)^{-1} = \overline{A}.$$

This completes the proof that $\overline{A} = \bigcap AV = \bigcap VA$.
