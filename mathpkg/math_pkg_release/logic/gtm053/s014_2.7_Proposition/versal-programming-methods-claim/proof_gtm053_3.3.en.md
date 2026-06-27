---
role: proof
locale: en
of_concept: versal-programming-methods-claim
source_book: gtm053
source_chapter: "3"
source_section: "3.3"
---
Identify $U, V$ with $\mathbf{Z}^+$ (since any infinite object is isomorphic to $\mathbf{Z}^+$). Consider evaluation morphisms $\text{ev} : P \times \mathbf{Z}^+ \rightarrow \mathbf{Z}^+$. Such a morphism computes all recursive functions $\mathbf{Z}^+ \rightarrow \mathbf{Z}^+$ iff it is a versal family in the sense of V.5.7.

Now consider another versal family of recursive functions of two variables $P \times \mathbf{Z}^+ \rightarrow \mathbf{Z}^+$. Let $P'$ be its base: $\text{Ev} : P' \times P \times \mathbf{Z}^+ \rightarrow \mathbf{Z}^+$. Then the programming method $(Q := P' \times P, \text{Ev})$ is versal, since versality of $\text{Ev}$ implies that for any $\text{ev} : P \times U \rightarrow V$, there exists $p' \in P'$ such that $\text{Ev}(p', p, u) = \text{ev}(p, u)$.
