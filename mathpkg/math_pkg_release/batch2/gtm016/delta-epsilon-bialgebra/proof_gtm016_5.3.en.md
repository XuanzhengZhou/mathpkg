---
role: proof
locale: en
of_concept: delta-epsilon-bialgebra
source_book: gtm016
source_chapter: "5"
source_section: "5.3"
---

The $K$-linearity of $\Delta$ and $\varepsilon$ follows from the definitions: $\Delta(x)$ is defined via the coclosed property $x(ab) = \sum_i x(a)x_i(b)$ for $a,b \in K$, and $\varepsilon(x) = x(1)$.

(1) Coassociativity follows from the two expansions of $x(abc)$ in Proposition 5.3.7, corresponding to $(\Delta \otimes \id) \circ \Delta$ and $(\id \otimes \Delta) \circ \Delta$.

(2) The coidentity property follows from $x(a) = x(1a) = \sum_i x(1)x_i(a) = \sum_i \varepsilon(x_{(1)i})x_{(2)i}(a)$ and similarly $x(a) = x(a1)$.

(3) $\Delta(I) = I \otimes I$ since $I(ab) = ab = I(a)I(b)$. For multiplicativity: if $x(ab) = \sum_i x(a)x_i(b)$ and $y(ab) = \sum_j y(a)y_j(b)$, then $(xy)(ab) = \sum_{i,j} x(y(a)) x_i(y_j(b))$, giving $\Delta(xy) = \sum_{i,j} x_j y \otimes x_i y_j$.

(4) $\varepsilon(I) = I(1) = 1_K$, and $\varepsilon(xy) = (xy)(1) = x(y(1)) = x(\varepsilon(y) \cdot 1) = \varepsilon(x)\varepsilon(y)$ by $K$-linearity.
