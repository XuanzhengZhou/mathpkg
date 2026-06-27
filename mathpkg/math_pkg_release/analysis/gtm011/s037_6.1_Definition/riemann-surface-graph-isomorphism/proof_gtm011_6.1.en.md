---
role: proof
locale: en
of_concept: riemann-surface-graph-isomorphism
source_book: gtm011
source_chapter: "6"
source_section: "6.1"
---

The proof proceeds by showing that $\tau$ is analytic. Let $(a, [g]_a) \in \mathcal{R}$ and let $D$ be a disk about $a$ on which $g$ is defined (by Lemma 6.20). Let $\Delta = g(D)$ so that $\Delta \subset G$. Let

$$U = \{(\zeta, f(\zeta)): \zeta \in \Delta\}$$

and define $\varphi: U \to \mathbb{C}$ by $\varphi(\zeta, f(\zeta)) = f(\zeta)$; so $(U, \varphi)$ is a coordinate patch on the graph of $f$ (Proposition 6.6). Also $N(g, D) = \{(z, [g]_z): z \in D\}$ gives that $(N(g, D), \rho)$ is a coordinate patch on $\mathcal{R}$ (Theorem 6.7) containing $(a, [g]_a)$, and satisfying $\tau(N(g, D)) \subset U$. Hence to complete the proof it must be shown that $\varphi \circ \tau \circ \rho^{-1}$ is an analytic function on $D$. This is trivial. In fact, if $z \in D$ then

$$\varphi \circ \tau \circ \rho^{-1}(z) = \varphi \circ \tau(z, [g]_z)$$
$$= \varphi(g(z), z)$$
$$= z;$$

that is, $\varphi \circ \tau \circ \rho^{-1}$ is the identity function on $D$, which is certainly analytic. Thus $\tau$ is an analytic isomorphism.
