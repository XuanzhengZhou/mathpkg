---
role: proof
locale: en
of_concept: finite-variance-hitting-time-asymptotic
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

For $0 \leq t < 1$, $U(t) = \sum_{n=0}^{\infty} t^n P_n(0,0) = \frac{1}{2\pi} \int_{-\pi}^{\pi} \frac{d\theta}{1 - t\phi(\theta)}$. Near $\theta = 0$, $1 - \phi(\theta) \sim \frac{1}{2}\sigma^2\theta^2$. By T7.1, the integral away from 0 remains bounded as $t \to 1$ (aperiodicity). Hence
$$\lim_{t \to 1} \sqrt{1-t} \, U(t) = \frac{1}{\sqrt{2}\,\sigma},$$
verified by the substitution $x = \theta\sigma[2(1-t)]^{-1/2}$.

The renewal identity $\sum R_n t^n = [(1-t)U(t)]^{-1}$ (P1.2) gives
$$\lim_{t \to 1} \sqrt{1-t} \sum_{n=0}^{\infty} R_n t^n = \sigma\sqrt{2}.$$

Since $R_n = P_0[T > n]$ is monotone nonincreasing, Karamata's theorem (P20.2) yields $\lim_{n\to\infty} \sqrt{n}R_n = \sigma\sqrt{2}/\Gamma(3/2) = \sigma\sqrt{2/\pi}$.
