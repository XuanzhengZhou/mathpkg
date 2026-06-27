---
role: proof
locale: en
of_concept: equivalence-of-ap-conditions
source_book: gtm003
source_chapter: "Chapter III"
source_section: "9. The Approximation Property. Compact Maps"
---

(a) $\Rightarrow$ (b): Given a $u \in \mathcal{L}(E)$, a precompact set $A$, and a $0$-neighborhood $V$ in $E$, we have to show the existence of $u_0 \in E' \otimes E$ such that $u(x) - u_0(x) \in V$ for all $x \in A$. Let $U$ be a $0$-neighborhood in $E$ for which $u(U) \subset V$. By (a) there exists an $e_0 \in E' \otimes E$ such that $x - e_0(x) \in U$ for all $x \in A$. Clearly, if $e_0 = \sum_{i=1}^{n} x_i' \otimes x_i$, then the map $u_0 = u \circ e_0 = \sum_{i=1}^{n} x_i' \otimes u(x_i)$ satisfies the requirement.

(b) $\Rightarrow$ (c): For each fixed $v \in \mathcal{L}(E, F)$ the mapping $u \mapsto v \circ u$ is continuous on $\mathcal{L}_c(E)$ into $\mathcal{L}_c(E, F)$. Thus since $E' \otimes E$ is dense in $\mathcal{L}_c(E)$, $E' \otimes v(E)$ is dense in a subspace of $\mathcal{L}_c(E, F)$ containing $v \circ e = v$, which establishes the assertion.

(b) $\Rightarrow$ (d): Likewise, for each fixed $w \in \mathcal{L}(F, E)$, $u \mapsto u \circ w$ is continuous on $\mathcal{L}_c(E)$ into $\mathcal{L}_c(F, E)$, since for each precompact set $B \subset F$, $w(B)$ is precompact in $E$. Thus since $E' \otimes E$ is dense in $\mathcal{L}_c(E)$, the image under $u \mapsto u \circ w$ is dense in a subspace of $\mathcal{L}_c(F, E)$ containing $e \circ w = w$.

The implications (c) $\Rightarrow$ (b) and (d) $\Rightarrow$ (b) are trivial by taking $F = E$.
