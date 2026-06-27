---
role: proof
locale: en
of_concept: frenet-equations-invariance
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

(i) An isometry $B$ of $\mathbb{R}^n$ can be written as $B(x) = R x + b$, where $R \in O(n)$ is the orthogonal part and $b \in \mathbb{R}^n$. For $\tilde{c} = B \circ c$, we have $\tilde{c}^{(k)}(t) = R c^{(k)}(t)$. Thus the linear spans are preserved: $\tilde{c}^{(k)}$ is a linear combination of $\tilde{e}_1, \ldots, \tilde{e}_k$ if and only if $c^{(k)}$ is a linear combination of $e_1, \ldots, e_k$. By the uniqueness of the distinguished Frenet frame (up to orientation), choosing $\tilde{e}_i = R e_i$ preserves all the conditions.

Then $\dot{\tilde{e}}_i = R \dot{e}_i = R \sum_j \omega_{ij} e_j = \sum_j \omega_{ij} R e_j = \sum_j \omega_{ij} \tilde{e}_j$, so $\tilde{\omega}_{ij} = \omega_{ij}$.

(ii) Let $\tilde{c}(s) = c(\phi(s))$. By the chain rule, $\tilde{c}'(s) = \dot{c}(\phi(s)) \phi'(s)$, $\tilde{c}''(s) = \ddot{c}(\phi(s)) (\phi'(s))^2 + \dot{c}(\phi(s)) \phi''(s)$, etc. By induction, $\tilde{c}^{(k)}(s)$ is a linear combination of $c^{(1)}(\phi(s)), \ldots, c^{(k)}(\phi(s))$. Therefore the distinguished Frenet frame satisfies $\tilde{e}_i(s) = e_i(\phi(s))$ (possibly with sign adjustments for orientation). Differentiating with respect to $s$ and using the chain rule:
$$\frac{d}{ds}\tilde{e}_i(s) = \dot{e}_i(\phi(s)) \phi'(s) = \sum_j \omega_{ij}(\phi(s)) \phi'(s) e_j(\phi(s)) = \sum_j \omega_{ij}(\phi(s)) \phi'(s) \tilde{e}_j(s).$$
Hence $\tilde{\kappa}_i(s) = \tilde{\omega}_{i,i+1}(s) = \omega_{i,i+1}(\phi(s)) \phi'(s)$. However, if we use arc length parametrization for both $c$ and $\tilde{c}$, then $\phi'(s) = 1$ and the curvatures coincide exactly: $\tilde{\kappa}_i(s) = \kappa_i(\phi(s))$.
