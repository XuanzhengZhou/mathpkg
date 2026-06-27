---
role: proof
locale: en
of_concept: symmetric-distribution-characterization
source_book: gtm095
source_chapter: "2"
source_section: "12"
---

# Proof of Characterization of Symmetric Distributions via Characteristic Functions

Let $F$ be a symmetric distribution function, i.e., $F(x) = 1 - F(-x+)$ for continuity points. If $g(x)$ is a bounded odd Borel function, then $\int_R g(x) dF(x) = 0$. (For simple odd functions this follows directly from the definition of symmetry of $F$; the general case follows by approximation.)

Taking $g(x) = \sin tx$, which is an odd function, we have $\int_R \sin tx\, dF(x) = 0$. Consequently,

$$\varphi(t) = \int_{-\infty}^{\infty} e^{itx} dF(x) = \int_{-\infty}^{\infty} (\cos tx + i \sin tx) dF(x) = \int_{-\infty}^{\infty} \cos tx\, dF(x) = \mathsf{E}\, \cos t\xi,$$

which is a real-valued function.

Conversely, let $\varphi_\xi(t)$ be a real-valued function. Then by Property (3),

$$\varphi_{-\xi}(t) = \varphi_\xi(-t) = \overline{\varphi_\xi(t)} = \varphi_\xi(t).$$

Since the characteristic function uniquely determines the distribution (Theorem 2, Uniqueness), it follows that $\xi$ and $-\xi$ have the same distribution, i.e., the distribution of $\xi$ is symmetric.
