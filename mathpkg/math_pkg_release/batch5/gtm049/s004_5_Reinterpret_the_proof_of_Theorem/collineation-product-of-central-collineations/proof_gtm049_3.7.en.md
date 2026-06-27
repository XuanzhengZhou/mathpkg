---
role: proof
locale: en
of_concept: collineation-product-of-central-collineations
source_book: gtm049
source_chapter: "3"
source_section: "3.7"
---

Let $m(\pi)$ be the maximum of the dimensions $\operatorname{pdim} M$ for all subspaces $M$ whose points are left invariant by $\pi$. Define $i(\pi) = \operatorname{pdim} V - m(\pi)$. The proof is by induction on $i(\pi)$.

When $i(\pi) = 0$, $\pi$ is the identity mapping, regarded as a product of no central collineations. When $i(\pi) = 1$, $\pi$ is a central collineation by definition.

Assume the result holds for all $\pi$ with $i(\pi) < k$ and consider a collineation with $i(\pi) = k$. Let $M$ be a subspace whose points are left invariant by $\pi$ with $\operatorname{pdim} M = m(\pi)$. If $P$ is any point not in $M$, then $P\pi$ also is not in $M$. Write $\pi = \mathcal{P}(g)$ where the restriction of $g$ to $M$ is $1_M$.

If $P = [p]$ and $q = pg$, then by Lemma 3 there exists an automorphism $f_1$ such that $f_1$ restricts to the identity on $M$, $q = pf_1$, and $\pi_1 = \mathcal{P}(f_1)$ is a central collineation.

It follows that $f_1^{-1}g$ restricts to the identity on $M + [q]$, so $m(\mathcal{P}(f_1^{-1}g)) \geq m(\pi) + 1$ and $i(\mathcal{P}(f_1^{-1}g)) \leq k - 1$. By the induction hypothesis, $\mathcal{P}(f_1^{-1}g) = \pi_2 \cdots \pi_k$ is a product of at most $k-1$ central collineations. Thus

$$\mathcal{P}(g) = \mathcal{P}(f_1)\mathcal{P}(f_1^{-1}g) = \pi_1\pi_2 \cdots \pi_k$$

is a product of at most $k \leq n$ central collineations.
