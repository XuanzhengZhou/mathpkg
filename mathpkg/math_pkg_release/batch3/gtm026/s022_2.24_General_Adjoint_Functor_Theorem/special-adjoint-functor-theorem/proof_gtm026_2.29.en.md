---
role: proof
locale: en
of_concept: special-adjoint-functor-theorem
source_book: gtm026
source_chapter: "2"
source_section: "2.29"
---

The proof proceeds by verifying the solution set condition of Theorem 2.24, since the other hypotheses (locally small domain with small limits, and $U$ preserving small limits) are already assumed.

Fix $K$ in $\mathcal{K}$. Let $C$ be a cogenerator in $\mathcal{A}$ and let $P$ be the cartesian power object $C^{\mathcal{K}(K, CU)}$ in $\mathcal{A}$. This is meaningful since $\mathcal{K}$ is locally small (as a consequence of $\mathcal{A}$ being locally small and $U$ preserving limits). Since $\mathcal{A}$ is well-powered, there exists a small set $\mathcal{S}$ of objects in $\mathcal{A}$ such that every subobject of $P$ is represented by a monomorphism with domain in $\mathcal{S}$.

Set $\mathcal{S}_K = \{(S, s): S \in \mathcal{S} \text{ and } s: K \longrightarrow SU\}$. Then $\mathcal{S}_K$ is a small set, again since $\mathcal{K}$ is locally small.

Now consider an arbitrary pair $(A, f)$ with $f: K \longrightarrow AU$. Consider the cartesian power $Q = C^{\mathcal{A}(A, C)}$, which exists since $\mathcal{A}$ is locally small. For each $x: A \longrightarrow C$ in $\mathcal{A}$ we have $f.xU: K \longrightarrow CU$ in $\mathcal{K}$, which induces a unique morphism $\alpha$ from the product diagram. The evaluation map $\text{ev}_A$ is a monomorphism because $C$ is a cogenerator, so $A$ may be thought of as a subobject of $Q$. Because $\mathcal{A}$ has small limits we may take the inverse image of $A$ under $\alpha$, which is a subobject of $P$; that is, there exists a pullback square with $S \in \mathcal{S}$. Because $U$ preserves small limits, $U$ of this square is still a pullback and $PU$, $QU$ are still powers of $CU$. In particular, we can define $\text{ev}_K$ as in 1.60. For each $x: A \longrightarrow C$ we have the required commuting diagram. Therefore $\mathcal{S}_K$ is a solution set, and by Theorem 2.24, $U$ has a left adjoint.
