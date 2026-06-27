---
role: proof
locale: en
of_concept: schauder-adjoint-compactness
source_book: gtm003
source_chapter: "Chapter III"
source_section: "9. The Approximation Property. Compact Maps"
---

Let $U, V$ be the respective unit balls in $E, F$ and let $U^0, V^0$ be the corresponding dual unit balls in $E', F'$.

($\Rightarrow$) Assume $u$ is compact. We show that $u'(V^0) = B$ is relatively compact in $E'$. For this it suffices (since $E'$ is metric) to show that each sequence $\{x_n'\} \subset B$ has a cluster point. Let $x_n' = u'(y_n')$ ($n \in \mathbb{N}$), where $\{y_n'\} \subset V^0$. Since $V^0$ is equicontinuous and closed for $\sigma(F', F)$, it is $\sigma(F', F)$-compact by (4.3), Corollary. Hence $\{y_n'\}$ has a $\sigma(F', F)$-cluster point $y_0' \in V^0$. Let $\{n_k\}$ be such that $y_{n_k}' \to y_0'$ for $\sigma(F', F)$.

Now $u(U)$ is relatively compact in $F$; let $K = \overline{u(U)}$. The restrictions of $y_{n_k}'$ to $K$ form a sequence of continuous functions converging pointwise to the restriction of $y_0'$ on the compact set $K$. By Ascoli's theorem, this convergence is uniform on $K$. Consequently, $\sup_{x \in U} |\langle x_n' - x_0', x \rangle| = \sup_{x \in U} |\langle y_{n_k}' - y_0', u(x) \rangle| \to 0$, where $x_0' = u'(y_0')$. Hence $x_{n_k}' \to x_0'$ in $E'$, proving $B$ is relatively compact in $E'$.

($\Leftarrow$) Assume $u'$ is compact. Then $u''$ is compact by the forward implication. Identifying $E$ with a subspace of $E''$ and $F$ with a subspace of $F''$, the restriction of $u''$ to $E$ is $u$, so $u$ is compact.
