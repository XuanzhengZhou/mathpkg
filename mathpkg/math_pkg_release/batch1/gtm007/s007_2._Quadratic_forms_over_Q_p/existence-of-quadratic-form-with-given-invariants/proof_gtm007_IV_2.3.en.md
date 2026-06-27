---
role: proof
locale: en
of_concept: existence-of-quadratic-form-with-given-invariants
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.3"
---

**Case $n = 1$.** Trivial: any form $f(X) = d X^2$ has $\varepsilon(f) = 1$ (empty product), so we must have $\varepsilon = 1$.

**Case $n = 2$.** Write $f \sim a X^2 + b Y^2$ with $d = ab$ and $\varepsilon = (a, b)$. If $d = -1$ (i.e., $ab = -1$ in $k^*/k^{*2}$), then $b = -a$ (up to a square), and

$$\varepsilon = (a, b) = (a, -a) = (a, -1)(a, a) = (a, -1)(a, -1) = 1.$$

Thus we cannot have simultaneously $d = -1$ and $\varepsilon = -1$.

Conversely, we construct forms for the allowed combinations:
- If $d = -1$ and $\varepsilon = 1$: take $f = X^2 - Y^2$.
- If $d \neq -1$: there exists $a \in k^*$ such that $(a, -d) = \varepsilon$ (by the lemma on $k^*/k^{*2}$), and take $f = a X^2 + a d Y^2$. Then $d(f) = a^2 d = d$ and $\varepsilon(f) = (a, ad) = (a, -d) = \varepsilon$.

**Case $n = 3$.** Choose $a \in k^*/k^{*2}$ distinct from $-d$. By the rank $2$ case, there exists a binary form $g$ of rank $2$ such that $d(g) = a d$ and $\varepsilon(g) = \varepsilon (a, -d)$. Then set $f = a Z^2 + g$. We have

$$d(f) = a \cdot d(g) = a \cdot a d = d,$$
$$\varepsilon(f) = \prod_{i<j} (\text{coeffs}) = \varepsilon(g) \cdot (a, ad) = \varepsilon(a, -d) \cdot (a, -d) = \varepsilon.$$

So $f$ has the required invariants.

**Case $n \geq 4$.** Reduce to $n = 3$ by taking $f = g(X_1, X_2, X_3) + X_4^2 + \cdots + X_n^2$ where $g$ is a ternary form with the required invariants. Adding squares $X_i^2$ does not change $d$ or $\varepsilon$.
