---
role: proof
locale: en
of_concept: finite-characterization-via-well-ordering
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Characterization of Finite Sets via Well-Ordering

PROOF One may proceed by induction on $P(x)$. Explicitly, consider the set $s$ of all integers $u$ such that, if $P(x) = u$ and each member of $x$ is finite, then $\bigcup x$ is finite. Clearly 0 belongs to the set $s$. If $u \in s$, $P(x) = u + 1$, and each member of $x$ is finite, then one may split $x$ into two subsets, one of which has power $u$ and one of which is a singleton. The induction hypothesis and the preceding theorem then show that $\bigcup x$ is finite. Hence $s = \omega$.
