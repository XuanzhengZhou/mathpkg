---
role: proof
locale: en
of_concept: bound-critical-points-by-dimension
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Lemma 1.9.** We argue by contradiction. Suppose $S = \{p_1,\ldots,p_{m+1}\}$ consists of distinct critical points of $f$ in $f^{-1}(q)$. For each $i$, let
\[
H_i = (df)_{p_i}(T_{p_i}X) \subseteq T_qY.
\]
Since each $p_i$ is a critical point, $(df)_{p_i}$ is not surjective, so $H_i$ is a proper subspace of $T_qY$; hence $\operatorname{codim} H_i \geq 1$.

By Lemma 1.7 (the last lemma), the subspaces $H_1,\ldots,H_{m+1}$ are in general position in $T_qY$. Therefore
\[
\operatorname{codim}(H_1 \cap \cdots \cap H_{m+1}) = \sum_{i=1}^{m+1} \operatorname{codim} H_i \geq m+1.
\]
But $H_1 \cap \cdots \cap H_{m+1}$ is a subspace of $T_qY$, which has dimension $m$, so its codimension cannot exceed $m$. This contradiction shows that $f^{-1}(q)$ can contain at most $m$ critical points. $\square$
