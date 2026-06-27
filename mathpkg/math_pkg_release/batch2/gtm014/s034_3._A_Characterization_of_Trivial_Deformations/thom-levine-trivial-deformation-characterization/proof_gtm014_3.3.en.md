---
role: proof
locale: en
of_concept: thom-levine-trivial-deformation-characterization
source_book: gtm014
source_chapter: "III"
source_section: "3. A Characterization of Trivial Deformations"
---

**Necessity.** If $F$ is trivial, then $\tau_F^i = 0$ for all $i$. We show this implies $F(x,v) = f(x)$ globally. Fix $(x_0, v_0) \in X \times V$ and choose coordinates $x_1, \ldots, x_n$ near $x_0$ in $X$ and $y_1, \ldots, y_m$ near $F_{v_0}(x_0, v_0)$ in $Y$. In these coordinates we may write $F(x, v) = (F_1(x, v), \ldots, F_m(x, v), v)$. Then

$$\left(dF\right)_{(x, v)} \left( \frac{\partial}{\partial t_i} \bigg|_{(x, v)} \right) = \left( \frac{\partial F_1}{\partial t_i} (x, v), \ldots, \frac{\partial F_m}{\partial t_i} (x, v) \right) + \frac{\partial}{\partial t_i} \bigg|_{F(x, v)}.$$

Thus $\tau_F^i \equiv 0$ implies that $\partial F_j / \partial t_i (x, v) \equiv 0$ for $1 \leq j \leq m$. Thus $F_j(x, v)$ is independent of $t_i$ for all $i$ and $F_j(x, v) = F_j(x) = f_j(x)$ where $f = (f_1, \ldots, f_m)$ in these coordinates. Since $(x_0, v_0)$ is arbitrary we find that globally $F(x, v) = f(x)$, so $F$ is trivial.

Alternatively, for the constructive direction: given a trivial $F$, define $\eta_q^i = \pi(dH)_{H^{-1}(q)}((\partial/\partial t_i)|_{H^{-1}(q)})$ where $q \in Y \times U$ and $H$ conjugates $F$ to $f \times \text{id}_U$. Clearly $\eta^i$ is a vector field on $Y \times U$ with vanishing $\mathbf{R}^k$-component. Substituting $\eta$ into the defining equation yields $\tau_F^i(p) = (dF)_p(\zeta_p^i) + \eta_{H(p)}^i$. Since $H(r) = H \cdot (f \times \text{id}_U) \cdot G^{-1}(p) = F(p)$, we obtain $\tau_F^i = (dF)(\zeta^i) + F^*(\eta^i)$.

**Sufficiency.** Let $F: X \times V \rightarrow Y \times V$ be a $k$-deformation of $f$ and let $\zeta^i$ and $\eta^i$ be vector fields on $X \times V$ and $Y \times V$ respectively, such that the $\mathbf{R}^k$-components of $\zeta^i$ and $\eta^i$ are zero and $\tau_F^i = (dF)(\zeta^i) + F^*(\eta^i)$ on $X \times V$. We must show that $F$ is trivial. Since $X$ is compact, $\zeta^i$ is trivially compactly supported. By shrinking $V$ we may assume that $\overline{V}$ is compact and that $\tau_F^i = (dF)(\zeta^i) + F^*(\eta^i)$ on $X \times \overline{V}$. We can then damp $\eta^i$ to zero off a compact neighborhood of $F(X \times \overline{V})$ and assume that $\eta^i$ is compactly supported.

Apply Lemmas 3.4 and 3.5 to show the existence of diffeomorphisms $G: X \times V \rightarrow X \times V$ and $H: Y \times V \rightarrow Y \times V$ so that

$$-\zeta^k = \pi(dG)(G^{-1})^*\left( \frac{\partial}{\partial t_k} \right)$$

and

$$\eta^k = \pi(dH)(H^{-1})^*\left( \frac{\partial}{\partial t_k} \right).$$

Iterating this procedure for $i = k, k-1, \ldots, 1$ yields diffeomorphisms $G$ and $H$ that conjugate $F$ to a deformation with $\tau_F^i = 0$ for all $i$. The necessity argument then shows $F$ is trivial.
