---
role: proof
locale: en
of_concept: sylvesters-law-of-inertia
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

If $M$ is a positive definite subspace and $N$ is a negative semi-definite subspace, then clearly $M \cap N = \{0\}$. Thus

$$\dim M + \dim N \leq \dim V.$$

But in particular $N = Q \oplus V^\perp$ satisfies this inequality and so

$$\dim M \leq \dim V - (\dim V - \dim P) = \dim P.$$

Hence $p = \dim P$ is the maximum dimension of all positive definite subspaces of $V$, and as such is an invariant. Finally, $q = \dim Q$ is also an invariant because $q = r - p$ where $r$ is the rank of $\sigma$.
