---
role: proof
locale: en
of_concept: goursats-theorem
source_book: gtm011
source_chapter: "IV"
source_section: "8"
---

We need only show that $f'$ is continuous on each open disk contained in $G$; so we may assume $G$ is itself an open disk. By Morera's Theorem (5.10), it suffices to show that $\int_T f = 0$ for each triangular path $T$ in $G$.

Let $T = [a, b, c, a]$ and let $\Delta$ be the closed set formed by $T$ and its interior, so $T = \partial \Delta$. Using the midpoints of the sides of $\Delta$, form four triangles $\Delta_1, \Delta_2, \Delta_3, \Delta_4$ inside $\Delta$. Let $T^{(1)}$ be the triangle among these four for which $|\int_{T^{(1)}} f|$ is largest. Then

$$\left| \int_T f \right| \leq 4 \left| \int_{T^{(1)}} f \right|.$$

Repeat this process inductively to obtain a sequence $\{T^{(n)}\}$ of closed triangular paths such that, with $\Delta^{(n)}$ being the inside of $T^{(n)}$ together with $T^{(n)}$:

$$\Delta^{(1)} \supset \Delta^{(2)} \supset \cdots,$$
$$\left| \int_{T^{(n)}} f \right| \leq 4 \left| \int_{T^{(n+1)}} f \right|,$$
$$\ell(T^{(n+1)}) = \frac{1}{2} \ell(T^{(n)}),$$
$$\operatorname{diam} \Delta^{(n+1)} = \frac{1}{2} \operatorname{diam} \Delta^{(n)}.$$

These imply:
$$\left| \int_T f \right| \leq 4^n \left| \int_{T^{(n)}} f \right|,$$
$$\ell(T^{(n)}) = \left(\frac{1}{2}\right)^n \ell \quad \text{where } \ell = \ell(T),$$
$$\operatorname{diam} \Delta^{(n)} = \left(\frac{1}{2}\right)^n d \quad \text{where } d = \operatorname{diam} \Delta.$$

Since each $\Delta^{(n)}$ is closed, Cantor's Theorem gives $\bigcap_{n=1}^{\infty} \Delta^{(n)} = \{z_0\}$ for a single point $z_0$.

Let $\epsilon > 0$. Since $f$ has a derivative at $z_0$, there exists $\delta > 0$ such that $B(z_0; \delta) \subset G$ and

$$\left| \frac{f(z) - f(z_0)}{z - z_0} - f'(z_0) \right| < \epsilon$$

whenever $0 < |z - z_0| < \delta$. Equivalently,

$$|f(z) - f(z_0) - f'(z_0)(z - z_0)| \leq \epsilon |z - z_0|$$

for $|z - z_0| < \delta$.

Choose $n$ large enough so that $\operatorname{diam} \Delta^{(n)} < \delta$. Then for $z \in T^{(n)}$, $|z - z_0| \leq \operatorname{diam} \Delta^{(n)}$. Note that $\int_{T^{(n)}} [f(z_0) + f'(z_0)(z - z_0)] dz = 0$ since the integrand has a primitive. Hence

$$\left| \int_{T^{(n)}} f \right| = \left| \int_{T^{(n)}} [f(z) - f(z_0) - f'(z_0)(z - z_0)] dz \right|$$
$$\leq \epsilon \cdot \operatorname{diam} \Delta^{(n)} \cdot \ell(T^{(n)}) = \epsilon \cdot \left(\frac{1}{2}\right)^n d \cdot \left(\frac{1}{2}\right)^n \ell = \epsilon d \ell \left(\frac{1}{4}\right)^n.$$

Using $|\int_T f| \leq 4^n |\int_{T^{(n)}} f|$, we obtain

$$\left| \int_T f \right| \leq 4^n \cdot \epsilon d \ell \left(\frac{1}{4}\right)^n = \epsilon d \ell.$$

Since $\epsilon > 0$ was arbitrary and $d$ and $\ell$ are fixed, $\int_T f = 0$. By Morera's Theorem, $f$ is analytic.
