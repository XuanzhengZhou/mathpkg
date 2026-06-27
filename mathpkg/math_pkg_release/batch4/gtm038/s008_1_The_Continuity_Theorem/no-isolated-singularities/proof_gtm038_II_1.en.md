---
role: proof
locale: en
of_concept: no-isolated-singularities
source_book: gtm038
source_chapter: "II. Domains of Holomorphy"
source_section: "1. The Continuity Theorem"
---

Without loss of generality we assume that $\zeta_0 = 0$. Let $P$ be a polycylinder about $\zeta_0$ with $P \subset B$, and set $P' := P \setminus \{\zeta_0\}$. This is precisely the situation of Theorem 1.3: $G = P \setminus \bar{P}_{r^0}$ with $r^0 = (0, \ldots, 0)$, so $G = P'$. By Theorem 1.3, there exists a holomorphic function $F'$ in $P$ with $F'|_{P'} = f|_{P'}$.

Define
$$F(\zeta) := \begin{cases} F'(\zeta) & \zeta \in P, \\ f(\zeta) & \zeta \in B'. \end{cases}$$

Since $P \cap B' = P'$ and $F'$ agrees with $f$ on $P'$, the function $F$ is well-defined. Moreover, $F$ is holomorphic on $P$ (since $F'$ is) and on $B'$ (since $f$ is). On the overlap $P' = P \cap B'$, both definitions coincide. Hence $F$ is the holomorphic continuation of $f$ to $B$.

The uniqueness follows from the identity theorem.
