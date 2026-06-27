---
role: proof
locale: en
of_concept: locally-convex-mathfrak-s-topology
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

If \(\mathfrak{B}\) is a \(0\)-neighborhood base in \(F\) consisting of convex sets, then each \(M(S, V) = \{f : f(S) \subset V\}\) is convex (since \(V\) is convex and the condition \(f(S) \subset V\) is preserved under convex combinations). Hence by Proposition 3.1 the \(\mathfrak{S}\)-topology is locally convex if it is a vector space topology, which follows from (3.1).

To show the \(\mathfrak{S}\)-topology is Hausdorff: Let \(f \in G\) with \(f \neq 0\). Since \(f\) is continuous on \(T\) and \(\bigcup\{S : S \in \mathfrak{S}\}\) is dense in \(T\), there exists \(t_0 \in S_0 \in \mathfrak{S}\) such that \(f(t_0) \neq 0\). Since \(F\) is a Hausdorff space, there exists a \(0\)-neighborhood \(V_0 \in \mathfrak{B}\) with \(f(t_0) \notin V_0\). It follows that \(f \notin M(S_0, V_0)\). Thus every non-zero element of \(G\) is separated from \(0\), so the \(\mathfrak{S}\)-topology is Hausdorff.
