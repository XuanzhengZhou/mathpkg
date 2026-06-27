---
role: proof
locale: en
of_concept: whitney-sum-tangent-bundle
source_book: gtm051
source_chapter: "5"
source_section: "5.6"
---

**Proof.** The construction is exactly analogous to the proof that the tangent bundle $TM$ is a differentiable manifold (Proposition 5.5.5). As with $TM$, the differentiable structure of $TM \oplus TM$ is completely determined by the differentiable structure of $M$.

Given an atlas $(u_\alpha, M_\alpha)_{\alpha \in A}$ for $M$, each chart $u_\alpha: M_\alpha \to U_\alpha \subset \mathbb{R}^2$ induces a map
$$Tu_\alpha: TM_\alpha \to U_\alpha \times \mathbb{R}^2, \quad X \in T_pM \mapsto (u_\alpha(p), X_\alpha)$$
where $X_\alpha$ is the representative of $X$ with respect to the chart. The transition maps
$$Tu_\beta \circ (Tu_\alpha)^{-1}: (u_\alpha(p), X_\alpha) \mapsto (u_\beta(p), X_\beta) = (u_\beta \circ u_\alpha^{-1}(u_\alpha(p)), d(u_\beta \circ u_\alpha^{-1})_{u_\alpha(p)} X_\alpha)$$
are differentiable, so $\{(Tu_\alpha, TM_\alpha)\}$ forms an atlas for $TM$.

For the Whitney sum, we apply the same construction fiberwise: for each chart $(u_\alpha, M_\alpha)$, define
$$Tu_\alpha \oplus Tu_\alpha: TM_\alpha \oplus TM_\alpha \to U_\alpha \times \mathbb{R}^2 \times \mathbb{R}^2, \quad (X,Y) \mapsto (u_\alpha(p), X_\alpha, Y_\alpha).$$
The transition maps are
$$(Tu_\beta \oplus Tu_\beta) \circ (Tu_\alpha \oplus Tu_\alpha)^{-1}(u_\alpha(p), X_\alpha, Y_\alpha) = (u_\beta \circ u_\alpha^{-1}(u_\alpha(p)), d(u_\beta \circ u_\alpha^{-1}) X_\alpha, d(u_\beta \circ u_\alpha^{-1}) Y_\alpha),$$
which are differentiable since $u_\beta \circ u_\alpha^{-1}$ is a diffeomorphism. Hence $\{(Tu_\alpha \oplus Tu_\alpha, TM_\alpha \oplus TM_\alpha)\}$ is a differentiable atlas for $TM \oplus TM$, making it a $6$-dimensional manifold. $\square$
