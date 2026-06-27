---
role: proof
locale: en
of_concept: compact-open-smallest-jointly-continuous
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Corollary — Compact-Open Topology is the Smallest Jointly Continuous Topology

If $X$ is locally compact, then a topology is jointly continuous on compacta if and only if it is jointly continuous. Indeed, every point of $X$ has a compact neighborhood, so joint continuity on each compact set implies joint continuity on the whole space $X$ (since continuity of $P : F \times X \to Y$ is a local property).

By Theorem 7.5, every topology which is jointly continuous on compacta is larger than the compact-open topology $\mathcal{C}$. Under local compactness, "jointly continuous on compacta" is equivalent to "jointly continuous". Hence every jointly continuous topology contains $\mathcal{C}$.

If additionally $X$ is regular and $F$ consists of continuous functions, Theorem 7.5 also guarantees that $\mathcal{C}$ itself is jointly continuous on compacta, hence jointly continuous. Therefore $\mathcal{C}$ is the smallest jointly continuous topology for $F$.
