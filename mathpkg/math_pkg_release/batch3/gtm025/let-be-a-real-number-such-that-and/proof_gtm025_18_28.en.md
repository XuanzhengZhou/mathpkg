---
role: proof
locale: en
of_concept: "let-be-a-real-number-such-that-and"
source_book: gtm025
source_chapter: "Differentiation"
source_section: "18.28"
---

We choose an auxiliary function $g$, which for $p > 1$ is an arbitrary function in $\mathfrak{L}_{p'}([- \pi, \pi])$ such that $\|g\|_{p'} \leq 1$, and which for $p = 1$ is the function identically 1. We then write

$$\left| \frac{1}{2\pi} \int_{-\pi}^{\pi} (f(x) - \sigma_n f(x)) g(x) \, dx \right|$$

$$= \left| \frac{1}{2\pi} \int_{-\pi}^{\pi} \left( f(x) \frac{1}{2\pi} \int_{-\pi}^{\pi} K_n(t) \, dt - \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x-t) K_n(t) \, dt \right) g(x) \, dx \right|$$

$$\leq \frac{1}{4\pi^2} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} |f(x) - f(x-t)| |g(x)| K_n(t) \, dt \, dx. \tag{1}$$

We anticipate Fubini's theorem (21.13) [which of course is proved without recourse to the present theorem] to reverse the order of integration in the last expression of (1). This produces

$$\frac{1}{4\pi^2} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} |f(x) - f(x-t)| |g(x)| \, dx K_n(t) \, dt. \tag{2}$$

Now use Hölder's inequality (13.4.ii) on the inner integral in (2):

$$\frac{1}{2\pi} \int_{-\pi}^{\pi} |f(x) - f

matter how small $\delta$ may be. That is, the first expression in (4) is arbitrarily small for $n$ sufficiently large. This implies by (15.1) that

$$\lim_{n \to \infty} \|f - \sigma_n f\|_p = 0 \quad (p > 1).$$

For $p = 1$, use (3) and repeat the argument with obvious changes. $\square$

Our point in going through (18.28) was to lead up to the much subtler fact that $\sigma_n f$ converges to $f$ not merely "in the mean" [i.e., in the $\mathfrak{L}_p$ norm] but also pointwise almost everywhere.
