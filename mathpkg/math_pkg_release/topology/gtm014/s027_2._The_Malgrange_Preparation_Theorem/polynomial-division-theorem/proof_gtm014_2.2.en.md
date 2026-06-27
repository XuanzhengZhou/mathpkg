---
role: proof
locale: en
of_concept: polynomial-division-theorem
source_book: gtm014
source_chapter: "2"
source_section: "2. The Malgrange Preparation Theorem"
---

The proof uses the same idea as the proof of Theorem 1.4 (the complex-analytic version), but replaces the Cauchy Integral Formula with its smooth analogue provided by Green's Theorem.

**Step 1: A generalized Cauchy formula.** Let $z = x + iy$ be a complex coordinate on $\mathbb{C}$. Let $D$ be a bounded domain in $\mathbb{C}$ with smooth boundary $\gamma$, and let $F$ be a smooth complex-valued function on a neighborhood of $\overline{D}$. Then for any $w \in D$,

$$F(w) = \frac{1}{2\pi i} \int_{\gamma} \frac{F(z)}{z - w} dz + \frac{1}{2\pi i} \iint_D \frac{(\partial F / \partial \bar{z})(z)}{z - w} dz \wedge d\bar{z}.$$

*Proof of the formula.* For $w \in D$, choose $\varepsilon$ less than the distance from $w$ to $\gamma$. Let $D_{\varepsilon} = D \setminus (\text{disk of radius } \varepsilon \text{ about } w)$ and $\gamma_{\varepsilon} = \partial D_{\varepsilon}$. Green's Theorem in $\mathbb{R}^2$ states that for smooth $M, N: D_{\varepsilon} \to \mathbb{R}$ continuous on $\gamma_{\varepsilon}$,

$$\int_{\gamma_{\varepsilon}} M dx + N dy = \iint_{D_{\varepsilon}} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dx \wedge dy.$$

This holds for complex-valued $M, N$ by treating real and imaginary parts separately. With $F = f + i g$ and $dz = dx + i dy$,

$$\int_{\gamma_{\varepsilon}} F dz = \int_{\gamma_{\varepsilon}} (f + ig)(dx + i dy) = 2i \iint_{D_{\varepsilon}} \frac{\partial F}{\partial \bar{z}} dx \wedge dy = -\iint_{D_{\varepsilon}} \frac{\partial F}{\partial \bar{z}} dz \wedge d\bar{z}.$$

Applying this to $F(z)/(z - w)$ and noting that $1/(z - w)$ is holomorphic on $D_{\varepsilon}$ (so $\frac{\partial}{\partial \bar{z}}(F(z)/(z-w)) = (\partial F/\partial \bar{z})(z)/(z-w)$), we obtain the formula after letting $\varepsilon \to 0$.

*Note:* If $F$ is holomorphic in $D$, then $\partial F/\partial \bar{z} = 0$ and the formula reduces to the standard Cauchy Integral Formula.

**Step 2: Constructing $q$ and $r$.** Let $\tilde{G}(t, x, \lambda)$ be a smooth extension of $G(t, x)$ to complex $t$ (i.e., $\tilde{G}(t, x, \lambda) = G(t, x)$ for all real $t$), with the property that $\partial \tilde{G}/\partial \bar{z}$ vanishes on the zeroes of $P_k$ and for real $z$. Choose a closed curve $\gamma$ in $\mathbb{C}$ enclosing the zeroes of $P_k(\cdot, \lambda)$ and a domain $D$ bounded by $\gamma$. Define

