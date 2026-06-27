---
role: proof
locale: en
of_concept: holomorphic-3-4-
source_book: gtm038
source_chapter: "I"
source_section: "3. The Cauchy Integral"
---

**Theorem 3.4 (Cauchy estimates).** Let $f(z) = \sum_{v=0}^{\infty} a_v z^v$ be a power series converging on the polycylinder $P_r(0)$. Then for every $0 < \rho < r$ (componentwise),

$$|a_v| \leq \frac{\|f\|_{T_{\rho}}}{\rho^v}$$

where $\|f\|_{T_{\rho}} = \sup_{z \in T_{\rho}} |f(z)|$ and $\rho^v = \rho_1^{v_1} \cdots \rho_n^{v_n}$.

**Proof.** By the Cauchy integral formula (Theorem 3.1), for $z \in P_{\rho}(0)$,

$$f(z) = \left(\frac{1}{2\pi i}\right)^n \int_{T_{\rho}} \frac{f(\xi)}{(\xi_1 - z_1) \cdots (\xi_n - z_n)} d\xi_1 \cdots d\xi_n.$$

Differentiating under the integral sign with respect to $z$ (which is justified by uniform convergence) gives

$$a_v = \frac{1}{v!} \frac{\partial^{|v|} f}{\partial z^v}(0) = \left(\frac{1}{2\pi i}\right)^n \int_{T_{\rho}} \frac{f(\xi)}{\xi_1^{v_1+1} \cdots \xi_n^{v_n+1}} d\xi_1 \cdots d\xi_n.$$

Since $|\xi_j| = \rho_j$ on $T_{\rho}$, the estimate follows immediately:

$$|a_v| \leq \left(\frac{1}{2\pi}\right)^n \cdot \frac{\|f\|_{T_{\rho}}}{\rho_1^{v_1+1} \cdots \rho_n^{v_n+1}} \cdot (2\pi\rho_1) \cdots (2\pi\rho_n) = \frac{\|f\|_{T_{\rho}}}{\rho^v}.$$
