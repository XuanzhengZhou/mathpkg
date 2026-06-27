---
role: proof
locale: en
of_concept: sards-theorem-lemma-b
source_book: gtm014
source_chapter: "1"
source_section: "1"
---

Let $p \in C - C_1$. Then there exists some first-order partial derivative of some component of $f$ that does not vanish at $p$. Without loss of generality, assume $\frac{\partial f_1}{\partial x_1}(p) \neq 0$. Define a map $h: U \to \mathbf{R}^n$ by
$$h(x_1, \ldots, x_n) = (f_1(x), x_2, \ldots, x_n).$$
The Jacobian of $h$ at $p$ has nonzero determinant (since $\frac{\partial f_1}{\partial x_1}(p) \neq 0$), so by the Inverse Function Theorem, $h$ restricts to a diffeomorphism on some open neighborhood $U'_p \subset U$ of $p$.

Let $V = h(U'_p)$. Then the composition $g = f \circ h^{-1}: V \to \mathbf{R}^m$ has the form
$$g(y_1, \ldots, y_n) = (y_1, g_2(y), \ldots, g_m(y)).$$
In this coordinate system, the critical points of $g$ are controlled by the map $\tilde{g}(y_2, \ldots, y_n) = (g_2(0, y_2, \ldots, y_n), \ldots, g_m(0, y_2, \ldots, y_n))$ restricted to $\{0\} \times \mathbf{R}^{n-1}$.

By construction, $h(C \cap U'_p) \subset C[g]$, and by the induction hypothesis on the dimension $n-1$, the set of critical values of $\tilde{g}$ has measure zero. Consequently, $f(C \cap U'_p)$ has measure zero. Since $C - C_1$ can be covered by countably many such neighborhoods $U'_p$, it follows that $f(C - C_1)$ has measure zero.
