---
role: proof
locale: en
of_concept: approximation-by-approximate-identity
source_book: gtm012
source_chapter: "3"
source_section: "3. Translation, convolution, and approximation"
---

# Proof of Theorem 3.6: Approximation of Continuous Functions by Convolution with an Approximate Identity

Recall that a sequence $(\varphi_n)_{n=1}^{\infty} \subset \mathcal{C}$ is an **approximate identity** if

1. $\varphi_n(x) \geq 0$ for all $n, x$;
2. $\frac{1}{2\pi} \int_0^{2\pi} \varphi_n(x) \, dx = 1$ for all $n$;
3. for each $0 < \delta < \pi$,
   $$\int_\delta^{2\pi - \delta} \varphi_n(x) \, dx \to 0 \quad \text{as} \quad n \to \infty.$$

**Theorem 3.6.** Suppose $(\varphi_n)_{n=1}^{\infty} \subset \mathcal{C}$ is an approximate identity. Then for each $u \in \mathcal{C}$,

$$|\varphi_n * u - u| \to 0 \quad \text{as} \quad n \to \infty.$$

Moreover, if $u \in \mathcal{P}$, then

$$\varphi_n * u \to u \quad (\mathcal{P}) \quad \text{as} \quad n \to \infty.$$

**Proof.** Since $\frac{1}{2\pi} \int_0^{2\pi} \varphi_n(y) \, dy = 1$ and $\varphi_n * u = u * \varphi_n$ (commutativity, Proposition 3.1(6)), we have

$$2\pi \left| (\varphi_n * u)(x) - u(x) \right| = \left| \int_0^{2\pi} [u(x - y) - u(x)] \varphi_n(y) \, dy \right|.$$

Given $\varepsilon > 0$, since $u$ is uniformly continuous, there exists $\delta > 0$ such that

$$|u(x - y) - u(x)| < \varepsilon \quad \text{whenever} \quad |y| < \delta \text{ or } |y - 2\pi| < \delta.$$

Split the integral into two regions: where $y$ is close to $0$ (and $2\pi$) and where it is not:

$$
\begin{aligned}
\left| \int_0^{2\pi} [u(x - y) - u(x)] \varphi_n(y) \, dy \right|
&\leq \int_{[0,\delta] \cup [2\pi-\delta, 2\pi]} |u(x - y) - u(x)| \varphi_n(y) \, dy \\
&\quad + \int_\delta^{2\pi - \delta} |u(x - y) - u(x)| \varphi_n(y) \, dy.
\end{aligned}
$$

The first integral is bounded by

$$\varepsilon \int_0^{2\pi} \varphi_n(y) \, dy = 2\pi \varepsilon,$$

using property (ii) of the approximate identity and the uniform continuity estimate.

For the second integral, since $|u(x - y) - u(x)| \leq 2|u|$, we have

$$\int_\delta^{2\pi - \delta} |u(x - y) - u(x)| \varphi_n(y) \, dy \leq 2|u| \int_\delta^{2\pi - \delta} \varphi_n(y) \, dy.$$

By property (iii) of the approximate identity, there exists $N$ such that for all $n \geq N$,

$$\int_\delta^{2\pi - \delta} \varphi_n(y) \, dy < \varepsilon.$$

Thus for $n \geq N$, the second integral is bounded by $2|u| \varepsilon$. Combining the estimates,

$$\left| (\varphi_n * u)(x) - u(x) \right| \leq \varepsilon + \frac{|u|}{\pi} \varepsilon = \varepsilon\left(1 + \frac{|u|}{\pi}\right)$$

for all $n \geq N$ and all $x$. Since $\varepsilon > 0$ was arbitrary, this proves

$$|\varphi_n * u - u| \to 0 \quad \text{as} \quad n \to \infty.$$

**Now suppose $u \in \mathcal{P}$.** For each $k$, using Proposition 3.4 (differentiation of convolution) and commutativity,

$$D^k(\varphi_n * u) = D^k(u * \varphi_n) = (D^k u) * \varphi_n = \varphi_n * (D^k u).$$

Since $D^k u \in \mathcal{C}$ (as $u \in \mathcal{P}$), the first part of the theorem applied to $D^k u$ shows that

$$|D^k(\varphi_n * u) - D^k u| = |\varphi_n * (D^k u) - D^k u| \to 0 \quad \text{as} \quad n \to \infty.$$

Thus each derivative $D^k(\varphi_n * u)$ converges uniformly to $D^k u$, which means precisely that

$$\varphi_n * u \to u \quad (\mathcal{P}) \quad \text{as} \quad n \to \infty.$$

$\square$
