---
role: proof
locale: en
of_concept: orthogonal-complement-reduction
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

The proof proceeds exactly as in Exercise 3 of Section 6.3 (see proof of `simultaneous-mapping-reduction`), with the subspace $M$ taken to be $[c]^{\perp(\sigma)}$, the orthogonal complement of the common eigenvector $c$ with respect to the bilinear form $\sigma$.

Since $\sigma(c, c) = 1$, the line $[c]$ is non-degenerate, and by the properties of orthogonal complements in a space with a non-degenerate bilinear form, we have the direct sum decomposition
$$V = [c] \oplus [c]^{\perp(\sigma)}.$$
Set $M = [c]^{\perp(\sigma)}$ and apply the reduction lemma: for each $m \in M$, express $mf = mf' + xc$ with $mf' \in M$, $x \in F$. The induced mapping $f'$ is linear on $M$ and satisfies $(fg)' = f'g'$. The induction on $\dim V$ then completes the proof.
