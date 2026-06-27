---
role: proof
locale: en
of_concept: net-convergence-pseudo-metric
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Net Convergence in Pseudo-Metric Spaces

**Theorem 12.** A net $\{S_n, n \in D\}$ in a pseudo-metric space $(X,d)$ converges to a point $s$ if and only if $\{d(S_n, s), n \in D\}$ converges to zero.

*Proof.* A net $\{S_n, n \in D\}$ converges to $s$ iff the net is eventually in each open $r$-sphere about $s$, but this is true iff $\{d(S_n, s), n \in D\}$ is eventually in each open $r$-sphere about $0$ in the space of real numbers with the usual metric. By definition, this means $\{d(S_n, s), n \in D\}$ converges to zero.

