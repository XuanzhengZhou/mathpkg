---
role: proof
locale: en
of_concept: monomorphism-extension-theorem
source_book: gtm033
source_chapter: "3"
source_section: "3. The Classification of Vector Bundles"
---

# Proof of Monomorphism Extension Theorem (Theorem 3.1)

Consider first the special case where $\xi$ is the trivial bundle $M \times \mathbb{R}^k$. Then for each $x \in U$, the restriction $F|_{\{x\} \times \mathbb{R}^k}$ is an injective linear map from $\mathbb{R}^k$ to $\mathbb{R}^s$ of rank $k$. Choosing the standard basis of $\mathbb{R}^k$, this linear map is represented by an $s \times k$ matrix of rank $k$, i.e., a $k$-frame in $\mathbb{R}^s$. We thus obtain a map

$$g: U \to V_{s,k}$$

from $U$ to the Stiefel manifold $V_{s,k}$ of orthonormal $k$-frames in $\mathbb{R}^s$, which is easily proved to be $C^r$ (the matrix entries vary differentiably with $x$).

Since $s \geqslant k + \dim M$, we have $\dim M \leqslant s - k$. Now apply Theorem 3.2.5 (on extending maps into the Stiefel manifold): when the dimension of the domain is at most $s - k$, any $C^r$ map from a closed subset into $V_{s,k}$ can be extended to a $C^r$ map on the whole manifold that agrees with the original map on a neighborhood of the closed subset. Concretely, we extend $g|_A$ (where $A \subset U$ is closed) to a $C^r$ map

$$\tilde{g}: M \to V_{s,k}$$

which agrees with $g$ on some neighborhood $W$ of $A$ in $U$.

The extended map $\tilde{g}$ defines a $C^r$ bundle monomorphism

$$G: M \times \mathbb{R}^k \to M \times \mathbb{R}^s$$

over $1_M$ by the formula $G(x, v) = (x, \tilde{g}(x) \cdot v)$, where $\tilde{g}(x)$ acts as a linear injection $\mathbb{R}^k \hookrightarrow \mathbb{R}^s$ (using the identification of a $k$-frame with the corresponding injective linear map). This $G$ coincides with $F$ on $W \times \mathbb{R}^k$, since $\tilde{g} = g$ on $W$ and $F$ is represented by $g$ on $U \times \mathbb{R}^k$.

For the general case where $\xi$ may be nontrivial, take a cover of $M$ by open sets $\{V_\alpha\}$ such that $\xi|_{V_\alpha}$ is trivial for each $\alpha$. By paracompactness of $M$, there exists a locally finite refinement $\{W_j\}$ by relatively compact open sets and a partition of unity subordinate to this cover. On each $W_j$, $\xi|_{W_j}$ is trivial. One then extends the monomorphism inductively across the $W_j$, using the trivial case at each step. At the $j$-th inductive step, one has already extended the monomorphism to a neighborhood of

$$A \cup \bigcup_{i < j} \overline{W}_i,$$

and the extension across $W_j$ is handled by the trivial-bundle case proved above (possibly after shrinking $W_j$ slightly). The dimension condition $s \geqslant k + \dim M$ guarantees that at each step the target Stiefel manifold $V_{s,k}$ is $(s - k - 1)$-connected, hence $(s - k - 1) \geqslant (\dim M - 1)$, so that the extension obstruction vanishes.

The resulting global extension $G: \xi \to M \times \mathbb{R}^s$ is $C^r$ by construction and agrees with $F$ on a neighborhood of $A$. $\square$
