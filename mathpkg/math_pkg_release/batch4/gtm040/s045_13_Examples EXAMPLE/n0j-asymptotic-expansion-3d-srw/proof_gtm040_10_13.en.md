---
role: proof
locale: en
of_concept: n0j-asymptotic-expansion-3d-srw
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

We start from the integral formula

$$N_{0j} = 3 \int_E \frac{e^{-2\pi i(j \cdot x)} \, dx}{3 - \cos 2\pi x_1 - \cos 2\pi x_2 - \cos 2\pi x_3},$$

where $E = [-1/2, 1/2]^3$. The denominator has the expansion

$$3 - \cos 2\pi x_1 - \cos 2\pi x_2 - \cos 2\pi x_3 = 2\pi^2|x|^2 + \|x\|^4 - \frac{2}{5}\pi^4|x|^4 + \cdots$$

where $\|x\|^4 = x_1^4 + x_2^4 + x_3^4$.

Let $\varphi(x)$ be an infinitely differentiable function defined on $\mathbb{R}^3$ such that $0 \leq \varphi \leq 1$, $\varphi(x) = 1$ for $x$ in a small neighborhood of $0$, and $\varphi(x) = 0$ outside of a slightly larger neighborhood of $0$. Let $\|x\|$ denote the $\ell^4$ norm. Write $f(x)$ for the periodic extension of

$$\frac{3\varphi(x)}{3 - \cos 2\pi x_1 - \cos 2\pi x_2 - \cos 2\pi x_3}.$$

The difference between the integrand and $\vec{f}$ is bounded away from $0$ and is $O(|x|^2)$ near $0$. Moreover, its Laplacian is integrable in $E \setminus \{0\}$. These facts imply that the Fourier coefficients of the difference are $O(|j|^{-2})$ as $j \to \infty$. Hence it is enough to show that the Fourier coefficients of $\vec{f}$ are equal to

$$\frac{3}{2\pi|j|} + O(|j|^{-2}).$$

It is clear from the definitions that

$$\int_E \vec{f}(x) e^{-2\pi ij \cdot x} dx = \int_{\mathbb{R}^3} f(x) e^{-2\pi ij \cdot x} dx.$$

Here the right side is the Fourier transform of $f$ evaluated at $j$. We are thus to estimate the Fourier transform of $f$. Write

$$f(x) = [\varphi(x) - 1] \left[ \frac{3}{2\pi^2|x|^2} + \frac{\|x\|^4}{2|x|^4} \right] + \frac{3}{2\pi^2|x|^2} + \frac{\|x\|^4 - \frac{3}{5}|x|^4}{2|x|^4} + \frac{3}{10},$$

and take the Fourier transform of both sides in the sense of distributions.

The transform of the constant $\frac{3}{10}$ is the distribution supported in the unit ball.

In the third term, the numerator $\|x\|^4 - \frac{3}{5}|x|^4$ is a homogeneous harmonic polynomial, and its Fourier transform is known to be

$$\frac{15}{8\pi} \text{PV} \left[ \frac{\|y\|^4 - \frac{3}{5}|y|^4}{2|y|^7} \right],$$

which decays as $O(|y|^{-3})$.

For the second term $\frac{3}{2\pi^2|x|^2}$, its Fourier transform in $\mathbb{R}^3$ is $\frac{3}{2\pi|y|}$.

For the first term, since $[\varphi(x)-1]$ vanishes near the origin, it is infinitely differentiable. Iterating the Laplacian enough times makes it integrable, giving a bounded Fourier transform. Under multiplication by $|y|^{2k}$ this yields

$$\text{FT(first term)} = O(|y|^{-2k})$$

for sufficiently large $k$.

Since the sum of the transforms of the four terms is a function, we must have, outside the unit ball,

$$\text{FT}(f)(y) = O(|y|^{-2k}) + \frac{3}{2\pi|y|} + O(|y|^{-3}).$$

Evaluating at $j$ (a lattice point) gives

$$\text{FT}(f)(j) = \frac{3}{2\pi|j|} + O(|j|^{-3}),$$

and consequently

$$N_{0j} = \frac{3}{2\pi|j|} + O(|j|^{-2}),$$

as required.
