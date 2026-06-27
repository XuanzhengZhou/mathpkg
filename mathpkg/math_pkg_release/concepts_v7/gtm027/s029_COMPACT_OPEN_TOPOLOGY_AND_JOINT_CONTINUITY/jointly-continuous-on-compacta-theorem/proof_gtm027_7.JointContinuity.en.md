---
role: proof
locale: en
of_concept: jointly-continuous-on-compacta-theorem
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Theorem 7.5 — Jointly Continuous on Compacta and the Compact-Open Topology

**First assertion:** Suppose a topology $\mathcal{J}$ for $F$ is jointly continuous on compacta. Let $K \subset X$ be compact and $U \subset Y$ be open. We must show $W(K, U) \in \mathcal{J}$. For any $f \in W(K, U)$, we have $(f, x) \in P^{-1}[U]$ for all $x \in K$, where $P(f, x) = f(x)$. Since $\mathcal{J}$ is jointly continuous on $K$, the restriction $P|_{F \times K}$ is continuous. Thus for each $x \in K$ there exist a $\mathcal{J}$-neighborhood $G_x$ of $f$ and a neighborhood $M_x$ of $x$ in $K$ such that $G_x \times M_x \subset P^{-1}[U]$. Compactness of $K$ yields a finite subcover $\{M_{x_i}\}$; letting $G = \bigcap_i G_{x_i}$ gives a $\mathcal{J}$-neighborhood of $f$ contained in $W(K, U)$. Hence $W(K, U) \in \mathcal{J}$, so $\mathcal{J} \supset \mathcal{C}$.

**Second assertion:** Assume $X$ is regular or Hausdorff and each $f \in F$ is continuous on every compact subset of $X$. Let $K \subset X$ be compact, $x \in K$, $U \subset Y$ open, and $(f, x) \in P^{-1}[U]$. Since $f$ is continuous on $K$, there exists a compact neighborhood $M$ of $x$ in $K$ such that $f[M] \subset U$ (using that $X$ is either Hausdorff or regular to obtain such $M$). Then $W(M, U) \times M$ is a neighborhood of $(f, x)$ in $F \times K$ contained in $P^{-1}[U]$. Thus $\mathcal{C}$ is jointly continuous on $K$, and hence jointly continuous on compacta.
