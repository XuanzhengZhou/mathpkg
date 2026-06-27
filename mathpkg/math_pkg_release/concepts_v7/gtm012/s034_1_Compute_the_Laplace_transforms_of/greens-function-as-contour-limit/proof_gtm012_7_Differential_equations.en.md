---
role: proof
locale: en
of_concept: greens-function-as-contour-limit
source_book: gtm012
source_chapter: "7"
source_section: "Differential equations"
---

# Proof of Existence and Form of the Green's Function as a Contour Integral

**Theorem 7.2.** Suppose $p$ is a polynomial of degree $n \geq 1$; suppose $z_1, z_2, \ldots, z_r$ are the distinct roots of $p$, with multiplicities $m_1, m_2, \ldots, m_r$. Then the limit

$$G(t) = \lim_{R \to \infty} \frac{1}{2\pi i} \int_{C_R} e^{tz} p(z)^{-1} \, dz$$

exists. Moreover, $G(t) = 0$ for $t < 0$ (and also for $t = 0$ if $n > 1$). For $t > 0$, $G(t)$ is a linear combination of the functions

$$t^k \exp(z_j t), \qquad 0 \leq k < m_j.$$

**Proof.** Recall that $C_R$ is the directed line segment from $b - iR$ to $b + iR$, where $b$ is chosen large enough so that all roots of $p$ lie in the half-plane $\operatorname{Re} z < b$. Let $M = \max\{\operatorname{Re} z_j\}$ and choose $b > M$.

*Case $t < 0$.* For $R > 0$, let $D_R$ be the rectangle with vertices $b \pm iR$, $(b + R^{1/2}) \pm iR$, oriented counterclockwise. On the right vertical side $\operatorname{Re} z = b + R^{1/2}$, we have the estimate

$$|e^{tz} p(z)^{-1}| \leq c(t) \exp(t R^{1/2}) (R^{1/2})^{-n} \to 0 \quad \text{as } R \to \infty,$$

since $t < 0$. On the horizontal sides, $|\operatorname{Im} z| = R$ and $b \leq \operatorname{Re} z \leq b + R^{1/2}$, so

$$|e^{tz} p(z)^{-1}| \leq c'(t) \exp(t b) R^{-n} \to 0 \quad \text{as } R \to \infty.$$

Thus the integrals over the non-$C_R$ sides of $D_R$ converge to $0$ as $R \to \infty$. Since the integrand $e^{tz} p(z)^{-1}$ is holomorphic inside $D_R$, Cauchy's theorem gives

$$\frac{1}{2\pi i} \int_{\partial D_R} e^{tz} p(z)^{-1} \, dz = 0.$$

Therefore

$$\frac{1}{2\pi i} \int_{C_R} e^{tz} p(z)^{-1} \, dz \to 0 \quad \text{as } R \to \infty,$$

so $G(t) = 0$ for $t < 0$. If $n > 1$, the estimates also give $G(0) = 0$.

*Case $t > 0$.* Let $D_R$ be the rectangle with vertices $b \pm iR$, $(b - R^{1/2}) \pm iR$, oriented counterclockwise. For sufficiently large $R$, $D_R$ contains all roots of $p(z)$. On the left vertical side $\operatorname{Re} z = b - R^{1/2}$, we have

$$|e^{tz} p(z)^{-1}| \leq c(t) \exp(t(b - R^{1/2})) R^{-n/2} \to 0 \quad \text{as } R \to \infty,$$

since $\exp(-t R^{1/2})$ dominates. On the horizontal sides, similar estimates show the integrals tend to $0$. Since the integral over $\partial D_R$ is independent of $R$ (the integrand is meromorphic and all poles lie inside $D_R$ for large $R$), the limit in the definition of $G(t)$ exists and equals the contour integral over any sufficiently large closed curve enclosing all roots of $p$:

$$G(t) = \frac{1}{2\pi i} \int_{\partial D_R} e^{tz} p(z)^{-1} \, dz, \qquad t > 0.$$

Now we apply the Residue Theorem. The integrand $e^{tz} p(z)^{-1}$ has poles at $z_1, \ldots, z_r$. At a pole $z_j$ of order $m_j$, expand $p(z)^{-1}$ in a Laurent series:

$$p(z)^{-1} = \sum_{m \geq -m_j} b_m (z - z_j)^m.$$

Also expand $e^{tz}$ around $z_j$:

$$e^{tz} = e^{tz_j} e^{t(z - z_j)} = e^{tz_j} \sum_{m \geq 0} \frac{t^m}{m!} (z - z_j)^m.$$

The residue at $z_j$ is the coefficient of $(z - z_j)^{-1}$ in the product of these expansions. This coefficient is a linear combination of $t^k \exp(z_j t)$ for $0 \leq k < m_j$, specifically

$$\operatorname{Res}(e^{tz} p(z)^{-1}; z_j) = e^{tz_j} \sum_{k=0}^{m_j-1} \frac{t^k}{k!} \, b_{-1-k}.$$

Therefore

$$G(t) = \sum_{j=1}^{r} \sum_{k=0}^{m_j-1} c_{jk} \, t^k \exp(z_j t), \qquad t > 0,$$

where the constants $c_{jk}$ are determined by the Laurent coefficients of $p(z)^{-1}$ at $z_j$.

$\square$
