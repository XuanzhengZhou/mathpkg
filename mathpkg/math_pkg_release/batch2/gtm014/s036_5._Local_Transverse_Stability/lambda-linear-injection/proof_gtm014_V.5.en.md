---
role: proof
locale: en
of_concept: lambda-linear-injection
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

To see that $\lambda$ is well-defined we shall compute a formula for $\lambda(\omega)$ which just depends on the $k$-jet of $\tau$. Choose coordinates $x_1, \ldots, x_n$ based at $p$ in $X$ and coordinates $y_1, \ldots, y_m$ based at $q = f(p)$ in $Y$. Let $f_1, \ldots, f_m$ be the coordinate functions of $f$ in these coordinates. We may write $\tau = \sum_{i=1}^m g_i f^*(\partial/\partial y_i)$ where $g_i$ is a smooth function on $X$ and $F_t = (F_t^1, \ldots, F_t^m)$ where $F_t^i = f_i + t g_i + O(t^2)$. This last equality follows since $(dF_t/dt)|_{t=0} = \tau$.

Thus
$$j^k F_t^i(0) = \sum_{|\alpha| \leq k} \frac{x^\alpha}{\alpha!} \frac{\partial^{|\alpha|} F_t^i}{\partial x^\alpha}(0) = \sum_{|\alpha| \leq k} \frac{x^\alpha}{\alpha!} \left( \frac{\partial^{|\alpha|} f_i}{\partial x^\alpha}(0) + t \frac{\partial^{|\alpha|} g_i}{\partial x^\alpha}(0) + O(t^2) \right).$$

Hence
$$\frac{d}{dt} j^k F_t^i(0)\big|_{t=0} = \sum_{|\alpha| \leq k} \frac{x^\alpha}{\alpha!} \frac{\partial^{|\alpha|} g_i}{\partial x^\alpha}(0).$$

This sum is completely determined by $j^k g(0)$; that is, the $k$-jet of $\tau$ at $p$. Now suppose that $\lambda(\omega) = 0$. Then by the above formula $(\partial^{|\alpha|}/\partial x^\alpha)g_i(0) = 0$ for $|\alpha| \leq k$ and thus $\omega = 0$ in $J^k(f^*TY)_p$; so $\lambda$ is injective. The linearity of $\lambda$ also follows from the formula.
