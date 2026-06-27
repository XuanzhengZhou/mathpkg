---
locale: en
of_concept: let-t-mathbfa-rightarrow-mathbfens-be-a-cofunctor-and-let-be
role: proof
source_book: gtm020
source_chapter: 20. General Theory of Characteristic Classes
source_section: '1'
---

We define an inverse function $\alpha$ of $\beta$ by the relation $\alpha(x)(X)u = T(u)x$ for $x \in T(K)$ and $u \in [X, K]$. To verify that $\alpha(x): [-, K] \rightarrow T$ is a morphism of cofunctors, we make the following calculation for $f: Y \rightarrow X$:

$$T(f)\alpha(x)(X)u = T(f)T(u)x = T(uf)x = \alpha(x)(Y)uf = \alpha(x)(T)[f, K]u$$

To show that $\alpha$ and $\beta$ are inverses to each other, we calculate $\beta(\alpha(x)) = \alpha(x)(K)1_K = T(1_K)x = x$ and $\alpha\beta(\phi)(X)u = \alpha(\phi(K)1_K)(X)u = T(u)\phi(K)1_K = \phi(X)u1_K = \phi(X)u$. Consequently, we have $\beta\alpha = 1$ and $\alpha\beta = 1$. This proves the theorem.
