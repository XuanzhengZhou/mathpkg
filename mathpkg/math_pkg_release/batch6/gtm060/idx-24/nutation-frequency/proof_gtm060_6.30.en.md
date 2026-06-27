---
role: proof
locale: en
of_concept: nutation-frequency
source_book: gtm060
source_chapter: "6"
source_section: "30"
---

For a Lagrange top whose axis is stably stationary at $\theta_0$, small oscillations in $\theta$ are governed by a one-dimensional effective system with energy

$$E = \frac{I_1}{2} \dot{\theta}^2 + U_{\text{eff}}(\theta),$$

where $U_{\text{eff}}$ attains a minimum at $\theta_0$. The general formula for the frequency of small oscillations in a one-dimensional system with energy $E = a \dot{x}^2/2 + U(x)$ is

$$\omega^2 = \frac{U''(x_0)}{a},$$

where $x_0$ is the minimum of $U$.

Setting $\theta = \theta_0 + x$, the effective potential expands as

$$U_{\text{eff}} = \frac{(M_z - M_3 \cos \theta)^2}{2I_1 \sin^2 \theta} + mgl \cos \theta.$$

For $g = 0$ (no gravity), $M_z = M_3 \cos \theta_0$. Computing the expansion near $\theta_0$:

$$M_z - M_3 \cos \theta = M_3(\cos \theta_0 - \cos(\theta_0 + x)) = M_3 x \sin \theta_0 + O(x^2).$$

Then

$$U_{\text{eff}} = \frac{M_3^2 x^2 \sin^2 \theta_0}{2I_1 \sin^2 \theta_0} + o(x^2) = \frac{I_3^2 \omega_3^2}{2I_1} x^2 + \cdots,$$

where we used $M_3 = I_3 \omega_3$. Thus $U_{\text{eff}}''(\theta_0) = I_3^2 \omega_3^2 / I_1$ and the coefficient $a = I_1$. Applying the frequency formula:

$$\omega_{\text{nut}}^2 = \frac{U_{\text{eff}}''(\theta_0)}{I_1} = \frac{I_3^2 \omega_3^2}{I_1^2},$$

so $\omega_{\text{nut}} = I_3 \omega_3 / I_1$.
