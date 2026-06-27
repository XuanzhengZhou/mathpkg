---
role: proof
locale: en
of_concept: m-connected-2m-equivalent-statements
source_book: gtm054
source_chapter: "Chapter V"
source_section: "Section 30"
---

Observe that if $n \geq m + 1$, then all the $2m$ statements are true for $K_n$. We assume, therefore, that $\Gamma$ is not complete. The entanglement of the implications that we prove is indicated by the directed graph in Figure C18.

$B_1 \Rightarrow A$. The condition $B_1$ is precisely C8. The implication follows from Whitney's theorem (C7).

$B_k \Rightarrow C_{k-1}$ (for $k = 2, \ldots, m$). Let $S \in \mathcal{P}_{k-1}(V)$ and $\{a, z\} \in \mathcal{P}_2(V + S)$ be given. Assume $B_k$ with $z = z_1$ and $S = \{z_1, \ldots, z_k\}$. This provides an openly-disjoint $[m - (k - 1)]$-family of $az$-paths which avoid $S$.

$C_k \Rightarrow A$ (for $k = 1, \ldots, m - 1$). Let $U \subseteq V$, and suppose that $a$ is an interior vertex of $\Gamma_U$ and that $z$ is an exterior vertex of $\Gamma_U$. Let $S$ be the set of attachment vertices of $\Gamma_U$. By the definitions, every $az$-path contains a vertex in $S$.

Suppose $|S| \leq k$. By $C_k$, there exists an openly-disjoint $(m - k)$-family of $az$-paths in $\Gamma_{(S)}$, and since $m - k > 0$, this family is not empty; i.e., some $az$-path contains no vertex of $S$. Hence $|S| > k$. Let $T \in \mathcal{P}_k(S)$. Similarly, there exists an openly-disjoint $(m - k)$-family of $az$-paths in $\Gamma_{(T)}$. Since no two of these paths contain the same vertex in $S + T$, we have $m - k \leq |S + T| = |S| - k$. Hence $\Gamma_U$ has $|S| \geq m$ attachment vertices, and $\Gamma$ is $m$-connected by Exercise C16.

$A \Rightarrow B_k$ (for $k = 1, \ldots, m$) and $A \Rightarrow C_k$ (for $k = 1, \ldots, m - 1$) follow by applying Dirac's generalization of Menger's theorem.
