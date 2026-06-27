---
role: proof
locale: en
of_concept: uniform-structures-equicontinuous
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

Let \(A\) be a total subset of \(E\) and let \(S\) be a precompact subset of \(E\). Given a \(0\)-neighborhood \(V\) in \(F\), choose a circled \(0\)-neighborhood \(W\) with \(W + W + W \subset V\). By equicontinuity of \(H\), there exists a \(0\)-neighborhood \(U\) in \(E\) such that \(u(U) \subset W\) for all \(u \in H\).

Since \(S\) is precompact, there exist finitely many points \(y_i \in S\) (\(i = 1, \ldots, m\)) such that \(S \subset \bigcup_i (y_i + U)\). Since the linear hull of \(A\) is dense in \(E\), there exist \(x_{ij} \in A\) and scalars \(\lambda_{ij}\) such that each \(y_i \in \sum_j \lambda_{ij} x_{ij} + U\). Then:
\[
S \subset \bigcup_{i=1}^m \left( \sum_{j=1}^n \lambda_{ij} x_{ij} + U + U \right).
\]

Choose a circled \(0\)-neighborhood \(V_0\) in \(F\) with \(\sum_{i,j} (\lambda_{ij} V_0) \subset W\), and let \(S_0 = \{x_{ij}\}\) be the finite set. If \(v \in M(S_0, V_0)\), then \(v(x_{ij}) \in V_0\) and
\[
v(S) \subset \bigcup_i \sum_j (\lambda_{ij} V_0) + v(U) + v(U) \subset W + v(U) + v(U).
\]

For \(u_0 \in H\) and \(w \in H \cap [u_0 + M(S_0, V_0)]\), write \(w = u_0 + v\) with \(v \in M(S_0, V_0)\). Then \(v(U) \subset w(U) + u_0(U) \subset W + W\) (since \(U\) is circled). Thus \(v(S) \subset W + W + W \subset V\), so \(w \in u_0 + M(S, V)\). This shows the two uniformities coincide on \(H\).
