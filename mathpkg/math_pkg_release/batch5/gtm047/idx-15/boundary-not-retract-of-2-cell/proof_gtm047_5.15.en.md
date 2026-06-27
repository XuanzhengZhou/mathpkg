---
role: proof
locale: en
of_concept: boundary-not-retract-of-2-cell
source_book: gtm047
source_chapter: "5"
source_section: "15"
---

As in the proof of Theorem 9, we may suppose that $C^2$ is a rectangular region in $\mathbf{R}^2$. Let $P, Q, R, S$ be as in Theorem 9, and suppose that there is a retraction $r: C^2 \to J$. Let
$$M_1 = r^{-1}(P), \quad M_2 = r^{-1}(R).$$
By Theorem 9, $Q$ and $S$ are in the same component of $C^2 - (M_1 \cup M_2)$. But $r(Q) = Q$ and $r(S) = S$, since $r|J$ is the identity. The sets $M_1$ and $M_2$ are disjoint closed subsets of $C^2$ (since $\{P\}$ and $\{R\}$ are closed in $J$ and $r$ is continuous), with $P \in M_1$ and $R \in M_2$, and $M_1 \cap J$, $M_2 \cap J$ are closed in $J$.

Theorem 9 asserts that $Q$ and $S$ lie in the same connected component of $C^2 - (M_1 \cup M_2)$. Hence there is a connected set (in fact, an arc) in $C^2$ joining $Q$ to $S$ and avoiding $M_1 \cup M_2$. Applying $r$ to this arc yields a connected set in $J$ joining $Q = r(Q)$ to $S = r(S)$ and avoiding $r(M_1 \cup M_2)$, which contains $P$ and $R$. Thus $Q$ and $S$ can be joined in $J$ without passing through $P$ or $R$. But on $J$, the points appear in cyclic order $P, Q, R, S$, so any arc in $J$ from $Q$ to $S$ must pass through either $P$ or $R$. This contradiction shows that no such retraction exists.
