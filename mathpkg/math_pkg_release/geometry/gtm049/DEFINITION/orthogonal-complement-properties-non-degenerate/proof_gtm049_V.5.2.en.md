---
role: proof
locale: en
of_concept: orthogonal-complement-properties-non-degenerate
source_book: gtm049
source_chapter: "V"
source_section: "5.2"
---

Non-degeneracy of $\sigma$ implies $V^{\top} = 0 = V^{\perp}$. Then (1) follows immediately from Proposition 4, since $M \cap V^{\top} = 0$ and $M \cap V^{\perp} = 0$.

By Lemma 2, $M \subset M^{\perp \top}$, and by (1), $\dim M^{\perp \top} = \dim V - \dim M^{\perp} = \dim V - (\dim V - \dim M) = \dim M$. Hence equality holds, establishing (2).

Property (3) follows from the definitions: if $M \subset N$, any vector orthogonal to all of $N$ is certainly orthogonal to all of $M$, so $M^{\perp} \supset N^{\perp}$. Conversely, if $M^{\perp} \supset N^{\perp}$, applying $\top$ and using (2) yields $M \subset N$.

Properties (4) and (5) are proved by the same reasoning as in Theorem 6 of Chapter IV (p. 81), using that $\perp$ and $\top$ are inclusion-reversing bijections.
