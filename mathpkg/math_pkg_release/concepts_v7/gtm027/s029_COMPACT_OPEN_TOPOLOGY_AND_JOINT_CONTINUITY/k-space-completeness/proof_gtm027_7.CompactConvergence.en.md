---
role: proof
locale: en
of_concept: k-space-completeness
source_book: gtm027
source_chapter: "7"
source_section: "Uniform Convergence on Compacta"
---

# Proof of Theorem 7.12 — Completeness on k-Spaces under Compact Convergence

Let $X$ be a $k$-space (i.e., a space in which a set is closed iff its intersection with every closed compact set is closed) and let $(Y, \mathcal{V})$ be a complete uniform space. Let $F$ be the family of all continuous functions on $X$ to $Y$, with the uniformity of uniform convergence on compacta.

By Theorem 7.10(c), the space of all functions on $X$ to $Y$ which are continuous on each compact subset is complete relative to uniform convergence on compacta. In a $k$-space, a function which is continuous on every compact subset is continuous on the whole space $X$ (this is the defining property of $k$-spaces: the topology is determined by the compact subsets). Hence the family $F$ coincides with the family of functions continuous on each compact set.

Therefore $F$ is a closed subset of the complete space of functions continuous on compacta (Theorem 7.10(d)), and thus $F$ is complete relative to uniform convergence on compacta.
