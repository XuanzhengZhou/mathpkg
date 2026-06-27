---
role: proof
locale: en
of_concept: "let-if-the-identity-holds-then-in"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.34"
---

Let $\mathfrak{T}$ be the set of all trigonometric polynomials on $T$, defined as in the proof of (16.32). If $f = 0$, then it is obvious that

$$\int_{-\pi}^{\pi} f(t) p(t) dt = 0$$

for all $p \in \mathfrak{T}$. Let $x$ be a fixed number in $[-\pi, \pi]$. It is easy to construct a nondecreasing sequence $(g_n)_{n=1}^{\infty}$ of nonnegative continuous functions such that:

$$g_n(-\pi) = g_n(\pi) = 0;$$

$$\lim_{n \to \infty} g_n(t) = \xi_{1-\pi,x}(t) \quad \text{for all} \quad t \in [-\pi, \pi].$$

By (7.35.b), there exists for each $n \in N$ a polynomial $p_n \in \mathfrak{T}$ such that $\|g_n - p_n\|_u < \frac{1}{n}$. Then we have

$$f(t) \xi_{1-\pi,x}(t) =

such that $|\hat{g}(n)| < \frac{\varepsilon}{2}$ whenever $|n| \geq p$. Hence $|n| \geq p$ implies

$$|f(n)| \leq |f(n) - \hat{g}(n)| + |\hat{g}(n)|$$
$$< \left| \frac{1}{2\pi} \int_{-\pi}^{\pi} (f(x) - g(x)) \exp(-i nx) \, dx \right| + \frac{\varepsilon}{2}$$
$$\leq \frac{1}{2\pi} \int_{-\pi}^{\pi} |f(x) - g(x)| \, dx + \frac{\varepsilon}{2}$$
$$< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

(16.36) Remark. There is an analogous theory of Fourier transforms for the space $\mathfrak{L}_1(R, \mathcal{M}_\lambda, \lambda) = \mathfrak{L}_1(R)$. In this case, one defines

$$f(y) = (2\pi)^{-\frac{1}{2}} \int_{R} f(x) \exp(-i yx) \, dx$$

for each $y \in R$. Once again the equality $f = 0$ implies $f = 0$ a.e. Also, $\lim_{|y| \to \infty} f(y) = 0$. These transforms are important in several parts of analysis. Using them, it is possible to prove that the Hermite functions are a complete orthonormal set in $\mathfrak{L}_2(R)$; for a short proof, see (21.64.b) infra.
