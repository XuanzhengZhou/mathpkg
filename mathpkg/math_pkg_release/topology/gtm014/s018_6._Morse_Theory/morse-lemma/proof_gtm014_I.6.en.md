---
role: proof
locale: en
of_concept: morse-lemma
source_book: gtm014
source_chapter: "I"
source_section: "§6. Morse Theory"
---

Let $U$ be a coordinate nbhd of $p$ and $\psi: U \to \mathbf{R}^n$ a chart. Then $(d^2(f \circ \psi^{-1}))$ is a symmetric, nondegenerate, bilinear form on $T_0 \mathbf{R}^n$. Choose a matrix $A$ which diagonalizes this form, i.e.

$$d^2(f \circ \psi^{-1} \circ A) = \begin{pmatrix} -I_k & 0 \\ 0 & I_{n-k} \end{pmatrix}$$

where $I_s$ is the $s \times s$ identity matrix. Let $\eta = A^{-1} \circ \psi$. Then $\eta$ is also a chart on $U$. Define $g(x) = f(\eta^{-1}(x))$ on a convex nbhd of $0$.

By construction, $g$ has a nondegenerate critical point at $0$ with Hessian $\pm \delta_{ij}$ in diagonal form. Apply Lemma 6.12 to $g$: there exists a nbhd $V$ of $0$ and smooth functions $h_i: V \to \mathbf{R}$ such that $h_i(0)=0$, $\frac{\partial h_i}{\partial x_j}(0) = \pm \delta_{ij}$, and

$$g(x) = g(0) + (\pm h_1^2(x) \pm \cdots \pm h_n^2(x)).$$

Since the Hessian has $k$ negative and $n-k$ positive eigenvalues, the signs arrange as $-h_1^2 - \cdots - h_k^2 + h_{k+1}^2 + \cdots + h_n^2$.

Finally, set $\alpha_i = h_i \circ \eta$ for $i=1,\ldots,n$. Then $\alpha = (\alpha_1, \ldots, \alpha_n): U \to \mathbf{R}^n$ is a chart centered at $p$ because $\frac{\partial \alpha_i}{\partial x_j}(p) = \pm \delta_{ij}$ implies the Jacobian is invertible. Pulling back gives

$$f(x) = f(p) - \alpha_1^2(x) - \cdots - \alpha_k^2(x) + \alpha_{k+1}^2(x) + \cdots + \alpha_n^2(x)$$

for all $x$ in a nbhd of $p$.
