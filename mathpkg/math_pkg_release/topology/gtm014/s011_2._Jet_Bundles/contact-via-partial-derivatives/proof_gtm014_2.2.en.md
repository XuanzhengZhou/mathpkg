---
role: proof
locale: en
of_concept: contact-via-partial-derivatives
source_book: gtm014
source_chapter: "2"
source_section: "2. Jet Bundles"
---

We proceed by induction on $k$.

For $k = 1$, $f \sim_1 g$ iff $(df)_p = (dg)_p$, which holds iff the first partial derivatives of $f$ at $p$ are identical with the first partial derivatives of $g$ at $p$. This establishes the base case.

Assume the lemma holds for $k - 1$. Let $y_1, \ldots, y_n$ be the coordinates of $\mathbf{R}^n$ in $U \times \mathbf{R}^n = TU$. Then the differential $(df): U \times \mathbf{R}^n \to \mathbf{R}^m \times \mathbf{R}^m = T\mathbf{R}^m$ is given by

$$(x, y) \mapsto (f(x), \bar{f}_1(x, y), \ldots, \bar{f}_m(x, y))$$

where

$$\bar{f}_i(x, y) = \sum_{j=1}^{n} \frac{\partial f_i}{\partial x_j}(x) \, y_j.$$

Similarly for $(dg)$.

By assumption, $f \sim_k g$ at $p$, which means $(df) \sim_{k-1} (dg)$ at every point $(p, v) \in \{p\} \times \mathbf{R}^n$. By the induction hypothesis, the partial derivatives of $(df)$ at points $(p, v) \in \{p\} \times \mathbf{R}^n$ are equal to the partial derivatives of $(dg)$ at these same points. Let $\alpha$ be an $n$-tuple of non-negative integers with $|\alpha| \leq k - 1$; then

$$\frac{\partial^{|\alpha|} \bar{f}_i}{\partial x^\alpha}(p, v) = \frac{\partial^{|\alpha|} \bar{g}_i}{\partial x^\alpha}(p, v).$$

Evaluate at $v = (0, \ldots, 1, \ldots, 0)$ (the $j$-th standard basis vector). Since $\bar{f}_i(x, y) = \sum_j \frac{\partial f_i}{\partial x_j}(x) y_j$, differentiating with respect to $x^\alpha$ and evaluating at $v = e_j$ yields

$$\frac{\partial}{\partial x^\alpha}\left(\frac{\partial f_i}{\partial x_j}\right)(p) = \frac{\partial}{\partial x^\alpha}\left(\frac{\partial g_i}{\partial x_j}\right)(p).$$

Thus all partial derivatives of order $|\alpha| + 1 \leq k$ agree at $p$, completing the induction step. The converse direction follows similarly: if all partial derivatives up to order $k$ agree at $p$, then the partial derivatives of $\bar{f}_i$ and $\bar{g}_i$ up to order $k-1$ agree, so by induction $(df) \sim_{k-1} (dg)$ everywhere on $T_p X$, hence $f \sim_k g$ at $p$.
