---
role: proof
locale: en
of_concept: interior-point-of-cone-is-order-unit
source_book: gtm003
source_chapter: "V. Order Structures"
source_section: "6. The Order Topology"
---

If $e$ is an interior point of $C$ in an ordered t.v.s., then there exists a circled $0$-neighborhood $U$ with $e + U \subset C$. For any $x \in L$, there exists $\lambda > 0$ such that $\lambda x \in U$, whence $e \pm \lambda x \in C$. Thus $-\lambda x \leq e \leq$,  i.e., $x \in \lambda^{-1}[-e, e]$, proving that $e$ is an order unit.

Conversely, if $e$ is an order unit, then $[-e, e]$ absorbs every order interval, and its gauge generates $\mathfrak{T}_0$ (by the proof of Theorem 6.2 when $L$ is Archimedean). The set $\{x : p_e(x) < 1\}$ is a $\mathfrak{T}_0$-neighborhood contained in $[-e, e] \subset C - e$, so $e$ is interior to $C$ in $\mathfrak{T}_0$.
