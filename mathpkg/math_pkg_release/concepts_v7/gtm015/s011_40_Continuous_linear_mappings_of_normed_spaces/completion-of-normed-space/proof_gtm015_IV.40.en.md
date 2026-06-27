---
role: proof
locale: en
of_concept: completion-of-normed-space
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Every normed space is a dense linear subspace of a Banach space

**Theorem (40.15).** Every normed space may be regarded as a dense linear subspace of a Banach space.

**Proof.**

Let $E$ be a normed space and let $x \mapsto x''$ be the canonical isometric embedding of $E$ into its bidual $E''$ (Theorem 40.13). The image of $E$ under this mapping is a linear subspace $E_0$ of $E''$, and the mapping $x \mapsto x''$ is an isometric isomorphism of $E$ onto $E_0$.

Let $F$ be the closure of $E_0$ in $E''$. Since $E''$ is a Banach space (Corollary 40.9: the dual of any normed space is a Banach space), the closed linear subspace $F$ is also a Banach space (by the theorem that a closed subspace of a complete metric space is complete).

By construction, $E_0$ is dense in $F$. Identifying $E$ with $E_0$ via the isometric isomorphism $x \mapsto x''$, we may regard $E$ as a dense linear subspace of the Banach space $F$.

**Remark.** Since $F$ is a complete topological vector space, $F$ may be identified with the completion of $E$ as a uniform space (in the sense of the general theory of completions of uniform spaces).
