---
role: proof
locale: en
of_concept: isomorphism-criterion-for-vector-bundle-b-morphism
source_book: gtm020
source_chapter: "2"
source_section: "2.5"
---

The direct implication is immediate because the inverse of $u: p^{-1}(b) \to (p')^{-1}(b)$ is the restriction to $(p')^{-1}(b)$ of the inverse of $u$.

Conversely, let $v: \xi' \to \xi$ be the function defined by the requirement that $v|_{(p')^{-1}(b)}$ be the inverse of the restricted linear transformation $u: p^{-1}(b) \to (p')^{-1}(b)$. The function $v$ will be the desired inverse of $u$ provided $v$ is continuous.

Let $U$ be an open subset of $B$, let $h: U \times F^k \to p^{-1}(U)$ be a local coordinate of $\xi$, and let $h': U \times F^k \to (p')^{-1}(U)$ be a local coordinate of $\xi'$. It suffices to prove that $v: (p')^{-1}(U) \to p^{-1}(U)$ is continuous for every such $U$.

By the local representation of a $B$-morphism (2.3), $(h')^{-1}uh$ has the form $(b, x) \mapsto (b, f_b(x))$, where $b \mapsto f_b$ is a map from $U$ to $\operatorname{GL}(k, F)$. Since $u|_{p^{-1}(b)}$ is an isomorphism for each $b$, the linear map $f_b$ is invertible for each $b \in U$. The inverse $v$ is then locally given by $(h)^{-1}v h'$, which maps $(b, y) \mapsto (b, f_b^{-1}(y))$. The continuity of $v$ follows from the continuity of the map $b \mapsto f_b$ and the continuity of the inversion map $\operatorname{GL}(k, F) \to \operatorname{GL}(k, F)$.
