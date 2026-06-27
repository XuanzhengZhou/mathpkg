---
role: proof
locale: en
of_concept: ideal-of-graph-coordinates
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

The functions $b_i(x) - y_i$ clearly vanish on $\operatorname{graph} b$ in $\mathbf{R}^k \times \mathbf{R}^l$. Also $i^*_{\mathbf{R}^k \times \{0\}}(b_i(x) - y_i) = b_i(x)$, so
$$
\mathcal{I}_{(0,0)}(\mathbf{R}^k \times \{0\}, \operatorname{graph} b) \supset (b_1, \ldots, b_l).
$$

Conversely, suppose that $f: \mathbf{R}^k \times \mathbf{R}^l \to \mathbf{R}$ vanishes on $\operatorname{graph} b$. Then we may write
$$
f(x, y) = (b_1(x) - y_1)f_1(x, y) + \cdots + (b_l(x) - y_l)f_l(x, y)
$$
where each $f_i$ is a smooth function. To see this, let
$$
g(t) = f(x, (1 - t)y + t b(x))
$$
for $t \in \mathbf{R}$. Then
$$
f(x, y) = g(0) - g(1) = -\int_0^1 \frac{dg}{dt}(t) \, dt.
$$

Expanding $\frac{dg}{dt}$ by the chain rule:
$$
\frac{dg}{dt}(t) = \sum_{i=1}^l \frac{\partial f}{\partial y_i}(x, (1-t)y + t b(x)) \cdot (b_i(x) - y_i).
$$

Therefore
$$
f(x, y) = \sum_{i=1}^l (b_i(x) - y_i) \int_0^1 \frac{\partial f}{\partial y_i}(x, (1-t)y + t b(x)) \, dt,
$$
which expresses $f$ as a linear combination of $b_i(x) - y_i$ with smooth coefficients. Applying $i^*_{\mathbf{R}^k \times \{0\}}$ to this expression gives
$$
(i^*_{\mathbf{R}^k \times \{0\}} f)(x) = \sum_{i=1}^l b_i(x) \cdot f_i(x, 0),
$$
showing that $i^*_{\mathbf{R}^k \times \{0\}} f$ belongs to the ideal $(b_1, \ldots, b_l)$. Hence the reverse inclusion holds, proving the lemma.
