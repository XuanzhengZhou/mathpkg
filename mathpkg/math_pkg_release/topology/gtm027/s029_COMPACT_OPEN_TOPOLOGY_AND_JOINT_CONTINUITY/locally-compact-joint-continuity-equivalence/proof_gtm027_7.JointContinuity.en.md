---
role: proof
locale: en
of_concept: locally-compact-joint-continuity-equivalence
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Corollary — Locally Compact Spaces: Joint Continuity Equals Joint Continuity on Compacta

Let $X$ be locally compact. We show that a topology for $F$ is jointly continuous if and only if it is jointly continuous on compacta.

($\Rightarrow$) If $P : F \times X \to Y$ is continuous, then for any compact $K \subset X$, the restriction $P|_{F \times K}$ is continuous. Hence joint continuity implies joint continuity on compacta.

($\Leftarrow$) Conversely, suppose the topology is jointly continuous on compacta. Let $(f, x) \in F \times X$ and let $U \subset Y$ be an open neighborhood of $f(x)$. Since $X$ is locally compact, $x$ has a compact neighborhood $K$. By joint continuity on $K$, the map $P|_{F \times K}$ is continuous. Thus there exist a neighborhood $G$ of $f$ in $F$ and a neighborhood $V$ of $x$ in $K$ (which is also a neighborhood in $X$ since $K$ is a neighborhood) such that $P[G \times V] \subset U$. Hence $P$ is continuous at $(f, x)$, establishing joint continuity.

Therefore, for locally compact $X$, joint continuity and joint continuity on compacta are equivalent.
