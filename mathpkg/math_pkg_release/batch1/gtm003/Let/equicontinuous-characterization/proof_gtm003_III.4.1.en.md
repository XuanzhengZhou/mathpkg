---
role: proof
locale: en
of_concept: equicontinuous-characterization
source_book: gtm003
source_chapter: "III"
source_section: "4.1"
---

The equivalence of (a), (b), and (c) is established by a cyclic argument analogous to the proof of (III, 3.3).

(a) $\Rightarrow$ (b): Suppose $H$ is equicontinuous. For any 0-neighborhood $V$ in $F$, by definition of equicontinuity at $0$, there exists a 0-neighborhood $U$ in $E$ such that $u(U) \subset V$ for all $u \in H$. Then $U \subset \bigcap_{u \in H} u^{-1}(V)$, so $\bigcap_{u \in H} u^{-1}(V)$ is a 0-neighborhood in $E$.

(b) $\Rightarrow$ (c): If $\bigcap_{u \in H} u^{-1}(V)$ is a 0-neighborhood in $E$ for each 0-neighborhood $V$ in $F$, set $U = \bigcap_{u \in H} u^{-1}(V)$. Then for all $u \in H$, $u(U) \subset V$, hence $\bigcup_{u \in H} u(U) \subset V$.

(c) $\Rightarrow$ (a): Given a 0-neighborhood $V$ in $F$, choose a 0-neighborhood $U$ in $E$ such that $\bigcup_{u \in H} u(U) \subset V$. Then for all $u \in H$, $u(U) \subset V$, which is precisely the definition of equicontinuity of $H$.

(Note: The textbook states that this proof is similar to that of (III, 3.3) and omits the details.)
