---
role: proof
locale: en
of_concept: rademacher-series-for-partition-function
source_book: gtm041
source_chapter: "5"
source_section: "5.6"
---

We begin with Cauchy's integral formula for the partition function:
$$
p(n) = \frac{1}{2\pi i} \int_C \frac{F(x)}{x^{n+1}} \, dx,
$$
where $F(x) = \prod_{m=1}^{\infty} (1 - x^m)^{-1} = \sum_{n=0}^{\infty} p(n) x^n$, and $C$ is a positively oriented closed curve surrounding $x = 0$ inside the unit disk.

Make the change of variable $x = e^{2\pi i \tau}$. As $x$ traverses a circle of radius $e^{-2\pi}$ counterclockwise about $0$, the point $\tau$ varies from $i$ to $i+1$ along a horizontal segment. Replace this segment by the Rademacher path $P(N)$. Then
$$
p(n) = \int_{P(N)} F(e^{2\pi i \tau}) e^{-2\pi i n \tau} \, d\tau.
$$

Decompose $P(N)$ into arcs of Ford circles:
$$
\int_{P(N)} = \sum_{k=1}^{N} \sum_{\substack{0 \leq h < k \\ (h,k)=1}} \int_{\gamma(h,k)},
$$
where $\gamma(h,k)$ is the upper arc of $C(h,k)$.

Apply the change of variable $z = -ik^2(\tau - h/k)$, so $\tau = h/k + iz/k^2$. Theorem 5.8 shows this maps $C(h,k)$ onto $K$ (radius $1/2$, center $z = 1/2$), and $\gamma(h,k)$ maps onto an arc joining $z_1(h,k)$ and $z_2(h,k)$. Hence
$$
p(n) = \sum_{h,k} i k^{-2} e^{-2\pi i nh/k} \int_{z_1}^{z_2} e^{2n\pi z/k^2} F\!\left(\exp\!\left(\frac{2\pi i h}{k} - \frac{2\pi z}{k^2}\right)\right) dz.
$$

Apply the transformation formula for $F$ (Theorem 5.1):
$$
F(x) = \omega(h,k) \left(\frac{z}{k}\right)^{1/2} \exp\!\left(\frac{\pi}{12z} - \frac{\pi z}{12k^2}\right) F(x'),
$$
where $x = \exp(2\pi i h/k - 2\pi z/k^2)$, $x' = \exp(2\pi i H/k - 2\pi/z)$, $\omega(h,k) = e^{\pi i s(h,k)}$, and $hH \equiv -1 \pmod{k}$.

Write $F(x') = 1 + (F(x') - 1)$ to split the integral:
$$
p(n) = \sum_{h,k} i k^{-5/2} \omega(h,k) e^{-2\pi i nh/k} (I_1 + I_2),
$$
where
$$
I_1 = \int_{z_1}^{z_2} z^{1/2} \exp\!\left(\frac{\pi}{12z} + \frac{2\pi z}{k^2}\left(n - \frac{1}{24}\right)\right) dz,
$$
and $I_2$ involves the remainder $F(x') - 1$.

Using Theorem 5.9, we estimate the modulus of the integrand in $I_2$: on the chord joining $z_1$ and $z_2$, $|z| < \sqrt{2}k/N$, and the path length is $< 2\sqrt{2}k/N$. This yields $|I_2(h,k)| < C k^{3/2} N^{-3/2}$, and summing over $h,k$ gives an error $O(N^{-1/2})$.

Replace the arc from $z_1$ to $z_2$ by the full circle $K(-)$ (negatively oriented), plus two short arcs $J_1$, $J_2$. The estimates of Theorem 5.9 show $|J_1|$, $|J_2| = O(N^{-1/2})$. Letting $N \to \infty$, we obtain
$$
p(n) = i \sum_{k=1}^{\infty} A_k(n) k^{-5/2} \int_{K(-)} z^{1/2} \exp\!\left(\frac{\pi}{12z} + \frac{2\pi z}{k^2}\left(n - \frac{1}{24}\right)\right) dz,
$$
where
$$
A_k(n) = \sum_{\substack{0 \leq h < k \\ (h,k)=1}} e^{\pi i s(h,k) - 2\pi i nh/k}.
$$

The change of variable $w = 1/z$ transforms the integral to
$$
p(n) = \frac{1}{i} \sum_{k=1}^{\infty} A_k(n) k^{-5/2} \int_{1-i\infty}^{1+i\infty} w^{-5/2} \exp\!\left(\frac{\pi w}{12} + \frac{2\pi}{k^2}\left(n - \frac{1}{24}\right)\frac{1}{w}\right) dw.
$$

Setting $t = \pi w/12$ expresses the integral as a Bessel function $I_{3/2}$. Using the formula for Bessel functions of half-odd order,
$$
I_{3/2}(z) = \sqrt{\frac{2z}{\pi}} \frac{d}{dz}\!\left(\frac{\sinh z}{z}\right),
$$
we finally obtain Rademacher's convergent series:
$$
p(n) = \frac{1}{\pi \sqrt{2}} \sum_{k=1}^{\infty} A_k(n) \, k^{1/2} \, \frac{d}{dn} \left( \frac{\sinh \left\{ \frac{\pi}{k} \sqrt{\frac{2}{3} \left(n - \frac{1}{24}\right)} \right\}}{\sqrt{n - \frac{1}{24}}} \right).
$$
