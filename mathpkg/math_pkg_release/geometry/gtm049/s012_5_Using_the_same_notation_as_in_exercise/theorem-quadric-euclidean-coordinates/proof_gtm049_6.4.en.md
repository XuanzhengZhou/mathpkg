---
role: proof
locale: en
of_concept: theorem-quadric-euclidean-coordinates
source_book: gtm049
source_chapter: "6"
source_section: "6.4"
---

Our theorem differs from Proposition 12 of Chapter V only in the fact that the required coordinate system must be euclidean. Our proof is a refinement of the proof of the earlier proposition.

Let $\mathcal{P}(V)$ be an $n$-dimensional real projective geometry, $H$ a hyperplane in $\mathcal{P}(V)$ and $\sigma$ a positive definite bilinear form on $H$. We may suppose our euclidean geometry to be $\mathcal{A}(c + H, d)$ for some $c$ not in $H$ and $d$ the distance determined by $\sigma$. The given quadric, say $R$, is the cross-section by $\mathcal{A}(c + H)$ of a suitable projective quadric $Q(\tau)$ in $\mathcal{P}(V)$.

Our aim is to find an ordered basis $(a_0, \ldots, a_n)$ of $V$ adapted to $\tau$ and such that $a_0 \in c + H$ and $(a_1, \ldots, a_n)$ is a cartesian basis of $(H, \sigma)$. For then $a_0 + a_1, \ldots, a_0 + a_n, a_0$ will be vectors for a euclidean frame of reference of $\mathcal{A}(c + H, d)$. If $f(X_0, \ldots, X_n) = 0$ is the equation of $Q(\tau)$ then $f(1, X_1, \ldots, X_n) = 0$ is the equation of $R$ with respect to this euclidean frame of reference.

In the following argument we shall write $\perp$ for $\perp(\tau)$.

(i) If $H^\perp \not\subset H$, we may find a vector $a_0$ in $H^\perp \cap c + H$. Choose a cartesian basis $(a_1, \ldots, a_n)$ of $(H, \sigma)$ with the property that $\tau(a_i, a_j) = 0$ whenever $i \neq j$ ($i, j = 1, \ldots, n$). (Such a basis exists by Theorem 1.) The basis $(a_0, \ldots, a_n)$ then satisfies the required conditions.

(ii) If $H^\perp \subset H$, consider first the case where $\tau$ is non-degenerate. For then $[a_1] = H^{\perp(\tau)}$ and $K = [a_1]^{\perp(\sigma)}$ are uniquely determined once $\tau$ is given. In the general case one can find a subspace $N$ which has $(V^{\perp(\tau)})^{\perp(\sigma)}$ as hyperplane at infinity; then $V = V^{\perp(\tau)} \oplus N$ and one can treat the restriction of $\tau$ to $N$ as above.
