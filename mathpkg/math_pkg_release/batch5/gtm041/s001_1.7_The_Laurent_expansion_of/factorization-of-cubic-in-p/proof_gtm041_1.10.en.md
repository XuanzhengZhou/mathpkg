---
role: proof
locale: en
of_concept: factorization-of-cubic-in-p
source_book: gtm041
source_chapter: "1"
source_section: "1.10"
---

Since $\wp$ is even, the derivative $\wp'$ is odd: $\wp'(-z) = -\wp'(z)$. The function $\wp'$ has periods $\omega_1$ and $\omega_2$, so $\wp'(z + \omega) = \wp'(z)$ for each period $\omega$.

For the half-period $\omega_1/2$, we have
$$\wp'\left(\frac{\omega_1}{2}\right) = \wp'\left(-\frac{\omega_1}{2} + \omega_1\right) = \wp'\left(-\frac{\omega_1}{2}\right) = -\wp'\left(\frac{\omega_1}{2}\right),$$
hence $\wp'(\omega_1/2) = 0$. Similarly, $\wp'(\omega_2/2) = 0$ and $\wp'((\omega_1 + \omega_2)/2) = 0$.

The differential equation for $\wp$ is
$$[\wp'(z)]^2 = 4\wp^3(z) - g_2\wp(z) - g_3.$$

At each half-period $z$ where $\wp'(z) = 0$, we obtain
$$4\wp^3(z) - g_2\wp(z) - g_3 = 0.$$

Therefore $e_1 = \wp(\omega_1/2)$, $e_2 = \wp(\omega_2/2)$, and $e_3 = \wp((\omega_1+\omega_2)/2)$ are roots of the cubic polynomial $4t^3 - g_2t - g_3$. Since the leading coefficient is $4$, we have the factorization
$$4\wp^3(z) - g_2\wp(z) - g_3 = 4(\wp(z) - e_1)(\wp(z) - e_2)(\wp(z) - e_3).$$

To prove distinctness, suppose two of the $e_i$ coincide, say $e_1 = e_2$. Then $\wp(z) - e_1$ would have a zero of order at least $2$ at both $\omega_1/2$ and $\omega_2/2$. An elliptic function of order $2$ would then have at least $4$ zeros in a fundamental parallelogram (counting multiplicity), which is impossible. The zeros of $\wp'$ in a period parallelogram are precisely the three half-period points (each of order $1$), and $\wp$ takes distinct values at these points.

Since the roots are distinct, the discriminant of the cubic $4t^3 - g_2t - g_3$ does not vanish. Computing the discriminant gives
$$\Delta = 16(g_2^3 - 27g_3^2).$$
Hence $g_2^3 - 27g_3^2 \neq 0$.
