---
role: proof
locale: en
of_concept: tvs-under-mathfrak-s-topology
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

For each \(S \in \mathfrak{S}\), the set \(H(S) = \{f \in G : f(S) \text{ is bounded in } F\}\) is a linear subspace of \(F^T\). Since \(G \subset \bigcap_{S \in \mathfrak{S}} H(S)\) by hypothesis and the \(\mathfrak{S}\)-topology is defined by the neighborhoods \(M(S, V) = \{f : f(S) \subset V\}\), it suffices to verify the continuity of addition and scalar multiplication.

Let \(V\) be a \(0\)-neighborhood in \(F\) and choose a circled \(0\)-neighborhood \(W\) with \(W + W \subset V\). For \(f, g \in G\) and \(S \in \mathfrak{S}\), if \(f(S) \subset W\) and \(g(S) \subset W\), then \((f+g)(S) \subset W + W \subset V\), so addition is continuous.

For scalar multiplication: given \(\lambda_0 \in K\), \(f_0 \in G\), \(S \in \mathfrak{S}\), and a \(0\)-neighborhood \(V\) in \(F\), choose a circled \(0\)-neighborhood \(W\) with \(W + W + W \subset V\) and \(f_0(S) \subset \lambda W\) for some \(\lambda > 0\) (since \(f_0(S)\) is bounded). Then for \(\lambda\) near \(\lambda_0\) and \(f \in f_0 + M(S, W)\), we have \((\lambda f)(S) \subset \lambda_0 f_0(S) + (\lambda - \lambda_0)f_0(S) + \lambda(f(S) - f_0(S)) \subset V\), establishing continuity of scalar multiplication. The simple convergence topology is coarser since each finite subset is contained in some \(S \in \mathfrak{S}\) (after embedding into the directed family).
