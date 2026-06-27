---
role: proof
locale: en
of_concept: finite-complex-subdivision-approaching-open-set
source_book: gtm047
source_chapter: "7"
source_section: "The triangulation theorem for 2-manifolds"
---

Let $K_1, K_2, \ldots$ be a sequence of finite complexes such that (1) $K_1 = K$, (2) for each $i$, $K_{i+1} < K_i$, and (3) $\lim_{i \to \infty} \|K_i\| = 0$. Such a sequence exists by repeated barycentric subdivision.

Set $n_1 = 1$ and let

$$L_1 = \{ \sigma \mid \sigma \in K_1 = K_{n_1} \text{ and } \sigma \subset U \}.$$

Suppose recursively that we have constructed $n_1, n_2, \ldots, n_r$ and $L_1, L_2, \ldots, L_r$ satisfying:

(1) For each $i$, $L_i$ is a subcomplex of $K_{n_i}$.
(2) The numbers $n_i$ form an increasing sequence.
(3) $\bigcup_{i=1}^{r} |L_i| \subset U$.
(4) $\bigcup_{i=1}^{r} |L_i|$ forms a neighborhood of $\bigcup_{i=1}^{r-1} |L_i|$ in $|K|$.
(5) If $\sigma \in K_{n_r}$, then either $\sigma \subset \bigcup_{i=1}^{r} |L_i|$ or $\sigma$ intersects $K - U$.

Since $\operatorname{Fr} \bigcup_{i=1}^{r} |L_i|$ and $K - U$ are disjoint compact sets, there is a minimum distance $\varepsilon > 0$ between them. Let $n_{r+1}$ be an integer greater than $n_r$ and sufficiently large so that $\|K_{n_{r+1}}\| < \varepsilon$. Then define

$$L_{r+1} = \{ \sigma \mid \sigma \in K_{n_{r+1}} \text{ and } \sigma \subset U \}.$$

The construction ensures that $\bigcup_i |L_i| = U$, and the union of the $L_i$ forms the required complex $K_U$.
