---
role: proof
locale: en
of_concept: compactness-by-compact-open-and-joint-continuity
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Theorem 7.6 — Compactness Relative to the Compact-Open Topology

Let $X$ be regular or Hausdorff, $Y$ Hausdorff, and $C$ the family of all functions on $X$ to $Y$ continuous on each compact subset. Let $\mathcal{C}$ and $\wp$ denote the compact-open and pointwise topologies. A subfamily $F \subset C$ is $\mathcal{C}$-compact iff:

**(Necessity):** Suppose $F$ is $\mathcal{C}$-compact. (a) Since $\mathcal{C}$ is Hausdorff (Theorem 7.4), a compact subset is closed; thus $F$ is $\mathcal{C}$-closed in $C$. (b) For each $x \in X$, the evaluation map $e_x : (F, \mathcal{C}) \to Y$, $f \mapsto f(x)$, is continuous (as $\wp \subset \mathcal{C}$). Hence $F[x] = e_x[F]$ is compact, and its closure $F[x]^-$ is compact. (c) Since $\mathcal{C}$ is jointly continuous on compacta (Theorem 7.5) and $F$ is $\mathcal{C}$-compact, $\mathcal{C} = \wp$ on $F$ by the Hausdorff property. Thus $\wp$ is jointly continuous on compacta, so by Theorem 7.5, $\mathcal{C} \subset \wp$ and hence $\mathcal{C} = \wp$. Then $\wp$ is jointly continuous on compacta.

**(Sufficiency):** Assume (a) $F$ is $\wp$-closed in $C$, (b) $F[x]^-$ is compact for each $x$, and (c) $\wp$ for $F$ is jointly continuous on compacta. Let $F^-$ be the $\wp$-closure of $F$ in $Y^X$. Condition (b) implies $F^- \subset \prod_{x \in X} F[x]^-$, which is $\wp$-compact by Tychonoff's theorem. Since $F^-$ is $\wp$-closed in this product, $F^-$ is $\wp$-compact. By (c), $\wp$ on $F^-$ is jointly continuous on compacta, so every member of $F^-$ is continuous on each compactum; thus $F^- \subset C$. Theorem 7.5 gives $\mathcal{C} \subset \wp$ on $F^-$, so $\mathcal{C} = \wp$ on $F^-$. By (a), $F$ is $\wp$-closed in $C$, hence $\wp$-closed in $F^-$, so $F^- = F$. Therefore $F$ is $\wp$-compact, and thus $\mathcal{C}$-compact.
