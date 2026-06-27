---
role: proof
locale: en
of_concept: tractable-equational-presentation-is-algebraic
source_book: gtm026
source_chapter: "1"
source_section: "1.26"
---

**Proof.** We use 1.24. It suffices to show that $U$ creates limits and that $U$ creates quotients of congruences.

**$U$ creates limits.** Let $(\Delta, D)$ be a diagram of $(\Omega, E)$-algebras and write $D_i = (X_i, \delta_i)$. Assume that $(L, \psi)$ is a limit of $DU$ in $\mathbf{Set}$. Let $\omega \in \Omega_n$. If $\alpha \in \Delta(i, j)$ we have a commutative diagram showing that $(\psi_i^n \cdot \delta_{i,\omega}) \cdot D_\alpha = \psi_j^n \cdot \delta_{j,\omega}$, i.e., that $(L^n, \psi^n \cdot \delta_{-,\omega})$ is a lower bound of $DU$. It follows that there exists unique $\delta_\omega: L^n \rightarrow L$ such that $\delta_\omega \cdot \psi_i = \psi_i^n \cdot \delta_{i,\omega}$ for all $i$; or, in other words, there exists a unique $\Omega$-algebra structure $\delta$ on $L$ such that $\psi_i: (L, \delta) \rightarrow (X_i, \delta_i)$ is an $\Omega$-homomorphism for all $i$. If $p, q: U^m \rightarrow U$ with $\{p, q\} \in E$ then for all $i$ we have $(L, \delta)p \cdot \psi_i = \psi_i^n \cdot (X_i, \delta_i)p = \psi_i^n \cdot (X_i, \delta_i)q = (L, \delta)q \cdot \psi_i$, so by the collective monicity of limits (1.20), $(L, \delta)p = (L, \delta)q$, proving $(L, \delta)$ satisfies $E$.

**$U$ creates quotients of congruences.** Let $R$ be a congruence on the $(\Omega, E)$-algebra $(X, \delta)$ with coordinate projections $p, q: R \longrightarrow X$. By definition (1.11) there exists an $(\Omega, E)$-structure $(R, \gamma)$ such that $p, q: (R, \gamma) \longrightarrow (X, \delta)$ are $\Omega$-homomorphisms. For each $\omega \in \Omega_n$, define $\bar{\delta}_{\omega}: (X/R)^n \longrightarrow X/R$ by $(x_i\theta)\bar{\delta}_{\omega} = (x_i)\delta_{\omega}\theta$. If $(x_i, y_i) \in R^n$ then $(x_i)\delta_{\omega} = (x_i, y_i)p^n\delta_{\omega} = (x_i, y_i)\gamma_{\omega}p$ and $(y_i)\delta_{\omega} = (x_i, y_i)\gamma_{\omega}q$ similarly, so $((x_i)\delta_{\omega}, (y_i)\delta_{\omega}) = (x_i, y_i)\gamma_{\omega} \in R$, which proves that $\bar{\delta}_{\omega}$ is well defined. As $\theta^n: X^n \longrightarrow (X/R)^n$ is onto, $\bar{\delta}$ is the unique $\Omega$-algebra structure on $X/R$ making $\theta$ an $\Omega$-homomorphism. The facts that $(X/R, \bar{\delta})$ satisfies $E$ and that $\theta: (X, \delta) \longrightarrow (X/R, \bar{\delta})$ is co-optimal both follow from the fact that $\theta^n$ is onto for every set $n$. $\square$
