---
role: proof
locale: en
of_concept: graph-of-analytic-function-is-analytic-manifold
source_book: gtm011
source_chapter: "6"
source_section: "6.1"
---

Since $\Gamma$ is homeomorphic to $G$ it must be connected. Fix $\alpha = (a, f(a))$ in $\Gamma$; it is left to the reader to show that $\varphi_\alpha$ is a homeomorphism of $U_\alpha$ onto $f(D_a)$. Suppose that $\beta = (b, f(b)) \in \Gamma$ with $U_\alpha \cap U_\beta \neq \emptyset$ and compute $\varphi_\alpha \circ \varphi_\beta^{-1}$. Since $f: D_b \to \mathbb{C}$ is one-one there is an analytic function $g: \Omega \to D_b$, where $\Omega = f(D_b)$, such that $f(g(\omega)) = \omega$ for all $\omega$ in $\Omega$. Since $\varphi_\beta(U_\beta) = \Omega$, we have $\varphi_\alpha \circ \varphi_\beta^{-1}(\omega) = f(g(\omega)) = \omega$, which is analytic. Thus $(\Gamma, \Phi)$ is an analytic manifold.
