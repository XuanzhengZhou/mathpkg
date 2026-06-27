---
role: proof
locale: en
of_concept: laplace-transform-converse
source_book: gtm012
source_chapter: "4"
source_section: "§5"
---

# Proof of Converse to the Laplace transform theorem

**Existence.** Choose any $b > a$ and let $C(b)$ be the vertical line $\{z \in \mathbb{C} \mid \operatorname{Re} z = b\}$. Define
$$f(t) = \frac{1}{2\pi i} \int_{C(b)} e^{zt} \, g(z) \, dz.$$

The hypothesis $|g(z)| \leq K (1+|z|)^{-2} \exp(-M \operatorname{Re} z)$ guarantees absolute convergence of the integral. Moreover, by differentiating under the integral sign (justified by the quadratic decay in $|z|$), $f$ is continuous.

We verify the three required properties.

(1) **Support condition.** For $t < M$, shift the contour to the right. Since $g$ is holomorphic for $\operatorname{Re} z > a$, and the integrand satisfies
$$|e^{zt} g(z)| \leq K (1+|z|)^{-2} \exp\bigl(\operatorname{Re} z (t - M)\bigr),$$
which decays exponentially as $\operatorname{Re} z \to +\infty$ when $t < M$, Cauchy's theorem implies $f(t) = 0$. Therefore $\operatorname{supp}(f) \subset [M, \infty)$.

(2) **Growth estimate.** For any $b > a$,
$$|f(t)| \leq \frac{1}{2\pi} \int_{C(b)} e^{t \operatorname{Re} z} |g(z)| \, |dz|$$
$$\leq \frac{K}{2\pi} \int_{C(b)} e^{t b} (1+|z|)^{-2} \exp(-M b) \, |dz|$$
$$= C(b) \, K \, e^{b(t-M)},$$
where $C(b) = \frac{1}{2\pi} \int_{-\infty}^{\infty} (1 + \sqrt{b^{2}+y^{2}})^{-2} \, dy$ is finite. Since $b > a$ is arbitrary, we may take any $b > a$ in the estimate, yielding $|f(t)| \leq K' e^{bt}$ for all $t$ (with a possibly adjusted constant).

(3) **Laplace transform.** Compute $Lf(w)$ for $\operatorname{Re} w > b$:
$$Lf(w) = \int_{M}^{\infty} e^{-wt} \left\{ \frac{1}{2\pi i} \int_{C(b)} e^{zt} g(z) \, dz \right\} dt.$$

The iterated integral is absolutely convergent because for $t \in \mathbb{R}$ and $z \in C(b)$,
$$|e^{-wt+zt} g(z)| \leq K (1+|z|)^{-2} \exp\bigl(-M b + t(b - \operatorname{Re} w)\bigr).$$

By Fubini's theorem, we may interchange the order of integration:
$$Lf(w) = \frac{1}{2\pi i} \int_{C(b)} g(z) \left\{ \int_{M}^{\infty} e^{(z-w)t} \, dt \right\} dz.$$

For $\operatorname{Re} w > b$, the inner integral converges:
$$\int_{M}^{\infty} e^{(z-w)t} \, dt = \frac{-e^{(z-w)M}}{z-w}.$$

Thus
$$Lf(w) = \frac{-1}{2\pi i} \int_{C(b)} g(z) \, e^{(z-w)M} \, (z-w)^{-1} \, dz.$$

Now observe that for $\operatorname{Re} w > b$ and $\operatorname{Re} z \geq b$,
$$|g(z) e^{(z-w)M}| \leq K (1+|z|)^{-2} \exp\bigl(-M \operatorname{Re} z + M(\operatorname{Re} z - \operatorname{Re} w)\bigr) = K (1+|z|)^{-2} e^{-M \operatorname{Re} w},$$
which decays quadratically in $|z|$. A standard contour deformation argument (closing the contour to the right and applying Cauchy's integral formula) shows that the integral equals $g(w)$. More precisely, writing the integral as
$$-\frac{e^{-wM}}{2\pi i} \int_{C(b)} \frac{g(z) e^{zM}}{z-w} \, dz,$$
and noting that the integrand $\frac{g(z) e^{zM}}{z-w}$ is meromorphic in the half-plane $\operatorname{Re} z > a$ with a single simple pole at $z = w$, Cauchy's integral formula gives
$$Lf(w) = -e^{-wM} \cdot \left[-g(w) e^{wM}\right] = g(w),$$
where the sign arises from the orientation of the contour.

Therefore $Lf(z) = g(z)$ for all $\operatorname{Re} z > b$, and since $b > a$ was arbitrary, this holds for all $\operatorname{Re} z > a$.

**Uniqueness.** Suppose $f_1, f_2$ both satisfy the conclusion. Then $L(f_1 - f_2) \equiv 0$. By Theorem 5.2 (the Laplace inversion formula), applying the inversion operator to both sides yields $f_1 - f_2 \equiv 0$. Hence $f$ is unique. $\square$
