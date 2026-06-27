---
role: proof
locale: en
of_concept: weight-formula-for-zeros-of-entire-modular-form
source_book: gtm041
source_chapter: "6"
source_section: "6.3"
---

**Proof.** The proof follows the same contour integration method as Theorem 2.4, integrating $f'/f$ around the boundary of the fundamental region $R_\Gamma$ with small circular detours around zeros on the boundary and a horizontal cut-off at $\operatorname{Im}(\tau) = M$. Calculating the limiting value of the integral as $M \to \infty$ and the circular detours shrink to their centers yields

$$N = \frac{k}{12} - \frac{1}{2} N(i) - \frac{1}{3} N(\rho) - N(i\infty).$$

The only essential difference between this result and the weight-0 case (Theorem 2.4) is the appearance of the term $k/12$. This comes from the weight factor $(c\tau + d)^k$ in the functional equation

$$f(A(\tau)) = (c\tau + d)^k f(\tau),$$

where $A(\tau) = (a\tau + b)/(c\tau + d)$. Differentiation of this equation gives

$$f'(A(\tau)) A'(\tau) = (c\tau + d)^k f'(\tau) + kc(c\tau + d)^{k-1} f(\tau),$$

from which we find the logarithmic derivative relation

$$\frac{f'(A(\tau)) A'(\tau)}{f(A(\tau))} = \frac{f'(\tau)}{f(\tau)} + \frac{kc}{c\tau + d}.$$

Consequently, for any path $\gamma$ not passing through a zero, we have

$$\frac{1}{2\pi i} \int_{A(\gamma)} \frac{f'(u)}{f(u)} \, du = \frac{1}{2\pi i} \int_{\gamma} \frac{f'(\tau)}{f(\tau)} \, d\tau + \frac{1}{2\pi i} \int_{\gamma} \frac{kc}{c\tau + d} \, d\tau.$$

Therefore the integrals along the arcs (2) and (3) in Figure 2.5 do not cancel as they did in the proof of Theorem 2.4 unless $k = 0$. Instead, they make a contribution whose limiting value is equal to

$$\frac{-k}{2\pi i} \int_{\rho}^{i} \frac{d\tau}{\tau} = \frac{-k}{2\pi i} (\log i - \log \rho) = \frac{-k}{2\pi i} \left(\frac{\pi i}{2} - \frac{2\pi i}{3}\right) = \frac{-k}{2\pi i} \cdot \left(-\frac{\pi i}{6}\right) = \frac{k}{12}.$$

Adding this contribution to the zeros counted by the argument principle yields the stated formula. $\square$
