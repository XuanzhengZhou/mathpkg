---
role: proof
locale: en
of_concept: cauchy-riemann-equations
source_book: gtm055
source_chapter: "5"
source_section: "6"
---

If $f$ is analytic at $\lambda_0 = x_0 + i y_0$, then the derivative $f'(\lambda_0)$ exists. Computing the limit of the difference quotient along the real and imaginary directions separately yields:
$$f'(\lambda_0) = u_x(x_0, y_0) + i v_x(x_0, y_0)$$
(approaching along the real axis), and
$$f'(\lambda_0) = v_y(x_0, y_0) - i u_y(x_0, y_0)$$
(approaching along the imaginary axis, using $1/i = -i$). Equating real and imaginary parts gives the Cauchy-Riemann equations.

Conversely, suppose $u, v \in \mathcal{C}^{(1)}(\Delta')$ and satisfy $u_x = v_y$, $u_y = -v_x$ at $(x_0, y_0)$. By the theorem on the total differential, there exist functions $\varepsilon', \varepsilon'', \eta', \eta''$ tending to zero as $(x, y) \to (x_0, y_0)$ such that
$$u(x,y) - u(x_0,y_0) = [u_x + \varepsilon'](x-x_0) + [u_y + \varepsilon''](y-y_0)$$
$$v(x,y) - v(x_0,y_0) = [v_x + \eta'](x-x_0) + [v_y + \eta''](y-y_0)$$
where partials are evaluated at $(x_0, y_0)$. Substituting the Cauchy-Riemann equations and computing $f(\lambda)-f(\lambda_0) = u+iv - (u_0+iv_0)$ yields
$$f(\lambda)-f(\lambda_0) = u_x(\lambda-\lambda_0) + i v_x(\lambda-\lambda_0) + [\varepsilon' + i\eta'](x-x_0) + [\varepsilon'' + i\eta''](y-y_0).$$
Dividing by $\lambda-\lambda_0$ and taking the limit shows $f'(\lambda_0) = u_x + i v_x$.
