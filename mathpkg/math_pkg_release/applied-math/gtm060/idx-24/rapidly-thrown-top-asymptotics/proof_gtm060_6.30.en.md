---
role: proof
locale: en
of_concept: rapidly-thrown-top-asymptotics
source_book: gtm060
source_chapter: "6"
source_section: "30"
---

The proof proceeds by analyzing the case where the initial angular velocity $\omega_3$ is fixed but the gravitational acceleration $g \to 0$, and then using a similarity argument to reinterpret the result in terms of $\omega_3 \to \infty$.

**Step 1: Locate the displaced minimum.** We apply the perturbed-minimum lemma to the effective potential energy. Setting $\theta = \theta_0 + x$ and expanding around $\theta_0$:

$$\cos \theta = \cos \theta_0 - x \sin \theta_0 + \cdots.$$

The effective potential at $g = 0$ has the Taylor expansion

$$U_{\text{eff}}|_{g=0} = \frac{I_3^2 \omega_3^2}{2I_1} x^2 + \cdots,$$

so in the notation of the lemma, $A = I_3^2 \omega_3^2 / I_1$. The gravitational term is

$$mgl \cos \theta = mgl \cos \theta_0 - x \cdot mgl \sin \theta_0 + \cdots,$$

so $\varepsilon = g$ and $C = -ml \sin \theta_0$. Applying the lemma, the minimum shifts to

$$\theta_g = \theta_0 + x_g, \quad x_g = \frac{I_1 ml \sin \theta_0}{I_3^2 \omega_3^2} \, g + O(g^2).$$

**Step 2: Determine the nutation amplitude.** The axis oscillates near $\theta_g$, and the initial conditions are $\theta = \theta_0$, $\dot{\theta} = 0$. Since $\theta_0$ is the starting (highest) position, the amplitude of nutation for small $g$ is asymptotically

$$a_{\text{nut}} \sim x_g \sim \frac{I_1 ml \sin \theta_0}{I_3^2 \omega_3^2} \, g \quad (g \to 0).$$

**Step 3: Obtain the precession frequency.** From the general formula

$$\dot{\varphi} = \frac{M_z - M_3 \cos \theta}{I_1 \sin^2 \theta},$$

with $M_z = M_3 \cos \theta_0$, expanding for small deviations and using the shifted minimum, one obtains

$$\omega_{\text{prec}} \sim \frac{mgl}{I_3 \omega_3} \quad (g \to 0).$$

**Step 4: Similarity argument.** The equations of motion are homogeneous under the scaling where $\omega_3$ scales simultaneously with $g$. Reinterpreting the $g \to 0$ asymptotics in terms of $\omega_3 \to \infty$ yields the stated asymptotic formulas. Under this reinterpretation, for $\omega_3 \to \infty$:

$$\omega_{\text{nut}} \sim \frac{I_3}{I_1} \omega_3, \quad a_{\text{nut}} \sim \frac{I_1 m g l}{I_3^2 \omega_3^2} \sin \theta_0, \quad \omega_{\text{prec}} \sim \frac{m g l}{I_3 \omega_3}.$$

The nutation frequency is obtained from the lemma's conclusion $f_\varepsilon''(x_\varepsilon) = A + O(\varepsilon)$ applied to the effective potential, which gives $\omega_{\text{nut}}^2 = U_{\text{eff}}''(\theta_g)/I_1 \sim I_3^2 \omega_3^2 / I_1^2$, yielding $\omega_{\text{nut}} \sim (I_3/I_1) \omega_3$.
