---
role: proof
locale: en
of_concept: "let-be-an-approximate-unit-in-if-then"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.37"
---

Let $f \in \mathfrak{L}_p(R)$ and let $\varepsilon > 0$ be given. Apply (13.24) to obtain a neighborhood $V$ of 0 in $R$ such that $2 \|f_{-y} - f\|_p < \varepsilon$ whenever $y \in V$. Next use (21.36.iii) to choose an $n_0 \in N$ such that $4 \|f\|_p \int_{V'} u_n(y) dy < \varepsilon$ for all $n \geq n_0$. Now fix an arbitrary $n \geq n_0$. Then (21.31) or (21.32) shows that $(f * u_n - f) \in \mathfrak{L}_p(R)$, and so for any $h \in \mathfrak{

(b) Recall our definition (16.36) of the Fourier transform $f$ of a function $f \in \mathfrak{L}_1(R)$: for all $y \in R$,

(i) $f(y) = (2\pi)^{-\frac{1}{2}} \int_{R} f(x) \exp(-ixy) dx$.

The factor $(2\pi)^{-\frac{1}{2}}$ in (i) is placed there as a matter of convenience. The reader will note the normalization used in the definition of Fourier coefficients $f(n)$ (16.33): we divided all integrals by $2\pi$. This was done to render the set $\{ \exp(inx) \}_{n \in Z}$ orthonormal over $[-\pi, \pi]$, and had useful by-products in (16.37), (18.28), and (18.29). All of these theorems would be slightly more complicated to state had we used $\int_{-\pi}^{\pi} \cdots d\lambda$ instead of $(2\pi)^{-1} \int_{-\pi}^{\pi} \cdots d\lambda$. The situation is similar in the case of Fourier transforms. There are good reasons for "normalizing" our integrals with the factor $(2\pi)^{-\frac{1}{2}}$, and we will point them out at the appropriate places.

(c) It is in fact convenient to replace all integrals $\int_{R} \cdots d\lambda$ by $(2\pi)^{-\frac{1}{2}} \int_{R} \cdots d\lambda$. Let us agree to do this throughout (21.38)–(21.66). Let us also agree that in (21.38)–(21.66),

$$\|f\|_p = \left[ (2\pi)^{-\frac{1}{2}} \int_{R} |f|^p d\lambda \right]^{\frac{1}{p}}$$

for $1 \leq p < \infty$. With this reinterpretation, we have

$$f * g(x) = (2\pi)^{-\frac{1}{2}} \int_{R

Thus

$$2 |f(y)| = \left| (2\pi)^{-\frac{1}{2}} \int_{R} f(x) \exp(-ixy) \, dx - (2\pi)^{-\frac{1}{2}} \int_{R} f\left(x - \frac{\pi}{y}\right) \exp(-ixy) \, dx \right|$$

$$\leq (2\pi)^{-\frac{1}{2}} \int_{R} \left| f(x) - f\left(x - \frac{\pi}{y}\right) \right| \cdot |\exp(-ixy)| \, dx$$

$$= (2\pi)^{-\frac{1}{2}} \int_{R} \left| f(x) - f\left(x - \frac{\pi}{y}\right) \right| \, dx.$$

A look at (13.24) shows that $|f(y)|$ is arbitrarily small if $|y|$ is sufficiently large.

It remains to show that $f$ is continuous. Given $\varepsilon > 0$, choose a compact interval $I = [-a, a]$ ($a > 0$) such that

$$4 \int_{I'} |f(x)| \, dx < \varepsilon$$

and then choose $\delta > 0$ such that

$$2a\delta \int_{-a}^{a} |f(x)| \, dx < \varepsilon.$$

Since $|\sin(u)| \leq |u|$ for all $u \in R$, it follows from (1) and (2) that if $y, t \in R$ and $|t| < \delta$, then

$$(2\pi)^{\frac{1}{2}} |f(y+t) - f(y)| = \left| \int_{R} f(x) \exp(-ixy) \left(\exp(-itx) - 1\right) \, dx \right|$$

$$\leq \int_{R} |f(x)| \cdot |\exp(-itx) - 1| \, dx$$

$$= \int_{R} |f(x)| \cdot 2 \left| \sin\left(\frac{tx}{2}\right) \right| \, dx$$

$$\leq

Our next theorem shows that this transformation also preserves products [convolution in $\mathfrak{L}_1$ turns into pointwise multiplication in $\mathfrak{C}_0$]. The Fourier transform is also one-to-one (21.47) and its range is uniformly dense in $\mathfrak{C}_0$ (21.62.b). There seems to be no simple way to describe intrinsically the functions in $\mathfrak{C}_0$ that have the form $f$ for some $f \in \mathfrak{L}_1$.
