---
locale: en
of_concept: the-following-diagram-is-commutative
role: proof
source_book: gtm020
source_chapter: 10. Relative K-Theory
source_section: '2'
---

For $A = B = \

isomorphism. Then there exists a triple $(\xi, u_1, u_0)$ such that $\xi$ is a vector bundle over $X$, $u_i: \xi_i \rightarrow \xi|X_i$ is an isomorphism for $i = 0, 1$, and $u_0\alpha = u_1$ over $A$. Moreover, if $(\eta, v_1, v_0)$ is a second triple with the above properties, there is an isomorphism $w: \eta \rightarrow \xi$ with $u_i = wv_i$ for $i = 0, 1$.

Proof. Let $E(\xi)$ be the space resulting from the identification of $x \in E(\xi_1|A) \subset E(\xi_1)$ with $\alpha(x) \in E(\xi_0|A) \subset E(\xi_0)$. There is a natural projection $E(\xi) \rightarrow X$ resulting from the projections of $\xi_i$, a natural vector space structure on each fibre of $\xi$, and natural bundle isomorphisms $u_i: \xi_i \rightarrow \xi|X_i$ for $i = 0, 1$.

To prove local triviality of $\xi$, we have only to find charts of $\xi$ near points $x \in A$. For $x \notin A$ the existence of local charts is clear. Let $U$ be an open neighborhood of $x$ in $X$ such that there is a retraction $r: U \cap X_0 \rightarrow U \cap A$ and such that there are maps $\phi_i: (U \cap X_i) \times F^n \rightarrow \xi_i|(U \cap X_i)$ which are local coordinate charts of $\xi_i$ over $U \cap X_i$. Over the set $U \cap A$ we have $\alpha\phi_1(x,v) = \phi_0(x,f(x)v)$, where $f: U \cap A \rightarrow GL(F^n)$ is a map. Replacing $\phi_0(x,v)$ by $\phi_0(x,f(r(x))v)$ for $(x,v) \in (U \cap X_0) \times F^n$, we can assume
