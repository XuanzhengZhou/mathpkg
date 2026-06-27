---
locale: en
of_concept: the-curvature-form-k-t-for-the-affine-homotopy-nabla-t-1-tna
role: proof
source_book: gtm020
source_chapter: 19. Characteristic Classes and Connections
source_section: '3'
---

Now calculate using $(1-t) - (1-t)^2 = t-t^2 = t(1-t)$ from the definition

$$K_t = d\theta_t - \theta_t \wedge \theta_t$$

$$= (1-t)d\theta_0 + t d\theta_1 + dt(-\theta_0 + \theta_1) - (1-t)^2\theta_0 \wedge \theta_0 - t^2\theta_1 \wedge \theta_1$$

$$- t(1-t)\{\theta_0 \wedge \theta_1 + \theta_1 \wedge \theta_0\}$$

$$= (1-t)K_0 + tK_1 + t(1-t)\{\theta_0 \wedge \theta_0 - \theta_0 \wedge \theta_1 - \theta_1 \wedge \theta_0 + \theta_1 \wedge \theta_1\}$$

$$+ (\theta_0 - \theta_1)dt$$

$$= (1-t)K_0 + tK_1 + t(1-t)(\theta_0 - \theta_1)^2 + (\theta_0 - \theta_1)dt.$$

This proves the proposition.

Now we wish to apply the homotopy formula $dQ + Qd = j_1 - j_0$ of (1.7) to a form coming from an invariant polynomial $\phi \in \text{Inv}(n)$ with $K$ on $M \times [0,1]$ substituted into $\phi$. By (3.7) the form $\phi(K)$ is a closed form on $M \times [0,1]$.

4

4.7 Remark. We can denote $c_q(E)_{DR} = [c_q(E, \nabla)] \in H^{2q}_{DR}(M, \underline{C})$ where $\nabla$ is any connection on the smooth vector bundle $E$. There is another Chern class $c_q(E) \in H^{2q}(M, \underline{Z})$ defined axiomatically in 16(3.2). There is a coefficient morphism $H^{2q}(M, \underline{Z}) \rightarrow H^{2q}_{DR}(M, \underline{C})$ in cohomology, and under this coefficient morphism $c_q(E)$ is mapped to $c_q(E)_{DR}$.

4.8 Reference. There are further considerations in the theory of connections. For example, there is the notion of universal connections. For this and related topics, see M. S. Narasimhan and S. Ramanan, Existence of universal connections I and II, American Journal of Mathematics, 83, 1961, pp. 563–572 and 85, 1963, pp. 223–231.

5. Homotopy to the Trivial Connection and the Chern-Simons Form

5.1 Remark. The curvature form $K_t$ of (4.2) for $\nabla_t = (1 - t)\nabla_0 + t\nabla_1$ in the case of $\nabla_0 = 0$ takes the following form in terms of the connection form $\theta_1$:

$$K_t = tK_1 + t(1 - t)\theta_1^2 + \theta_1 dt$$
$$= t d\theta_1 - t\theta_1^2 + t\theta_1^2 - t^2\theta_1^2 - \theta_1 dt$$
$$= t d\theta_1 - t^2\theta_1 \wedge \theta_1 - \theta_1 dt.$$
