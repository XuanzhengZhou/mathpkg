---
role: proof
locale: en
of_concept: regular-t1-sigma-locally-finite-metrizable
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Regular T1 Space with Sigma-Locally Finite Base is Metrizable

**Lemma 20.** A regular $T_1$-space whose topology has a $\sigma$-locally finite base is metrizable.

*Proof.* It will be shown that there is a countable family $D$ of pseudo-metrics on the space $X$ such that each member of $D$ is continuous on $X \times X$ and such that for each closed subset $A$ of $X$ and each point $x$ of $X \sim A$ there is a member $d$ of $D$ such that the $d$-distance from $x$ to $A$ is positive. This will prove metrizability, for the map of $X$ into each of the pseudo-metric spaces $(X,d)$ will then be continuous, and Lemma 5 (Embedding Lemma) and Theorem 14 will apply just as for the Urysohn theorem.

Let $\mathcal{B}$ be a $\sigma$-locally finite base for the topology of $X$, and suppose $\mathcal{B} = \bigcup \{\mathcal{B}_n : n \in \omega\}$ where each $\mathcal{B}_n$ is locally finite. For every ordered pair of integers $m$ and $n$ and for each member $U$ of $\mathcal{B}_m$, let $U'$ be the union of all members of $\mathcal{B}_n$ whose closures are contained in $U$. Because $\mathcal{B}_n$ is locally finite, the closure of $U'$ is a subset of $U$, and by Lemma 19 and Urysohn's Lemma there is a continuous function $f_U$ on $X$ to the unit interval which is one on $U'$ and zero on $X \sim U$.

Define

$$d(x,y) = \sum_{U \in \mathcal{B}_m} |f_U(x) - f_U(y)|.$$

The continuity of $d$ on $X \times X$ is a straightforward consequence of the local finiteness of $\mathcal{B}_m$: each point has a neighborhood intersecting only finitely many members of $\mathcal{B}_m$, so the sum is locally finite and continuous.

Finally, let $D$ be the countable family of all such pseudo-metrics (indexed by the countable set of pairs $(m,n)$). For any closed set $A$ and $x \notin A$, choose $U \in \mathcal{B}$ with $x \in U \subset X \sim A$, and let $U \in \mathcal{B}_m$, $V \in \mathcal{B}_n$ with $x \in V \subset V^{-} \subset U$. Then the pseudo-metric $d$ corresponding to $(m,n)$ satisfies $d(x,A) \geq 1$ (since $f_U(x) = 1$ and $f_U = 0$ on $A$).

