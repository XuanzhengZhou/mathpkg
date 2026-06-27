---
role: proof
locale: en
of_concept: tangent-bundle-is-smooth-manifold
source_book: gtm014
source_chapter: "1"
source_section: "3"
---

**Proof.**

Let $p \in X$, let $U$ be an open neighborhood of $p$ in $X$, and let $\phi$ be a chart with domain $U$. Set $T_U X = \pi^{-1}(U)$. Define
$$
\tilde{\phi} \colon T_U X \to \phi(U) \times \mathbf{R}^n
$$
by
$$
\tilde{\phi}(\alpha) = \bigl( \phi \circ \pi(\alpha),\, (\lambda_{\phi}^{\pi(\alpha)})^{-1}(\alpha) \bigr)
$$
for every $\alpha \in T_U X$. The map $\tilde{\phi}$ is bijective: an inverse is given by
$$
(v, q) \mapsto \lambda_{\phi}^{\phi^{-1}(v)}(q).
$$

If $\{\phi_\beta\}$ is a $C^k$ atlas on $X$, we topologize $TX$ by declaring a subset $V \subset TX$ to be open if $\tilde{\phi}_\beta(V \cap T_{U_\beta} X)$ is open in $\mathbf{R}^{2n}$ for every $\beta$. This makes each $\tilde{\phi}_\beta$ a homeomorphism onto its image.

To check that the transition maps are differentiable, let $\phi, \psi$ be two charts with overlapping domains. For $q \in \phi(U_\phi \cap U_\psi) \subset \mathbf{R}^n$ and $v \in \mathbf{R}^n$,
$$
\tilde{\psi} \circ \tilde{\phi}^{-1}(q, v) = \bigl( \psi \circ \phi^{-1}(q),\, d(\psi \circ \phi^{-1})_q(v) \bigr).
$$
Since $X$ is $C^k$, the transition map $\psi \circ \phi^{-1}$ is $C^k$, so its derivative $d(\psi \circ \phi^{-1})$ is $C^{k-1}$. Consequently, $\tilde{\psi} \circ \tilde{\phi}^{-1}$ is $C^{k-1}$, and thus $\{\tilde{\phi}_\beta\}$ forms a $C^{k-1}$ atlas on $TX$. The dimension of $TX$ is $\dim(\mathbf{R}^n \times \mathbf{R}^n) = 2n$.
