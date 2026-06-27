---
role: proof
locale: en
of_concept: open-cover-sigma-discrete-refinement
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Open Covers of Pseudo-Metrizable Spaces Have Sigma-Discrete Refinements

**Theorem 21.** Each open cover of a pseudo-metrizable space has an open $\sigma$-discrete refinement.

*Proof.* Let $\mathcal{U}$ be an open cover of the pseudo-metric space $(X,d)$. The first step in the proof is the decomposition of each member $U$ of $\mathcal{U}$ into "concentric disks." For each positive integer $n$ and each member $U$ of $\mathcal{U}$, let

$$U_n = \{x \in U : \operatorname{dist}(x, X \sim U) \geq 2^{-n}\}.$$

Because of the triangle inequality, $\operatorname{dist}(U_n, X \sim U_{n+1}) \geq 2^{-n} - 2^{-n-1} = 2^{-n-1}$.

Choose a well-ordering $<$ of the family $\mathcal{U}$ (see 0.25) and for each positive integer $n$ and each member $U$ of $\mathcal{U}$ let

$$U_n^* = U_n \sim \bigcup \{V_{n+1} : V \in \mathcal{U} \text{ and } V < U\}.$$

For each $U$ and $V$ in $\mathcal{U}$ and each positive integer $n$, it is true that $U_n^* \subset X \sim V_{n+1}$ or $V_n^* \subset X \sim U_{n+1}$, depending on whether $U$ follows or precedes $V$ in the ordering. In either case, $\operatorname{dist}(U_n^*, V_n^*) \geq 2^{-n-1}$.

Let $\mathcal{U}_n^* = \{U_n^* : U \in \mathcal{U}\}$. Then each $\mathcal{U}_n^*$ is a discrete family (since any two distinct members are at distance at least $2^{-n-1}$) and $\bigcup_n \mathcal{U}_n^*$ refines $\mathcal{U}$. Moreover, for any $x \in X$, choose the first $U \in \mathcal{U}$ (in the well-ordering) such that $x \in U$; then for sufficiently large $n$, $x \in U_n^*$. Hence $\bigcup_n \mathcal{U}_n^*$ is a cover. Therefore $\{\mathcal{U}_n^* : n \in \mathbb{N}\}$ is an open $\sigma$-discrete refinement of $\mathcal{U}$.

