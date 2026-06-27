---
role: proof
locale: en
of_concept: fubinis-theorem
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Fubini's Theorem

**Fubini's Theorem.** Let $(\Omega_1, \mathcal{F}_1, \rho_1)$ and $(\Omega_2, \mathcal{F}_2, \rho_2)$ be spaces with $\sigma$-finite measures, and let $\xi = \xi(\omega_1, \omega_2)$ be an $\mathcal{F}_1 \otimes \mathcal{F}_2$-measurable function, integrable with respect to the product measure $\rho_1 \times \rho_2$:

$$\int_{\Omega_1 \times \Omega_2} |\xi(\omega_1, \omega_2)| d(\rho_1 \times \rho_2) < \infty. \tag{47}$$

Then the integrals $\int_{\Omega_1} \xi(\omega_1, \omega_2) \rho_1(d\omega_1)$ and $\int_{\Omega_2} \xi(\omega_1, \omega_2) \rho_2(d\omega_2)$

(1) are defined for $\rho_2$-almost all $\omega_2$ and $\rho_1$-almost all $\omega_1$;
(2) are respectively $\mathcal{F}_2$- and $\mathcal{F}_1$-measurable functions;
(3) satisfy

$$\int_{\Omega_1 \times \Omega_2} \xi(\omega_1, \omega_2) d(\rho_1 \times \rho_2) = \int_{\Omega_1} \left[ \int_{\Omega_2} \xi(\omega_1, \omega_2) \rho_2(d\omega_2) \right] \rho_1(d\omega_1)$$
$$= \int_{\Omega_2} \left[ \int_{\Omega_1} \xi(\omega_1, \omega_2) \rho_1(d\omega_1) \right] \rho_2(d\omega_2).$$

*Proof.* We first show that $\xi(\omega_1, \cdot)$ is $\mathcal{F}_2$-measurable with respect to $\omega_2$, for each $\omega_1 \in \Omega_1$. This follows from the fact that for a fixed $\omega_1$, the section of a measurable set in the product $\sigma$-algebra is measurable (a standard result in measure theory).

Now let $\xi(\omega_1, \omega_2) \geq 0$. Then, since the function $\xi(\omega_1, \cdot)$ is $\mathcal{F}_2$-measurable for each $\omega_1$, the integral $\int_{\Omega_2} \xi(\omega_1, \omega_2) \rho_2(d\omega_2)$ is defined. We show that this integral is an $\mathcal{F}_1$-measurable function and

$$\int_{\Omega_1} \left[ \int_{\Omega_2} \xi(\omega_1, \omega_2) \rho_2(d\omega_2) \right] \rho_1(d\omega_1) = \int_{\Omega_1 \times \Omega_2} \xi(\omega_1, \omega_2) d(\rho_1 \times \rho_2).$$

The proof proceeds by the standard method:

- **Rectangles:** For $\xi(\omega_1, \omega_2) = I_{A \times B}(\omega_1, \omega_2) = I_A(\omega_1) I_B(\omega_2)$ with $A \in \mathcal{F}_1$, $B \in \mathcal{F}_2$, we have

$$\int_{\Omega_2} I_{A \times B}(\omega_1, \omega_2) \rho_2(d\omega_2) = I_A(\omega_1) \rho_2(B),$$

which is $\mathcal{F}_1$-measurable, and

$$\int_{\Omega_1} \left[ \int_{\Omega_2} I_{A \times B} d\rho_2 \right] d\rho_1 = \rho_1(A)\rho_2(B) = (\rho_1 \times \rho_2)(A \times B).$$

- **General measurable sets:** For $\xi = I_F$ with $F \in \mathcal{F}_1 \otimes \mathcal{F}_2$, the $\mathcal{F}_1$-measurability of $\int_{\Omega_2} I_F(\omega_1, \omega_2) \rho_2(d\omega_2)$ is established via the monotone class theorem. The equality of iterated and product integrals for $I_F$ follows by considering the set function $\lambda(F) = \int_{\Omega_1} \left[\int_{\Omega_2} I_F d\rho_2\right] d\rho_1$, which agrees with $\rho_1 \times \rho_2$ on rectangles, and hence, by Carathéodory's extension theorem (uniqueness of extension), on all of $\mathcal{F}_1 \otimes \mathcal{F}_2$.

- **Nonnegative functions:** Extend from indicator functions to simple functions by linearity, then to general nonnegative $\xi$ via the Monotone Convergence Theorem (approximating $\xi$ from below by simple functions).

- **General integrable functions:** Decompose $\xi = \xi^+ - \xi^-$. Since $\xi$ is integrable, $\int \xi^+ d(\rho_1 \times \rho_2) < \infty$ and $\int \xi^- d(\rho_1 \times \rho_2) < \infty$. Applying the result for nonnegative functions to $\xi^+$ and $\xi^-$, we obtain

$$\int_{\Omega_2} \xi^+(\omega_1, \omega_2) \rho_2(d\omega_2) < \infty \quad (\rho_1\text{-a.s.}),$$
$$\int_{\Omega_2} \xi^-(\omega_1, \omega_2) \rho_2(d\omega_2) < \infty \quad (\rho_1\text{-a.s.}),$$

and therefore $\int_{\Omega_2} |\xi(\omega_1, \omega_2)| \rho_2(d\omega_2) < \infty$ ($\rho_1$-a.s.). Except on a set $N$ of $\rho_1$-measure zero,

$$\int_{\Omega_2} \xi(\omega_1, \omega_2) \rho_2(d\omega_2) = \int_{\Omega_2} \xi^+ d\rho_2 - \int_{\Omega_2} \xi^- d\rho_2.$$

Defining the integral to be $0$ for $\omega_1 \in N$, we may suppose this holds for all $\omega_1 \in \Omega_1$. Integrating with respect to $\rho_1$ and using the result for nonnegative functions yields the desired equality. The symmetric argument for the other iteration order is identical. $\square$
