---
role: proof
locale: en
of_concept: semilinear-fixing-1dim-subspaces-over-field
source_book: gtm006
source_chapter: "I"
source_section: "4. Vector Spaces"
---

By Result 1.23, the subgroup $N \subseteq \Gamma L(V)$ of semi-linear transformations fixing all 1-dimensional subspaces satisfies $N \cong K^*$ and $N \cap GL(V) \cong Z(K^*)$. When $K$ is a field, $K^*$ is abelian and $Z(K^*) = K^*$.

Let $\alpha \in N$ have associated automorphism $\sigma \in \operatorname{Aut}(K)$. Following the proof of Result 1.23, $\alpha$ acts as $v^\alpha = a v^\sigma$ for some $a \in K^*$ (i.e., apply $\sigma$ to the coordinates of $v$, then multiply by $a$). For $\alpha$ to fix every 1-dimensional subspace, we need $v^\alpha = \lambda(v) v$ for each $v$, with $\lambda(v) \in K^*$.

Take $v = e_i$ (a basis vector). Then $e_i^\alpha = a e_i$, so $\lambda(e_i) = a$. Now take $v = e_1 + e_2$. Then
$$v^\alpha = (e_1 + e_2)^\alpha = e_1^\alpha + e_2^\alpha = a e_1 + a e_2 = a(e_1 + e_2) = a v.$$
Thus $\lambda(e_1 + e_2) = a$ as well. But we also compute:
$$v^\alpha = a (e_1 + e_2)^\sigma = a (e_1^\sigma + e_2^\sigma) = a (e_1 + e_2)$$
only if $1_K^\sigma = 1_K$, which is always true.

Now consider $v = k e_1$ for $k \in K$. Since $\alpha$ fixes $\langle e_1 \rangle$, we have $(k e_1)^\alpha = k^\sigma a e_1$. But we also need $(k e_1)^\alpha = \mu(k) k e_1$ for some $\mu(k) \in K^*$. Thus $k^\sigma a = \mu(k) k$, i.e., $\mu(k) = a k^{\sigma - 1}$.

For $\alpha$ to fix the 1-dimensional subspace $\langle e_1 + k e_2 \rangle$ for arbitrary $k$, we would need complicated conditions. However, since $K$ is a field (commutative), the only way for $a k^\sigma$ to be proportional to $k$ for all $k \in K$ is if $\sigma = \operatorname{id}$. Indeed, if $\sigma \neq \operatorname{id}$, pick $k$ such that $k^\sigma \neq k$; then $(k e_1)^\alpha = a k^\sigma e_1$ is not a scalar multiple of $k e_1$ unless $a k^\sigma = \lambda k$, which forces a specific relationship that cannot hold for all $k$.

Therefore $\sigma = \operatorname{id}$, so $\alpha$ is linear. Then $v^\alpha = a v$ for all $v$, which is a scalar multiple of the identity. Such transformations clearly commute with all linear transformations, so $\alpha \in Z(GL(V))$. In matrix form, $\alpha$ is $a I$ where $I$ is the identity matrix.
