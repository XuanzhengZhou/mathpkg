---
role: proof
locale: en
of_concept: homomorphism-uniform-continuity
source_book: gtm015
source_chapter: "5"
source_section: "Uniformity in topological groups"
---

# Proof of Continuity equals uniform continuity for group homomorphisms

Let $G$ and $H$ be topological groups, each equipped with its left uniform structure, and let $f: G \rightarrow H$ be a group homomorphism. We must show that $f$ is continuous if and only if it is uniformly continuous.

Recall from (5.1) the characterization of continuity for a homomorphism $f$ in terms of neighborhoods of the neutral element: $f$ is continuous if and only if for every neighborhood $V$ of $e_H$, there exists a neighborhood $U$ of $e_G$ such that $f(U) \subset V$.

The condition (d) of (5.1) states precisely: given any neighborhood $V$ of $e_H$, there exists a neighborhood $U$ of $e_G$ such that $x^{-1}y \in U$ implies $f(x)^{-1}f(y) \in V$.

But $x^{-1}y \in U$ means $(x, y) \in U_s$, and $f(x)^{-1}f(y) \in V$ means $(f(x), f(y)) \in V_s$. Therefore the condition is exactly:

$$(x, y) \in U_s \implies (f(x), f(y)) \in V_s,$$

which is precisely the definition of uniform continuity of $f$ with respect to the left uniform structures. Thus continuity of $f$ (at $e$) is equivalent to uniform continuity of $f$.
