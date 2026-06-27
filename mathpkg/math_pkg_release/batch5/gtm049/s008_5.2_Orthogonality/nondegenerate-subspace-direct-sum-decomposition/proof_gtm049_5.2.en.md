---
role: proof
locale: en
of_concept: nondegenerate-subspace-direct-sum-decomposition
source_book: gtm049
source_chapter: "5"
source_section: "5.2 Orthogonality"
---

We prove the result for $\perp$; the argument for $\top$ is exactly the same.

By Lemma 3, $M \cap M^{\perp} = 0$, so it suffices to show that $M + M^{\perp} = V$. For this we only need to prove $\dim M + \dim M^{\perp} = \dim V$.

Now $M \cap V^{\top} \subset M \cap M^{\top}$, and by Lemma 3 (applied to $\top$) we have $M \cap M^{\top} = 0$. Therefore $M \cap V^{\top} = 0$.

Applying Proposition 4:
$$\dim M + \dim M^{\perp} = \dim V - \dim(M \cap V^{\top}) = \dim V - 0 = \dim V.$$

Thus $M \cap M^{\perp} = 0$ and $\dim M + \dim M^{\perp} = \dim V$, which together imply $V = M \oplus M^{\perp}$.

The proof for $V = M \oplus M^{\top}$ follows by symmetry, using $M \cap M^{\top} = 0$ and the second formula of Proposition 4.
