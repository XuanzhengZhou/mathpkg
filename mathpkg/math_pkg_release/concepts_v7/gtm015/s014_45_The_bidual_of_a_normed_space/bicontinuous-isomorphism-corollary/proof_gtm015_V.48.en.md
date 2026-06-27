---
role: proof
locale: en
of_concept: bicontinuous-isomorphism-corollary
source_book: gtm015
source_chapter: "V"
source_section: "48"
---

# Proof of the Bicontinuous Isomorphism Corollary

Let $T: E \to F$ be a bijective continuous linear mapping, where $E$ and $F$ are metrizable, complete TVS. Then $T$ is surjective, so by the Open Mapping Theorem (48.1), $T$ is an open mapping. This means that for every open set $U \subset E$, $T(U)$ is open in $F$.

The inverse mapping $T^{-1}: F \to E$ is continuous because for any open set $U \subset E$, the preimage $(T^{-1})^{-1}(U) = T(U)$ is open in $F$ (since $T$ is open). Thus $T^{-1}$ is continuous, and $T$ is a bicontinuous isomorphism (i.e., a topological isomorphism of TVS).

*Application to quotient spaces (48.7):* Let $M$ and $N$ be closed linear subspaces of $E$ such that $E = M \oplus N$ algebraically. Let $\pi: E \to E/M$ be the quotient map and $S: E/M \to N$ the natural isomorphism. If $T = S \circ \pi: E \to N$ (the projection onto $N$ along $M$) is continuous, then $S$ is bicontinuous. Indeed, for $V$ open in $E/M$, $S(V) = S(\pi(\pi^{-1}(V))) = T(\pi^{-1}(V))$ is open in $T(E) = N$ since $\pi^{-1}(V)$ is open and $T$ is open. In particular, $N$ is complete (and hence closed in $F$). $\square$
