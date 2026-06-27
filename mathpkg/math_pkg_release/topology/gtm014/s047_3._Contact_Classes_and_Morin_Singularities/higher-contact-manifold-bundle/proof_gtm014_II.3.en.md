---
role: proof
locale: en
of_concept: higher-contact-manifold-bundle
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

Recall how the manifold structure of $G_{l,n}$ is obtained. We assume that $\mathbf{R}^n$ comes equipped with an inner product. Then a neighborhood of $V$ in $G_{l,n}$ is given by
$$
\mathcal{O}_V = \{ W \in G_{l,n} \mid \pi_V: W \to V \text{ is a bijection} \}
$$
where $\pi_V: \mathbf{R}^n \to V$ is orthogonal projection. We then identify $\operatorname{Hom}(V, V^\perp)$ with $\mathcal{O}_V$ by the mapping $A \mapsto \operatorname{graph} A$.

We claim that we can identify $\rho^{-1}(\mathcal{O}_V)$ with $\mathcal{O}_V \times F$ (where $V = \mathbf{R}^l$ in the definition of $F$). Given a submanifold germ $A$, there exists a unique germ of a smooth map $f: T_0 A \to (T_0 A)^\perp$ such that $A = \operatorname{graph} f$. Two submanifold germs $A$ and $B$ which are tangent at $0$ (i.e., $T_0 A = T_0 B$) have $k$th-order contact if and only if their defining functions $f$ and $g$ have the same $k$-jet at $0$. Thus, fixing the tangent space $V = T_0 A$, the set of $k$th-order contact elements with tangent space $V$ is parameterized by $k$-jets of maps $V \to V^\perp$ at $0$, modulo the action that identifies jets differing by a diffeomorphism of the source. This fiber is precisely $F$, the fiber of $J^k(\mathbf{R}^l, \mathbf{R}^{n-l})_{0,0} \to J^1(\mathbf{R}^l, \mathbf{R}^{n-l})_{0,0}$ (the higher-order terms beyond the first derivative).

The local product structure $\rho^{-1}(\mathcal{O}_V) \cong \mathcal{O}_V \times F$ gives $H_{k,l}^n$ the structure of a fiber bundle over $G_{l,n}$ with typical fiber $F$, establishing the lemma.

(Note: The original OCR text contains a gap between the end of Lemma 3.7 and the definition of $H_{1,l}^n$ preceding Lemma 3.9. The fragment "$(d\psi)_0(T_0B) = 0)$. Thus we may identify $H_{1,l}^n$ with the Grassmann manifold..." indicates the text lost the definition of $H_{k,l}^n$ and the statement that $H_{1,l}^n \cong G_{l,n}$.)
