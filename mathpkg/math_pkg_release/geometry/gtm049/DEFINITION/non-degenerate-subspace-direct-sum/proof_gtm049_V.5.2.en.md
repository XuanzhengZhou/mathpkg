---
role: proof
locale: en
of_concept: non-degenerate-subspace-direct-sum
source_book: gtm049
source_chapter: "V"
source_section: "5.2"
---

We prove the statement for $\perp$; the argument for $\top$ is identical.

First, $M \cap M^{\perp} = 0$ by Lemma 3, which states that a non-degenerate subspace intersects its orthogonal complement only in the zero vector.

It remains to show $M + M^{\perp} = V$, for which it suffices to prove $\dim M + \dim M^{\perp} = \dim V$. By Proposition 4,
$$\dim M + \dim M^{\perp} = \dim V + \dim(M \cap V^{\top}).$$
Now $M \cap V^{\top} \subset M \cap M^{\top}$, and $M \cap M^{\top} = 0$ by Lemma 3 (since $M$ is non-degenerate). Hence $\dim(M \cap V^{\top}) = 0$, yielding $\dim M + \dim M^{\perp} = \dim V$.
