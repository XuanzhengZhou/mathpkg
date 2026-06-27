---
role: proof
locale: en
of_concept: plh-approximation-between-triangulated-2-manifolds
source_book: gtm047
source_chapter: "8"
source_section: "8"
---

By Theorem 2, $U$ is a polyhedron, $= |K_U|$, where every $\sigma \in K_U$ is a rectilinear subsimplex of a simplex of $K_1$. Thus, in Theorem 6.4, we may take $K_1 = K_U$. By Theorem 6.4 it follows that there is a PLH $f: U \rightarrow |K_2|$, satisfying (1). It remains to show that $f$ can be chosen so as to satisfy (2). If for each component $C$ of $U$ we have $f(C) = h(C)$, then (2) follows. We may therefore assume hereafter that $U$ is connected.

Now $U$ is the union of a sequence $N_1, N_2, \ldots$ of compact connected 2-manifolds with boundary, such that for each $i$, $N_i \subset \text{Int } N_{i+1}$. For each $i$, let $N_i' = h(N_i)$. Using the Invariance of Domain (Theorem 0.4), we can easily show that $h(U)$ is open, and $\text{Int } N_i' = h(\text{Int } N_i)$ is open for each $i$.

The proof then proceeds by constructing $f$ inductively on the sequence $N_i$, ensuring that at each stage the PLH approximation $f$ on $N_i$ has image equal to $h(N_i)$. The full details rely on the PLH approximation theorem (Theorem 6.4) applied repeatedly with increasingly refined control, together with the Invariance of Domain to preserve openness of images.
