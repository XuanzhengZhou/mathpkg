---
role: proof
locale: en
of_concept: homological-determination-of-orientation
source_book: gtm020
source_chapter: "3"
source_section: "3.4"
---

By translations, we can assume that $f(0) = 0 = x$. Write $f(x) = Lx + g(x)$, where $Lx$ is linear and $D(g)(0) = 0$, $g(0) = 0$. As maps defined on pairs $(U, U - 0) \to (\mathbf{R}^n, \mathbf{R}^n - 0)$, there is a homotopy
$$h_t(x) = Lx + (1 - t)g(x),$$
where $h_0(x) = f(x)$ and $h_1(x) = Lx$. This reduces the problem to the case where $f: U \to V$ is a linear isomorphism.

By a second homotopy we can deform $f$ into an orthogonal transformation. Then $f$ can be expressed as a composition $f = r_1 \circ \cdots \circ r_q$, where each $r_i$ is a reflection through an $(n-1)$-dimensional subspace of $\mathbf{R}^n$. For each reflection $r_i$, we have
$$(r_i)_*(\alpha_0) = -\alpha_0, \quad (r_i)^*(\beta_0) = -\beta_0, \quad O(r_i) = -1.$$

By the rule for composition of induced maps in homology and cohomology, we obtain
$$f_*(\alpha_0) = (r_1)_* \cdots (r_q)_*(\alpha_0) = (-1)^q \alpha_0 = O(f)\,\alpha_0$$
and similarly
$$f^*(\beta_0) = O(f)\,\beta_0.$$
This proves the theorem.
