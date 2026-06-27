---
role: proof
locale: en
of_concept: functorial-vector-bundle
source_book: gtm014
source_chapter: "5"
source_section: "5. Vector Bundles"
---

*Proof.* The proof proceeds in four steps.

(1) First consider the case where $E = X \times V$ is a product (trivial) bundle. Then define $T(E) = X \times T(V)$, which is clearly a product bundle with fiber $T(V)$ over $X$.

(2) Suppose $\phi: E \to F$ is an isomorphism of product bundles $X \times V \to X \times W$. Then $\psi = \phi$ and $\psi \circ \phi^{-1}: X \times V \to X \times W$ is an isomorphism. This map can be identified with $\lambda: X \to \operatorname{Hom}(V, W)$ given by $\lambda(p) = \psi \circ \phi^{-1}|_{\{p\} \times V}: V \to W$. Since $\psi \circ \phi^{-1}$ is smooth, the map $\lambda$ is smooth. Then $T(\psi \circ \phi^{-1}): X \times T(V) \to X \times T(W)$ can be identified with $T \circ \lambda$, and since $T$ is a smooth functor, $T \circ \lambda$ is smooth. Hence $T(\psi \circ \phi^{-1})$ is smooth and an isomorphism.

(3) Let $E$ be an arbitrary trivial bundle with two product structures $\phi: E \to X \times V$ and $\psi: E \to X \times W$ (corresponding to two choices of trivialization). By step (2), the map $T(\psi \circ \phi^{-1}): X \times T(V) \to X \times T(W)$ is a smooth isomorphism. The diagram

$$\begin{array}{ccc}
T(E) & \xrightarrow{T(\phi)} & T(X \times V) \\
\operatorname{id} \downarrow & & \downarrow T(\psi \circ \phi^{-1}) \\
T(E) & \xrightarrow{T(\psi)} & T(X \times W)
\end{array}$$

commutes, which implies that the identity map on $T(E)$ is smooth as a map between the two possible vector bundle structures induced by the two trivializations. Thus the two structures are the same, establishing uniqueness for trivial bundles.

(4) Finally, let $E$ be an arbitrary vector bundle. For each $p \in X$, choose an open neighborhood $U_p$ such that $E|_{U_p}$ is a trivial bundle. By step (3), $T(E|_{U_p})$ has a unique vector bundle structure. If $U_p \cap U_q \neq \varnothing$, then $T(E|_{U_p \cap U_q})$ inherits two vector bundle structures, namely $T(E|_{U_p})|_{U_p \cap U_q}$ and $T(E|_{U_q})|_{U_p \cap U_q}$. The uniqueness established in step (3) for the trivial bundle $E|_{U_p \cap U_q}$ implies these two structures coincide. Therefore the local structures patch together to give a unique global vector bundle structure on $T(E)$. $\square$

*Note.* The same reasoning holds when $T$ is contravariant, or when $T$ is a functor of several variables with any mixture of variance.
