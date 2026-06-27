---
role: proof
locale: en
of_concept: product-complex-manifold
source_book: gtm038
source_chapter: "V"
source_section: "V.3 Examples of Complex Manifolds"
---

With the sets $W = W_1 \times \cdots \times W_\ell$, where each $W_i \subset X_i$ is open, taken as the basis for the topology of $X$, the Cartesian product $X = X_1 \times \cdots \times X_\ell$ becomes a Hausdorff space (the product of Hausdorff spaces is Hausdorff).

For any point $x_0 = (x_1, \ldots, x_\ell) \in X$, there exist neighborhoods $U_i(x_i) \subset X_i$ and isomorphisms $\varphi_i: (U_i, \mathcal{H}_i) \to (B_i, \mathcal{O}_i)$ where each $B_i$ is a polydisc in $\mathbb{C}^{n_i}$. Define
$$U := U_1 \times \cdots \times U_\ell, \quad \tilde{\varphi} := \tilde{\varphi}_1 \times \cdots \times \tilde{\varphi}_\ell: U \to B := B_1 \times \cdots \times B_\ell$$
by
$$(\tilde{\varphi}_1 \times \cdots \times \tilde{\varphi}_\ell)(x'_1, \ldots, x'_\ell) := (\tilde{\varphi}_1(x'_1), \ldots, \tilde{\varphi}_\ell(x'_\ell)).$$

Then $(U, \tilde{\varphi}_1 \times \cdots \times \tilde{\varphi}_\ell)$ is a complex coordinate system at $x_0$. If $(V, \tilde{\psi}_1 \times \cdots \times \tilde{\psi}_\ell)$ is another such coordinate system, the transition map
$$(\tilde{\varphi}_1 \times \cdots \times \tilde{\varphi}_\ell) \circ (\tilde{\psi}_1 \times \cdots \times \tilde{\psi}_\ell)^{-1} = (\tilde{\varphi}_1 \circ \tilde{\psi}_1^{-1}) \times \cdots \times (\tilde{\varphi}_\ell \circ \tilde{\psi}_\ell^{-1})$$
is holomorphic because each component $\tilde{\varphi}_i \circ \tilde{\psi}_i^{-1}$ is holomorphic (the $\varphi_i$ are isomorphisms of ringed spaces). Therefore $X$ is an $n$-dimensional complex manifold with $n = \sum_{i=1}^\ell n_i$.

To verify that the projection $p_i: X \to X_i$ is holomorphic, let $W \subset X_i$ be open and $g$ holomorphic on $W$. Then $p_i^{-1}(W) = X_1 \times \cdots \times X_{i-1} \times W \times X_{i+1} \times \cdots \times X_\ell$, and the pullback $g \circ p_i$ is holomorphic on $p_i^{-1}(W)$ (it is constant in the other variables and holomorphic in the $i$-th variable), which establishes that the projection is a holomorphic mapping.
