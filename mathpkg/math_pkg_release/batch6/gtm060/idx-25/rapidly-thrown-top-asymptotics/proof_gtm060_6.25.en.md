---
role: proof
locale: en
of_concept: rapidly-thrown-top-asymptotics
source_book: gtm060
source_chapter: "6"
source_section: "25"
---

Consider the case when the initial angular velocity is fixed, but $g \to 0$. By interpreting the formulas with the aid of a similarity argument (cf. Section B), the behavior as $\omega_3 \to \infty$ is equivalent to the behavior as $g \to 0$.

Apply the lemma on perturbation of a minimum to locate the minimum point $\theta_g$ of the effective potential energy. Set
$$\theta = \theta_0 + x, \quad \cos \theta = \cos \theta_0 - x \sin \theta_0 + \cdots.$$

The Taylor expansion in $x$ at $\theta_0$ gives
$$U_{\text{eff}}\big|_{g=0} = \frac{I_3^2 \omega_3^2}{2I_1} x^2 + \cdots, \quad mgl \cos \theta = mgl \cos \theta_0 - x\, mgl \sin \theta_0 + \cdots.$$

Applying the lemma to $f = U_{\text{eff}}\big|_{g=0}$, $\varepsilon = g$, $h = ml \cos(\theta_0 + x)$, we find that the minimum of the effective potential energy $U_{\text{eff}}$ is attained at an angle of inclination
$$\theta_g = \theta_0 + x_g, \quad x_g = \frac{I_1 ml \sin \theta_0}{I_3^2 \omega_3^2}\, g + O(g^2).$$

Thus the inclination $\theta$ of the top's axis will oscillate near $\theta_g$. But at the initial moment, $\theta = \theta_0$ and $\dot{\theta} = 0$. This means that $\theta_0$ corresponds to the highest position of the axis of the top. Therefore, for small $g$, the amplitude of nutation is asymptotically equal to
$$a_{\text{nut}} \sim x_g \sim \frac{I_1 ml \sin \theta_0}{I_3^2 \omega_3^2}\, g \quad (g \to 0).$$

From the general formula
$$\dot{\phi} = \frac{M_z - M_3 \cos \theta}{I_1 \sin^2 \theta}$$
and the condition $M_z = M_3 \cos \theta_0$, substitution of $\theta = \theta_0 + x$ yields the precession frequency as $\omega_{\text{prec}} \sim mgl/(I_3 \omega_3)$.

For the nutation frequency, applying the lemma's conclusion about the second derivative gives
$$\omega_{\text{nut}}^2 = \frac{U''_{\text{eff}}(\theta_g)}{I_1} = \frac{I_3^2 \omega_3^2}{I_1^2} + O(g),$$
so $\omega_{\text{nut}} \sim (I_3/I_1) \omega_3$. Reversing the similarity argument ($g \to 0$ equivalent to $\omega_3 \to \infty$) yields the stated asymptotic formulas.
