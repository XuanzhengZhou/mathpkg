---
role: proof
locale: en
of_concept: stone-weierstrass-order-form
source_book: gtm003
source_chapter: "V: Order Structures"
source_section: "8. Stone-Weierstrass and Representation Theorems"
---

Let $h \in \mathcal{C}_{\mathbb{R}}(X)$ and $\varepsilon > 0$ be given. For each $s \in X$, we construct a function $g_s \in F$ such that $g_s(s) = h(s)$ and $g_s(t) > h(t) - \varepsilon$ for all $t \in X$.

Since $F$ contains $e$ and separates points of $X$, for any two distinct points $r, s \in X$ there exists $f_{r,s} \in F$ with $f_{r,s}(r) \neq f_{r,s}(s)$. By adding suitable multiples of $e$ and scaling, we obtain functions that take prescribed values at two points.

Consider the set $V_s = \{r \in X : g_s(r) < h(r) + \varepsilon\}$, which is open and contains $s$. Hence $X = \bigcup_{s \in X} V_s$, and the compactness of $X$ implies the existence of a finite set $\{s_1, \ldots, s_m\}$ such that
$$
X = \bigcup_{\mu=1}^{m} V_{s_\mu}.
$$

Let $g = \inf\{g_{s_1}, \ldots, g_{s_m}\}$. Since $F$ is a vector sublattice, $g \in F$. For all $r \in X$ we have
$$
h(r) - \varepsilon < g(r) < h(r) + \varepsilon,
$$
hence $\|h - g\| < \varepsilon$. Since $h$ and $\varepsilon$ were arbitrary, $F$ is dense in $\mathcal{C}_{\mathbb{R}}(X)$.
