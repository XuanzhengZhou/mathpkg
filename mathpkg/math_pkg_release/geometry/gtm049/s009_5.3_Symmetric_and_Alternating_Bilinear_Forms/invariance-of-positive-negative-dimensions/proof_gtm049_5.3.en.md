---
role: proof
locale: en
of_concept: invariance-of-positive-negative-dimensions
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** If $M$ is a positive definite subspace and $N$ is a negative semi-definite subspace, then $M \cap N = 0$. Thus $\dim M + \dim N \leq \dim V$. In particular, taking $N = Q \oplus V^\perp$ (which is negative semi-definite) gives $\dim M \leq \dim V - (\dim V - \dim P) = \dim P$. Hence $p = \dim P$ is the maximum dimension of all positive definite subspaces of $V$, and as such is an invariant. Finally, $q = \dim Q$ is also invariant because $q = r - p$ where $r = \operatorname{rank} \sigma$.
