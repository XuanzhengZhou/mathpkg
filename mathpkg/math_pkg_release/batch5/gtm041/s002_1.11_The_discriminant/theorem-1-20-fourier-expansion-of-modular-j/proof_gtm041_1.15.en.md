---
role: proof
locale: en
of_concept: theorem-1-20-fourier-expansion-of-modular-j
source_book: gtm041
source_chapter: "1"
source_section: "1.15"
---

From the definitions,
$$g_2(\tau) = \frac{4\pi^4}{3}\left(1 + 240A\right), \quad g_3(\tau) = \frac{8\pi^6}{27}\left(1 - 504B\right),$$
where
$$A = \sum_{n=1}^{\infty} \sigma_3(n) x^n, \quad B = \sum_{n=1}^{\infty} \sigma_5(n) x^n, \quad x = e^{2\pi i\tau}.$$

The discriminant is $\Delta = g_2^3 - 27g_3^2$. Substituting the expressions,
$$\Delta = \frac{64\pi^{12}}{27}\left[(1 + 240A)^3 - (1 - 504B)^2\right].$$

Expanding,
$$(1 + 240A)^3 - (1 - 504B)^2 = 12^2(5A + 7B) + 12^3(100A^2 - 147B^2 + 8000A^3).$$

Since $5d^3 + 7d^5$ is divisible by 12 for every integer $d$, the coefficients of $5A + 7B$ are divisible by 12. Hence the entire series is divisible by $12^3$, giving
$$\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^{\infty} \tau(n) x^n,$$
where $\tau(n)$ are integers with $\tau(1) = 1$, $\tau(2) = -24$. The function $\tau(n)$ is called Ramanujan's tau function.

Now $J = g_2^3 / \Delta$. Writing
$$g_2^3 = \frac{64\pi^{12}}{27}(1 + 240A)^3 = \frac{64\pi^{12}}{27}\left(1 + \sum_{n=1}^{\infty} a_n x^n\right)$$
with integer $a_n$, and using $\Delta = (2\pi)^{12} x \prod_{n=1}^{\infty}(1 - x^n)^{24}$ (the product formula derived from the Dedekind eta function), we obtain the Fourier expansion
$$12^3 J(\tau) = e^{-2\pi i\tau} + 744 + \sum_{n=1}^{\infty} c(n) e^{2\pi i n\tau},$$
where $c(n)$ are integers. This expansion converges absolutely for $\tau \in H$.
