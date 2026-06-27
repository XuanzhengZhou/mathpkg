---
role: proof
locale: en
of_concept: relative-discriminant-decomposition
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 112

**Theorem 112.** The relative different of $K$ is the GCD of all relative differents of integers of $K$ with respect to $k$.

**Proof.** For the proof of this theorem we must proceed almost exactly as in the proof of Theorem 105 (the absolute case in §36).

Let $\theta$ be an integer generating the field $K$ over $k$, and let $\Phi(x)$ be the irreducible polynomial over $k$ with leading coefficient $1$ which has the root $\theta$. The relative ring $R_k(\theta)$ is the set of all numbers

$$\alpha_0 + \alpha_1\theta + \cdots + \alpha_{m-1}\theta^{m-1}$$

where $\alpha_0, \ldots, \alpha_{m-1}$ run through all integers in $k$.

By Lemma (a), if $A$ is an integer in $K$ such that $A\mathfrak{D}_k$ is integral, then $A = B/\Phi'(\theta)$ with $B \in R_k(\theta)$. This shows that $\Phi'(\theta)$ is a common multiple of the denominators arising from the dual basis of $R_k(\theta)$.

By Lemma (b), for each $B \in R_k(\theta)$, the relative trace $S_k(B/\Phi'(\theta))$ is integral, which means that $1/\Phi'(\theta)$ is in the complementary module of $R_k(\theta)$ with respect to the relative trace.

Now, using the approach of Theorem 105: consider the complementary module $\mathfrak{M}$ of the ring of integers of $K$ with respect to the relative trace form $S_k$. The relative different is $\mathfrak{D}_k = \mathfrak{M}^{-1}$. On the other hand, for any integer $\alpha$ generating $K$ over $k$, the relative different $\delta_k(\alpha)$ is related to $\Phi'(\alpha)$. The GCD of all such $\delta_k(\alpha)$ over all generating integers $\alpha$ is precisely $\mathfrak{D}_k$.

The proof is completed by Lemma (c): for each prime ideal $\mathfrak{P}$ of $K$, there exists a relative ring $R_k(\theta)$ such that $\mathfrak{P} \nmid \mathfrak{F} = \Phi'(\theta)/\mathfrak{D}_k$, which ensures that the prime ideal factorization of $\mathfrak{D}_k$ is exactly the GCD of the $\delta_k(\alpha)$.
