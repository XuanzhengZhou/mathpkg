---
role: proof
locale: en
of_concept: orthogonal-decomposition-nondegenerate-subspace
source_book: gtm049
source_chapter: "V"
source_section: "5.2"
---

**Proof.** We prove the result for $\perp$; the argument for $\top$ is identical.

First, we note that $M \cap M^{\perp} = 0$. Indeed, $M \cap V^{\top} \subset M \cap M^{\top}$. Since $M$ is non-degenerate, the restriction $\sigma|_M$ has trivial radical, so $M \cap M^{\top} = 0$. Hence $M \cap V^{\top} \subset 0$, so $M \cap V^{\top} = 0$. Now by Proposition 4,

$$\dim M + \dim M^{\perp} = \dim V + \dim(M \cap V^{\top}) = \dim V.$$

Since $M \cap M^{\perp} = 0$ and $\dim M + \dim M^{\perp} = \dim V$, we have $V = M \oplus M^{\perp}$.