$$q(w, x, \lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{\tilde{G}(\eta, x, \lambda)}{P_k(\eta, \lambda)} \frac{d\eta}{(\eta - w)} + \frac{1}{2\pi i} \iint_D \frac{(\partial \tilde{G}/\partial \bar{z})(\eta, x, \lambda)}{P_k(\eta, \lambda)} \frac{d\eta \wedge d\bar{\eta}}{(\eta - w)},$$

$$r_i(x, \lambda) = \frac{1}{2\pi i} \int_{\gamma} \frac{\tilde{G}(\eta, x, \lambda)}{P_k(\eta, \lambda)} s_i(\eta, \lambda) d\eta + \frac{1}{2\pi i} \iint_D \frac{(\partial \tilde{G}/\partial \bar{z})(\eta, x, \lambda)}{P_k(\eta, \lambda)} s_i(\eta, \lambda) d\eta \wedge d\bar{\eta},$$

where $s_i(\eta, \lambda)$ are polynomials such that $(P_k(\eta, \lambda) - P_k(w, \lambda))/(\eta - w) = \sum_{i=0}^{k-1} s_i(\eta, \lambda) w^i$.

The first integrals (the boundary integrals) are well-defined and smooth for the same reasons as in the complex-analytic case (Theorem 1.4), since $\gamma$ avoids the zeroes of $P_k$. The second integrals (the area integrals) are well-defined because $\partial \tilde{G}/\partial \bar{z}$ vanishes at the zeroes of $P_k$ by construction, making the integrands bounded. The smoothness of $q$ and $r_i$ in all variables follows from the smoothness of $\tilde{G}$ and differentiation under the integral sign, once it is established that the area integrals converge uniformly with all derivatives.

**Step 3: Constructing the smooth extension $\tilde{G}$.** The existence of the required smooth extension $\tilde{G}$ is established using two lemmas about smooth functions:

(a) *Series construction lemma.* Given a sequence of smooth functions $f_l(x)$ with suitable growth control on their derivatives, one can construct a smooth function $F(t, x) = \sum_{l=0}^{\infty} f_l(x) \frac{t^l}{l!} \rho(\mu_l t)$ where $\rho$ is a smooth bump function (identically $1$ near $0$, zero outside $[-1,1]$) and $\mu_l \to \infty$ sufficiently rapidly. The $\mu_l$ can be chosen to increase fast enough to guarantee that all termwise-differentiated series converge uniformly, making $F$ smooth.

(b) *Smooth extension from complementary subspaces.* Let $V$ and $W$ be linear subspaces of $\mathbb{R}^n$ such that $V + W = \mathbb{R}^n$. Let $g$ be smooth on a neighborhood of $0$ in $V$ and $h$ smooth on a neighborhood of $0$ in $W$. If $g$ and $h$ agree (with all derivatives) on $V \cap W$, then there exists a smooth function $F$ defined on a neighborhood of $0$ in $\mathbb{R}^n$ such that for all multi-indices $\alpha$,

$$\frac{\partial^{|\alpha|}F}{\partial x^\alpha}(x) = \begin{cases}
\frac{\partial^{|\alpha|}g}{\partial x^\alpha}(x) & \text{if } x \in V,\\
\frac{\partial^{|\alpha|}h}{\partial x^\alpha}(x) & \text{if } x \in W.
\end{cases}$$

*Proof of (b).* It suffices to prove the case $h \equiv 0$ (since $F = F_1 + h$ where $F_1$ extends $g - h$ and $0$). Choose coordinates $y_1, \ldots, y_n$ so that $V = \{y_1 = \cdots = y_j = 0\}$ and $W = \{y_{j+1} = \cdots = y_k = 0\}$ (possible since $V + W = \mathbb{R}^n$). Then set

$$F(y) = \sum_{\alpha = (a_1, \ldots, a_j, 0, \ldots, 0)} \frac{y^\alpha}{\alpha!} \frac{\partial^{|\alpha|} g}{\partial y^\alpha}(0, \ldots, 0, y_{j+1}, \ldots, y_n) \; \rho\!\left( \mu_{|\alpha|} \sum_{i=1}^{j} y_i^2 \right)$$

where $\rho$ is the same smooth bump function as in (a) and $\mu_l \to \infty$ rapidly. As in (a), the $\mu_l$ can be chosen to increase fast enough to guarantee smoothness. Direct verification shows $F$ has the required derivatives on $V$ (all $y_1 = \cdots = y_j = 0$, hence $\rho(\cdots) = \rho(0) = 1$, and the series collapses to the Taylor expansion of $g$ along $W$).

These lemmas together guarantee the existence of the smooth extension $\tilde{G}$ with $\partial \tilde{G}/\partial \bar{z}$ vanishing on the zeroes of $P_k$, completing the proof. $\square$
