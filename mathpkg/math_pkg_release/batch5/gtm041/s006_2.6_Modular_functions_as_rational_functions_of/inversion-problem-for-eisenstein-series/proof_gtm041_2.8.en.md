---
role: proof
locale: en
of_concept: inversion-problem-for-eisenstein-series
source_book: gtm041
source_chapter: "2"
source_section: "2.8"
---

We consider three cases: (1) $a_2 = 0$; (2) $a_3 = 0$; (3) $a_2 a_3 \neq 0$.

**Case 1.** $a_2 = 0$. Then the condition $a_2^3 - 27a_3^2 \neq 0$ implies $a_3 \neq 0$. Choose $\tau = \rho = e^{2\pi i / 3}$. From the proof of $g_2(\rho) = 0$ (Theorem 2.5), we have $g_2(1, \rho) = 0$. Since $g_3(1, \rho) \neq 0$ (otherwise $\Delta = 0$, contradicting $\Delta$ being a non-zero cusp form), choose $\omega_1$ such that $\omega_1^6 = g_3(1, \rho) / a_3$ and let $\omega_2 = \rho \omega_1$. Then

$$g_2(\omega_1, \omega_2) = \frac{1}{\omega_1^4} g_2(1, \rho) = 0 = a_2,$$

$$g_3(\omega_1, \omega_2) = \frac{1}{\omega_1^6} g_3(1, \rho) = a_3.$$

**Case 2.** $a_3 = 0$. Then $a_2 \neq 0$. Choose $\tau = i$. We have $g_3(1, i) = 0$ (by a computation similar to $g_2(\rho) = 0$) and $g_2(1, i) \neq 0$. Choose $\omega_1$ such that $\omega_1^4 = g_2(1, i) / a_2$ and let $\omega_2 = i \omega_1$. Then

$$g_2(\omega_1, \omega_2) = \frac{1}{\omega_1^4} g_2(1, i) = a_2,$$

$$g_3(\omega_1, \omega_2) = \frac{1}{\omega_1^6} g_3(1, i) = 0 = a_3.$$

**Case 3.** Assume $a_2 \neq 0$ and $a_3 \neq 0$. Choose a complex $\tau$ with $\operatorname{Im} \tau > 0$ such that

$$J(\tau) = \frac{a_2^3}{a_2^3 - 27a_3^2}.$$

Such a $\tau$ exists because $J$ maps the upper half-plane onto the whole complex plane. Note that $J(\tau) \neq 0$ since $a_2 \neq 0$, and

$$\frac{J(\tau) - 1}{J(\tau)} = \frac{27a_3^2}{a_2^3}.$$

For this $\tau$, choose $\omega_1$ to satisfy

$$\omega_1^2 = \frac{a_2}{a_3} \cdot \frac{g_3(1, \tau)}{g_2(1, \tau)}$$

and let $\omega_2 = \tau \omega_1$. Then

$$\frac{g_2(\omega_1, \omega_2)}{g_3(\omega_1, \omega_2)} = \frac{\omega_1^{-4} g_2(1, \tau)}{\omega_1^{-6} g_3(1, \tau)} = \omega_1^2 \frac{g_2(1, \tau)}{g_3(1, \tau)} = \frac{a_2}{a_3},$$

so

$$g_3(\omega_1, \omega_2) = \frac{a_3}{a_2} g_2(\omega_1, \omega_2).$$

Using the relation between $g_2$ and $\Delta$, one computes

$$\frac{g_2^3(\omega_1, \omega_2)}{g_2^3(\omega_1, \omega_2) - 27g_3^2(\omega_1, \omega_2)} = \frac{g_2^3(1, \tau)}{g_2^3(1, \tau) \omega_1^{12} - 27g_3^2(1, \tau) \omega_1^{12}} \cdot \omega_1^{12}$$

$$= \frac{g_2^3(1, \tau)}{g_2^3(1, \tau) - 27g_3(1, \tau)^2} = J(\tau) = \frac{a_2^3}{a_2^3 - 27a_3^2}.$$

Together with $g_3 = (a_3 / a_2) g_2$, solving these equations yields $g_2(\omega_1, \omega_2) = a_2$ and $g_3(\omega_1, \omega_2) = a_3$ as required.
