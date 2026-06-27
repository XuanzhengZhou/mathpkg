---
role: proof
locale: en
of_concept: cousin-i-solvability
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---
**1.** Clearly
$$\gamma(t_0, t_1) + \gamma(t_1, t_2) = (f_{t_0} - f_{t_1}) + (f_{t_1} - f_{t_2}) = f_{t_0} - f_{t_2} = \gamma(t_0, t_2)$$
on $U_{t_0t_1t_2}$. This proves that $\gamma \in Z^1(\mathfrak{U}, \mathfrak{H})$, i.e., $\gamma$ is a $1$-cocycle.

**2.** (a) Let $(U_t, f_t)_{t \in I}$ be solvable. Then there is a meromorphic function $f$ on $X$ such that $(f_t - f)|U_t$ is holomorphic. Let $\rho(t) := (f_t - f)|U_t$. Then $\rho \in C^0(\mathfrak{U}, \mathfrak{H})$ and
$$\delta \rho(t_0, t_1) = \rho(t_1) - \rho(t_0) = (f_{t_1} - f) - (f_{t_0} - f) = f_{t_1} - f_{t_0} = -\gamma(t_0, t_1)$$
on $U_{t_0t_1}$. Hence $\gamma = -\delta \rho \in B^1(\mathfrak{U}, \mathfrak{H})$.

(b) Conversely, if $\gamma = \delta \rho$ for some $\rho \in C^0(\mathfrak{U}, \mathfrak{H})$, then $\rho(t_0) - \rho(t_1) = f_{t_0} - f_{t_1}$ on $U_{t_0t_1}$. Hence $f_{t_0} - \rho(t_0) = f_{t_1} - \rho(t_1)$ on $U_{t_0t_1}$, and these locally defined meromorphic functions patch together to define a global meromorphic function $f$ on $X$ with $f|U_t = f_t - \rho(t)$. Then $f_t - f = \rho(t)$ is holomorphic on $U_t$, so $(U_t, f_t)_{t \in I}$ is solvable.
