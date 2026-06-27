---
role: proof
locale: en
of_concept: smooth-extension-lemma
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

It suffices to prove the lemma for $h \equiv 0$, by replacing $g$ with $g - h$; then $F = F_1 + h$ gives the required extension.

Choose coordinates $y_1, \ldots, y_n$ on $\mathbf{R}^n$ so that $V$ is defined by $y_1 = \cdots = y_j = 0$ and $W$ is defined by $y_{j+1} = \cdots = y_k = 0$. This is possible since $V + W = \mathbf{R}^n$. Set
$$F(y) = \sum_{\alpha = (a_1, \ldots, a_j, 0, \ldots, 0)} \frac{y^\alpha}{\alpha!} \frac{\partial^{|\alpha|} g}{\partial y^\alpha}(0, \ldots, 0, y_{j+1}, \ldots, y_n) \; \rho\!\left( \mu_{|\alpha|} \sum_{i=1}^{j} y_i^2 \right)$$
where $\rho$ is the smooth bump function ($\rho(t) = 1$ for $|t| \leq 1/2$, $\rho(t) = 0$ for $|t| \geq 1$) and $\{\mu_l\}_{l=0}^{\infty}$ is a sequence increasing to infinity.

As in the Borel Theorem, the $\mu_l$'s can be chosen to increase sufficiently rapidly to ensure $F$ is smooth on a neighborhood of $0$ in $\mathbf{R}^n$.

To verify the properties: For points in $V$ (where $y_1 = \cdots = y_j = 0$), all terms with $|\alpha| > 0$ vanish, leaving only the $\alpha = (0, \ldots, 0)$ term which gives $g(0, \ldots, 0, y_{j+1}, \ldots, y_n)$. The equality of all derivatives follows from the construction: on $V$, the Taylor expansion in the $y_1, \ldots, y_j$ directions matches $g$ to infinite order. On $W$ (where $y_{j+1} = \cdots = y_k = 0$), since $h \equiv 0$, we need all derivatives of $F$ to vanish. This holds because $g$ and $h = 0$ agree to infinite order on $V \cap W$ (where $y_1 = \cdots = y_k = 0$), so all derivatives $\partial^{|\alpha|} g / \partial y^\alpha$ vanish there.
