---
role: proof
locale: en
of_concept: free-category-universal-property
source_book: gtm005
source_chapter: "I"
source_section: "7"
---

For an $O$-graph $G$, the free category $F(G)$ has objects $\operatorname{Ob}(G)$ and arrows are finite composable paths of edges from $G$ (with empty paths as identities). Composition is path concatenation.

Universal property: There is a graph morphism $\eta_G: G \to U(F(G))$ (embedding edges as length-1 paths). For any graph morphism $\phi: G \to U(C)$ to a category $C$, there exists a unique functor $\hat{\phi}: F(G) \to C$ with $U(\hat{\phi}) \circ \eta_G = \phi$.

Define $\hat{\phi}$ on objects as $\phi$; on a path $f_n \circ \cdots \circ f_1$ (composition in $F(G)$), set $\hat{\phi}(f_n \circ \cdots \circ f_1) = \phi(f_n) \circ \cdots \circ \phi(f_1)$ (composition in $C$). This is well-defined by associativity in $C$, and uniqueness follows since any functor extending $\phi$ must map paths to the corresponding composites.
