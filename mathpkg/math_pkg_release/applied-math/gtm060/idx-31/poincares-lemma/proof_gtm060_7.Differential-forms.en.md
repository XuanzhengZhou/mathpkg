---
role: proof
locale: en
of_concept: poincares-lemma
source_book: gtm060
source_chapter: "7"
source_section: "Differential forms"
---
Let $\omega^k$ be a closed $k$-form on $\mathbb{R}^n$, so $d\omega^k = 0$. Define the co-cone operator $p$ on a $k$-form by
$$(p\omega)_{\mathbf{x}}(\xi_1, \ldots, \xi_{k-1}) = \int_0^1 \omega_{t\mathbf{x}}(\mathbf{x}, t\xi_1, \ldots, t\xi_{k-1})\, dt.$$
This operator satisfies the homotopy identity $d \circ p + p \circ d = \text{id}$. Since $\omega^k$ is closed, $d\omega^k = 0$, we obtain
$$d(p\omega^k) = \omega^k - p(d\omega^k) = \omega^k.$$
Thus $\omega^k$ is the exterior derivative of the $(k-1)$-form $p\omega^k$.
