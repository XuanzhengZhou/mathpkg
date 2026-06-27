---
locale: en
of_concept: let-u-xi-rightarrow-xi-be-a-b-morphism-between-two-vector-bu
role: proof
source_book: gtm020
source_chapter: 3. Vector Bundles
source_section: '1'
---

The direct implication is immediate because the inverse of $u: p^{-1}(b) \rightarrow (p')^{-1}(b)$ is the restriction to $(p')^{-1}(b)$ of the inverse of $u$. Conversely, let $v: \xi' \rightarrow \xi$ be the function defined by the requirement that $v|(p')^{-1}(b)$ be the inverse of the restricted linear transformation $u: p^{-1}(b) \rightarrow (p')^{-1}(b)$. The function $v$ will be the desired inverse of $u$ provided $v$ is continuous. Let $U$ be an open subset of $B$, let $h: U \times F^k \rightarrow p^{-1}(U)$ be a local coordinate of $\xi$, and let $h': U \times F^k \rightarrow (p')^{-1}(U)$ be a local coordinate of $\xi'$. It suffices to prove $v: (p')^{-1}(U) \rightarrow p^{-1}(U)$ is continuous for every such $U$. By (2.3), $(h')^{-1}uh$ has the form $(b, x) \mapsto (b, f_b(x))$, where $b \mapsto f_b

Proof. The fibre $p_1^{-1}(b_1)$ of $f^*(\xi) = (E_1, p_1, B_1)$ over $b_1 \in B_1$ is $b_1 \times p^{-1}(f(b_1)) \subset E_1 \subset B_1 \times E$. For $(b_1, x), (b_1, x') \in p_1^{-1}(b_1)$, we require $(b_1, x) + (b_1, x') = (b_1, x + x')$ and $k(b_1, x) = (b_1, kx)$, where $k \in F$. Since $f_\xi(b_1, x) = x$, the restriction $f_\xi: p_1^{-1}(b_1) \rightarrow p^{-1}(b)$ is a linear isomorphism, and this requirement uniquely defines the vector space structure of $p_1^{-1}(b_1)$.

Finally, we exhibit the local triviality of $f^*(\xi)$. If $h: U \times F^k \rightarrow p^{-1}(U)$ is a vector bundle isomorphism over $U$, then $h': f^{-1}(U) \times F^k \rightarrow p_1^{-1}(f^{-1}(U))$, where $h'(b_1, x) = (b_1, h(f(b_1), x))$, is a vector bundle isomorphism over $f^{-1}(U)$.

In connection with the factorization in 2(5.5), we observe that if $(u, f): \eta \rightarrow \xi$ is a vector bundle morphism then $u$ factors as a composition $f_\xi v$, where $\eta \rightarrow f^*(\xi) \rightarrow \xi$, $v(y) = (p_\eta(y), u(y))$, and $f_\xi(b_1, x) = x$. Moreover, $v$ is a vector bundle morphism over $B(\eta)$. In view of Theorem (2.5), the $B(\eta)$-morphism $v$ is an isomorphism if and only if $v$ is an isomorphism

trivial bundles, and therefore $h$ has the form $h(x, y) = (x, g(x)y)$, where $(x, y) \in (B_1 \cap B_2) \times F^k$ and $g: A \rightarrow GL(k, F)$ is a map. We prolong $h$ to a $B_2$-isomorphism $w: B_2 \times F^k \rightarrow B_2 \times F^k$ by the formula $w(x, t, y) = (x, t, g(x)y)$ for each $x \in A, y \in F^k$, and $t \in [c, b]$. Then the bundle isomorphisms $u_1: B \times F^k \rightarrow E_1$ and $u_2 w: B_2 \times F^k \rightarrow E_2$ are equal on $(B_1 \cap B_2) \times F^k$, which is a closed set. Therefore, there exists an isomorphism $u: B \times F^k \rightarrow E$ with $u|B_1 \times F^k = u_1$ and $u|B_2 \times F^k = u_2 w$.
