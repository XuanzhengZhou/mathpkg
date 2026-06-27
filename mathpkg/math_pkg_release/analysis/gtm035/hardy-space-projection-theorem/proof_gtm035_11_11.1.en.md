---
role: proof
locale: en
of_concept: hardy-space-projection-theorem
source_book: gtm035
source_chapter: "11"
source_section: "11.1"
---
# Proof of H^2 Projection Theorem for Maximum Modulus Algebras

**Theorem 11.1.** Fix $F \in A$. Let $G$ denote the orthogonal projection in $L^2(\mu)$ of $F$ to $\mathcal{C}$. Then

(8) $G(0) = F(x^0)$, and

(9) $G \in H^2(\Gamma)$.

Moreover, for almost all $\lambda \in \Gamma$, $G(\lambda)$ lies in the closed convex hull of $F(p^{-1}(\lambda))$.

*Proof.* We now fix a positive integer $n$ and put $g = \bar{p}^n$. Then $g$ is identified with $\bar{\lambda}^n$ in $L^2(\Gamma, \frac{d\theta}{2\pi})$, and so we get

$$\int_Y Fp^n d\mu = \frac{1}{2\pi} \int_\Gamma G\lambda^n d\theta.$$

By choice of $\mu$ and choice of $x^0$, the left-hand side equals $F(x^0)(p(x^0))^n = 0$, since $p(x^0) = 0$. So

$$0 = \int_\Gamma G(e^{i\theta})e^{in\theta} d\theta, \quad n = 1, 2, \ldots.$$

Thus $G$ belongs to the Hardy space $H^2$ on $\Gamma$, proving (9).

Taking $g = 1$ in the identity above, we get

$$F(x^0) = \int_Y F d\mu = \frac{1}{2\pi} \int_\Gamma G d\theta = G(0),$$

so assertion (8) holds.

Fix next $\lambda_0 = e^{i\theta_0} \in \Gamma$. For each $\delta > 0$, let $\alpha$ denote the arc of $\Gamma$ from $e^{i(\theta_0 - \delta)}$ to $e^{i(\theta_0 + \delta)}$ and put

$$g_\delta(e^{i\theta}) = \begin{cases} \frac{\pi}{\delta}, & \theta_0 - \delta \leq \theta \leq \theta_0 + \delta \\ 0, & |\theta - \theta_0| > \delta \end{cases}$$

so that

$$\int_Y F\bar{g}_\delta d\mu = \frac{1}{2\pi} \int_\Gamma G\bar{g}_\delta d\theta = \frac{1}{2\delta} \int_{\theta_0 - \delta}^{\theta_0 + \delta} G(e^{i\theta})d\theta.$$

Also, $\int_Y \bar{g}_\delta \circ p \, d\mu = \frac{1}{2\delta} \int_{\theta_0 - \delta}^{\theta_0 + \delta} d\theta = 1$.

Now fix $\theta_0$ such that $\lambda_0 = e^{i\theta_0}$ is a Lebesgue point of $G$ on $\Gamma$. Letting $\delta \to 0$, we obtain that $G(\lambda_0)$ belongs to the closed convex hull of the values of $F$ on $p^{-1}(\lambda_0)$, i.e.,

$$G(\lambda) \in \overline{\operatorname{co}}(F(p^{-1}(\lambda))) \quad \text{for a.a. } \lambda \in \Gamma.$$

This completes the proof. $\square$
