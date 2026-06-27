---
role: proof
locale: en
of_concept: codimension-reduction-lemma
source_book: gtm053
source_chapter: "V"
source_section: "4"
---

For $m=2$, the function $t^{(2)}$ is constructed using the diagonal enumeration:
$$t_1^{(2)}(y) = y - \frac{1}{2}\left[\sqrt{2y - \frac{7}{4}} - \frac{1}{2}\right]\left(\left[\sqrt{2y - \frac{7}{4}} - \frac{1}{2}\right] + 1\right),$$
$$t_2^{(2)}(y) = \left[\sqrt{2y - \frac{7}{4}} - \frac{1}{2}\right] - t_1^{(2)}(y) + 2.$$
For $m \geqslant 3$, the construction proceeds by induction using $\tau^{(m)}(x_1, \ldots, x_m) = \tau^{(2)}(\tau^{(m-1)}(x_1, \ldots, x_{m-1}), x_m)$ and solving for the components of $t^{(m)}$.
