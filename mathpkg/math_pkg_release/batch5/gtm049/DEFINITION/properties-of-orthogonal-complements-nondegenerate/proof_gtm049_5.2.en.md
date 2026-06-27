---
role: proof
locale: en
of_concept: properties-of-orthogonal-complements-nondegenerate
source_book: gtm049
source_chapter: "V"
source_section: "5.2"
---

**Proof.** Since $\sigma$ is non-degenerate, $V^{\top} = 0 = V^{\perp}$. Thus $M \cap V^{\top} = 0$ for all $M$, and Proposition 4 gives $\dim M^{\perp} = \dim V - \dim M$, which is (1). The dual formula for $\top$ follows similarly.

For (2): By Lemma 2, $M \subset M^{\perp \top}$. Applying (1) twice gives $\dim M^{\perp \top} = \dim M$, so they are equal. Similarly $M = M^{\top \perp}$.

For (3): If $M \subset N$, then every vector orthogonal to all of $N$ is certainly orthogonal to all of $M$, so $N^{\perp} \subset M^{\perp}$. Conversely, if $N^{\perp} \subset M^{\perp}$, then applying (2) gives $M = M^{\perp \top} \subset N^{\perp \top} = N$.

For (4): $(M + N)^{\perp}$ consists of all $b$ with $\sigma(M + N, b) = 0$, which means $\sigma(M, b) = 0$ and $\sigma(N, b) = 0$, i.e., $b \in M^{\perp} \cap N^{\perp}$. So $(M + N)^{\perp} = M^{\perp} \cap N^{\perp}$.

For (5): Apply the result of (4) to $M^{\perp}$ and $N^{\perp}$, then use (2): $(M^{\perp} + N^{\perp})^{\perp} = M \cap N$, so taking $\perp$ again gives $M^{\perp} + N^{\perp} = (M \cap N)^{\perp}$.
