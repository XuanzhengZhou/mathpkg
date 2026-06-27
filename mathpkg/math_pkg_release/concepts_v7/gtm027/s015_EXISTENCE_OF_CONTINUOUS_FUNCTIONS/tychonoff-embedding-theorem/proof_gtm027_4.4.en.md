---
role: proof
locale: en
of_concept: tychonoff-embedding-theorem
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Tychonoff Embedding Theorem

**Tychonoff Embedding Theorem.** In order that a topological space be a Tychonoff space it is necessary and sufficient that it be homeomorphic to a subspace of a cube.

*Proof.* (Sufficiency) The closed unit interval $[0,1]$ is a Tychonoff space, and hence a cube $[0,1]^A$, being a product of unit intervals, is a Tychonoff space by Theorem 6. Each subspace of a cube is therefore a Tychonoff space.

(Necessity) If $X$ is a Tychonoff space and $F$ is the set of all continuous functions on $X$ to the closed unit interval $[0,1]$, then by the embedding lemma 4.5, the evaluation map $e: X \to [0,1]^F$ is continuous, one-to-one (since $X$ is $T_1$, the family $F$ distinguishes points), and open onto its image (since $X$ is completely regular, $F$ distinguishes points and closed sets). Therefore $e$ is a homeomorphism of $X$ onto a subspace of the cube $[0,1]^F$.

