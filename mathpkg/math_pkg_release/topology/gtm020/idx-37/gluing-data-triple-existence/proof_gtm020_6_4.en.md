---
role: proof
locale: en
of_concept: gluing-data-triple-existence
source_book: gtm020
source_chapter: "6"
source_section: "6.4"
---

Let $E(\xi)$ be the space resulting from the identification of $x \in E(\xi_1|A) \subset E(\xi_1)$ with $\alpha(x) \in E(\xi_0|A) \subset E(\xi_0)$. There is a natural projection $E(\xi) \to X$ resulting from the projections of $\xi_i$, a natural vector space structure on each fibre of $\xi$, and natural bundle isomorphisms $u_i: \xi_i \to \xi|_{X_i}$ for $i = 0, 1$.

To prove local triviality of $\xi$, we have only to find charts of $\xi$ near points $x \in A$. For $x \notin A$ the existence of local charts is clear. Let $U$ be an open neighborhood of $x$ in $X$ such that there is a retraction $r: U \cap X_0 \to U \cap A$ and such that there are maps $\phi_i: (U \cap X_i) \times F^n \to \xi_i|_{(U \cap X_i)}$ which are local coordinate charts of $\xi_i$ over $U \cap X_i$. Over the set $U \cap A$ we have $\alpha\phi_1(x,v) = \phi_0(x, f(x)v)$, where $f: U \cap A \to GL(F^n)$ is a map. Replacing $\phi_0(x,v)$ by $\phi_0(x, f(r(x))v)$ for $(x,v) \in (U \cap X_0) \times F^n$, we can assume that $\alpha\phi_1 = \phi_0$ over $U \cap A$, which yields local charts for $\xi$ near $x \in A$.

The uniqueness statement follows from the universal property of the identification space: the morphism $w$ is uniquely determined by the requirement $u_i = w v_i$ for $i = 0, 1$, and if $v_0$ and $v_1$ are isomorphisms, then $w$ is an isomorphism.
