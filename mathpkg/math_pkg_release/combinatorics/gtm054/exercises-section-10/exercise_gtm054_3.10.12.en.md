---
role: exercise
locale: en
chapter: "3"
section: "10"
exercise_number: 12
---

Let $K_n = (V, \mathcal{P}_2(V))$ and let $\mathcal{A}_n = \mathcal{Z}(K_n)$. Show that:

(a) $\mathcal{A}_n$ is spanned by $\{\mathcal{P}_2(W): W \in \mathcal{P}_3(V)\}$. [Hint: use induction on $n$.]

(b) $\mathcal{A}_n$ is connected for all $n$, and hence $K_n$ is bicon

III E Planar Multigraphs

Intuitively, a "planar multigraph" is a multigraph which can be represented in the plane in such a way that edges meet only at vertices. One can be more rigorous in topological language, but it requires regarding a multigraph as a topological object, namely as a 1-dimensional simplicial complex (except that two vertices may be joined by more than a single edge), an edge being regarded as a homeomorph of a closed real interval. Such a topological "multigraph" is called planar if it can be homeomorphically embedded into 2-dimensional Euclidean space, or equivalently, into the 2-sphere. Our approach here, however, will be combinatorial and ultimately algebraic. Demonstrating the equivalence of various mathematical approaches to planarity is no easy or elegant matter. Since one cannot seem to exploit the best from all possible mathematical worlds simultaneously, we will confine our rigor to combinatorics (except in §VII D and §VII E). Nonetheless we will freely use more pictorial language for both motivation and reinforcement.

Working unrigorously, the reader may observe by trial and error that $K_n$, for example, can be drawn in the plane if and only if $n \leq 4$. In particular, $K_5$ must be drawn with some edges meeting other than at common vertices (Figure E1a). With care the number of these "cross-overs" can be reduced to just one (Figure E1b).

After the reader has spent some time on this trial-and-error method, the difficulties of demonstrating for instance, that $K_5$ is "nonplanar" become apparent, and the lack of a rigorous terminology should no doubt contribute to the frustration. Among the various combinatorial developments of planarity, ours will most closely parallel the work of S. MacLane [m.1] and will be closely related also to the approach of H. Whitney [w.9].

The first observation related to MacLane's approach to planarity is that when a multigraph $\Gamma$ is realized in the plane (without "cross-overs"), there are certain cycles which play a special role. The set-theoretic complement in the plane of the realization of $\Gamma$ has connected components, which are usually called "regions." The boundaries of these "reg

as noted in §A, belong to the cycle space of $\Gamma$ and have algebraic significance in this space. These topological regions will be identified with their bounding cycles. MacLane used these cycles to characterize planarity.

We illustrate for a specific multigraph $\Gamma$, MacLane’s “bounding cycles.” Let $\Gamma$ be the multigraph drawn in Figure E2. Its “regions” are:

$$\{e_1, e_2\}, \{e_2, e_3, e_4\}, \{e_4, e_5\}, \{e_5, e_6, e_7\}, \{e_1, e_3, e_6, e_7\}.$$
