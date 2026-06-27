---
role: proof
locale: en
of_concept: homeomorphism-of-cantor-sets-preserving-countable-dense-sets
source_book: gtm047
source_chapter: "12"
source_section: "17"
---

We need a refinement of the proof of the preceding theorem. Let
$$D = \{P_1, P_2, \ldots\}, \quad D' = \{P'_1, P'_2, \ldots\},$$
where both sequences are bijective. We set up the same apparatus as in the proof of Theorem 8, with additional provisos as follows. Below, $G_i(P_j)$ denotes the element of $G_i$ that contains $P_j$, and similarly for $G_i'(P_k')$. We want to define the sets $G_i$ and $G_i'$, and the functions $f_i$ so that

(1) For each $j$ there is a $k_j$ such that for each $i$,
$$f_i(G_i(P_j)) = G_i'(P'_{k_j}).$$

(2) For each $k$ there is a $j_k$ such that for each $i$,
$$f_i(G_i(P_{j_k})) = G_i'(P'_k).$$

If these conditions hold, and $f$ is as in the proof of Theorem 8, then $f(P_j) = P'_{k_j}$ and $f(P_{j_k}) = P'_k$. Thus $f|_D$ is a homeomorphism $D \leftrightarrow D'$. We obtain Properties (1) and (2) by an inductive construction as follows.

(I) Define $G_1$, $G'_1$, and $f_1$ as before, so that $f_1$ is an arbitrary bijection $G_1 \leftrightarrow G'_1$. Let $P'_{k_1}$ be any point of $D'$. We ensure that $f_1(G_1(P_1)) = G'_1(P'_{k_1})$ by relabeling the elements of $G'_1$ if necessary. Similarly, choose $P_{j_1} \in D$ such that $f_1(G_1(P_{j_1})) = G'_1(P'_1)$.

(II) Having constructed $G_n$, $G'_n$, and $f_n$ satisfying (1) and (2) for $j,k \le n$, refine $G_n$ to $G_{n+1}$ and $G'_n$ to $G'_{n+1}$ so that the refinement compatibility conditions hold. Adjust $f_{n+1}$ to satisfy (1) and (2) for $j,k \le n+1$ while preserving the required intersection and inclusion properties. This is possible because at each stage only finitely many points of $D$ and $D'$ are constrained, and the refinements can be chosen sufficiently fine.

The limit function $f$ then satisfies $f(D) = D'$ and is a homeomorphism $C \leftrightarrow C'$ by the same argument as in Theorem 8. As a consequence, $f|_D$ is a homeomorphism $D \leftrightarrow D'$.
