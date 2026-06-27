---
role: proof
locale: en
of_concept: composite-of-hilbert-schmidt-is-nuclear
source_book: gtm003
source_chapter: "IV"
source_section: "10"
---

Denote by $\{x_\alpha : \alpha \in A\}$, $\{y_\beta : \beta \in B\}$ orthonormal bases of $H_1, H_2$, respectively, and by $[\cdot,\cdot]$ the inner product of $H_2$. If for the moment $u$ is any continuous linear map of $H_1$ into $H_2$ with conjugate $u^*$, we obtain, in view of the identity $u(x_\alpha) = \sum_\beta [u(x_\alpha), y_\beta] y_\beta$ ($\alpha \in A$), the equality

$$\sum_\alpha \|u(x_\alpha)\|^2 = \sum_{\alpha,\beta} |[u(x_\alpha), y_\beta]|^2 = \sum_{\alpha,\beta} |[x_\alpha, u^*(y_\beta)]|^2.$$

This establishes the symmetry of the Hilbert-Schmidt condition.

Now suppose $u: H_1 \to H_2$ and $v: H_2 \to H_3$ are both Hilbert-Schmidt. Then $w = v \circ u$ can be represented as an absolutely convergent series

$$w(x) = \sum_\beta [u(x), y_\beta] v(y_\beta) = \sum_{\alpha,\beta} [x, x_\alpha] [u(x_\alpha), y_\beta] v(y_\beta),$$

which is a nuclear representation, showing that $w$ is nuclear.
