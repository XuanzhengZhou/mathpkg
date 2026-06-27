---
role: proof
locale: en
of_concept: direct-sum-decomposition-theorem
source_book: gtm042
source_chapter: "1"
source_section: "1.4"
---

Let $V$ be a linear representation of $G$. We proceed by induction on $\dim(V)$. If $\dim(V) = 0$, the theorem is obvious (0 is the direct sum of the empty family of irreducible representations). Suppose $\dim(V) \geqslant 1$. If $V$ is irreducible, there is nothing to prove. Otherwise, by Theorem 1, $V$ can be decomposed into a direct sum $V' \oplus V''$ with $\dim(V') < \dim(V)$ and $\dim(V'') < \dim(V)$. By the induction hypothesis $V'$ and $V''$ are direct sums of irreducible representations, and so $V$ is a direct sum of irreducible representations.
