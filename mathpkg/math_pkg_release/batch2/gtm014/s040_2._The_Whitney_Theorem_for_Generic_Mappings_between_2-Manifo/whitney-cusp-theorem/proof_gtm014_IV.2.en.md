---
role: proof
locale: en
of_concept: whitney-cusp-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The proof is due to Morin and uses the Malgrange Preparation Theorem.

Choose coordinates $(x_1, x_2)$ centered at $p$ and $(y_1, y_2)$ centered at $q$ such that $f$ has the form
$$f^*y_1 = x_1, \quad f^*y_2 = h(x_1, x_2).$$
Since $f$ has rank 1 at $p$, this is possible. We can also assume that at the origin
$$(df)_0 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$
in this coordinate system; i.e.,
$$\frac{\partial h}{\partial x_1}(0) = \frac{\partial h}{\partial x_2}(0) = 0.$$

We note that $d(\partial h / \partial x_2)_0 \neq 0$, otherwise $f$ would not be one-generic.

*Proof.* Suppose
$$\frac{\partial}{\partial x_1}\left(\frac{\partial h}{\partial x_2}\right) = \frac{\partial}{\partial x_2}\left(\frac{\partial h}{\partial x_2}\right) = 0$$
at $0$. Let $\alpha = \frac{1}{2}(\partial^2 h / \partial x_1^2)(0)$ and compare $f$ with the map
$$(x_1, x_2) \mapsto (x_1, \alpha x_1^2).$$
They have the same 2-jet at $0$, but the latter map is of rank 1 everywhere, so it is not one-generic.

The set $S_1(f)$ is defined by the equation $\partial h / \partial x_2 = 0$; so at each point of $S_1(f)$ the kernel of $(df)$ is spanned by $\partial / \partial x_2$. This means we can take $\partial h / \partial x_2$ to be the function $k$ and $\partial / \partial x_2$ to be the vector field $\xi$ of Definition 2.3.

The condition for the origin to be a cusp is that
$$\frac{\partial^2 h}{\partial x_2^2}(0) = 0;$$
and for it to be a simple cusp,
$$\frac{\partial^3 h}{\partial x_2^3}(0) \neq 0.$$
Therefore, at the origin, we have
$$h = \frac{\partial h}{\partial x_2} = \frac{\partial^2 h}{\partial x_2^2} = 0 \quad \text{and} \quad \frac{\partial^3 h}{\partial x_2^3} \neq 0.$$

The Generalized Malgrange Preparation Theorem allows us to write
$$x_2^3 = 3a_2(x_1, h)x_2^2 + a_1(x_1, h)x_2 + a_0(x_1, h)$$
where $a_0, a_1$, and $a_2$ are smooth functions of $y_1$ and $y_2$ vanishing at $0$. (To see this recall that $f$ is given by $f(x_1, x_2) = (x_1, h(x_1, x_2))$. Then via $f$, $C_0^\infty(\mathbf{R}^2)$ becomes a module over $C_0^\infty(\mathbf{R}^2)$.)
