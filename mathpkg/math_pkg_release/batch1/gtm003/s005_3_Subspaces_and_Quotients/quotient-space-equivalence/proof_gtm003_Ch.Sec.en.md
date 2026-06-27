---
role: proof
locale: en
of_concept: quotient-space-equivalence
source_book: gtm003
source_chapter: ""
source_section: "3"
---

Let $M$ be a subspace of $L$. Define the relation $\sim$ on $L$ by $x \sim y$ if and only if $x - y \in M$.

**Reflexivity.** For any $x \in L$, $x - x = 0 \in M$ since $M$ is a subspace (it contains $0$). Thus $x \sim x$.

**Symmetry.** If $x \sim y$, then $x - y \in M$. Since $M$ is a subspace, $M$ is closed under scalar multiplication by $-1$, so $y - x = -(x - y) \in M$. Thus $y \sim x$.

**Transitivity.** If $x \sim y$ and $y \sim z$, then $x - y \in M$ and $y - z \in M$. Since $M$ is closed under addition, $(x - y) + (y - z) = x - z \in M$. Thus $x \sim z$.

Therefore $\sim$ is an equivalence relation on $L$. The equivalence class of $x$ is the coset $x + M$, and the set of all equivalence classes forms the quotient vector space $L/M$.
