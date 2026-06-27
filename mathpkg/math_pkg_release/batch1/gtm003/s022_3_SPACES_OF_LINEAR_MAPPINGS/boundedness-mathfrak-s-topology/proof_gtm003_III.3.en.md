---
role: proof
locale: en
of_concept: boundedness-mathfrak-s-topology
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

(a) \(\Rightarrow\) (b): Let \(H\) be bounded for the \(\mathfrak{S}\)-topology. Given a circled \(0\)-neighborhood \(V\) in \(F\) and \(S \in \mathfrak{S}\), choose \(\lambda > 0\) such that \(H \subset \lambda M(S, V)\). Then for each \(u \in H\) and \(x \in S\), \(u(x) \in \lambda V\), so \(S \subset \lambda \bigcap_{u \in H} u^{-1}(V)\).

(b) \(\Rightarrow\) (c): If \(S \in \mathfrak{S}\) and a circled \(0\)-neighborhood \(V\) in \(F\) are given, then \(S \subset \lambda \bigcap_{u \in H} u^{-1}(V)\) implies \(u(S) \subset \lambda V\) for all \(u \in H\); hence \(\bigcup_{u \in H} u(S)\) is bounded in \(F\).

(c) \(\Rightarrow\) (a): For given \(S\) and \(V\), the existence of \(\lambda\) such that \(u(S) \subset \lambda V\) for all \(u \in H\) implies \(H \subset \lambda M(S, V)\); hence \(H\) is bounded for the \(\mathfrak{S}\)-topology.
