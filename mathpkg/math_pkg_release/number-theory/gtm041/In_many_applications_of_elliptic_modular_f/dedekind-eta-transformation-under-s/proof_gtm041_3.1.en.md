---
role: proof
locale: en
of_concept: dedekind-eta-transformation-under-s
source_book: gtm041
source_chapter: "3"
source_section: "3.1"
---

**Siegel's proof of Theorem 3.1.** First we prove the formula for $\tau = iy$, where $y > 0$, and then extend the result to all $\tau$ in $H$ by analytic continuation.

If $\tau = iy$, the transformation formula becomes
$$\eta(i/y) = y^{1/2} \eta(iy),$$
and this is equivalent to
$$\log \eta(i/y) - \log \eta(iy) = \frac{1}{2} \log y.$$

Now
$$\log \eta(iy) = -\frac{\pi y}{12} + \log \prod_{n=1}^{\infty} \left( 1 - e^{-2\pi ny} \right)$$
$$= -\frac{\pi y}{12} + \sum_{n=1}^{\infty} \log \left( 1 - e^{-2\pi ny} \right) = -\frac{\pi y}{12} - \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{e^{-2\pi m n y}}{m}.$$

Define $F_n(z)$ for $z$ in the complex plane with $N = n + \frac{1}{2}$. Let $C$ be the parallelogram joining the vertices $y, i, -y, -i$ in that order. Inside $C$, $F_n$ has simple poles at $z = ik/N$ and at $z = ky/N$ for $k = \pm 1, \pm 2, \ldots, \pm n$. There is also a triple pole at $z = 0$ with residue $i(y - y^{-1})/24$.

The residue at $z = ik/N$ is
$$\frac{1}{8\pi k} \cot \frac{\pi i k}{y}.$$

Since this is an even function of $k$, we have
$$\sum_{k=-n}^{n} \operatorname{Res}_{z=ik/N} F_n(z) = 2 \sum_{k=1}^{n} \frac{1}{8\pi k} \cot \frac{\pi i k}{y}.$$

But
$$\cot i\theta = \frac{\cos i\theta}{\sin i\theta} = i \frac{e^{-\theta} + e^{\theta}}{e^{-\theta} - e^{\theta}} = -i \frac{e^{2\theta} + 1}{e^{2\theta} - 1} = \frac{1}{i} \left(1 - \frac{2}{1 - e^{2\theta}}\right).$$

Using this with $\theta = \pi k / y$, we obtain
$$\sum_{k=-n}^{n} \operatorname{Res}_{z=ik/N} F_n(z) = \frac{1}{4\pi i} \sum_{k=1}^{n} \frac{1}{k} - \frac{1}{2\pi i} \sum_{k=1}^{n} \frac{1}{k} \frac{1}{1 - e^{2\pi k / y}}.$$

Similarly,
$$\sum_{k=-n}^{n} \operatorname{Res}_{z=ky/N} F_n(z) = \frac{i}{4\pi} \sum_{k=1}^{n} \frac{1}{k} - \frac{i}{2\pi} \sum_{k=1}^{n} \frac{1}{k} \frac{1}{1 - e^{2\pi k y}}.$$

[The proof continues by applying the residue theorem to the contour integral and taking the limit as $n \to \infty$, ultimately establishing the transformation formula for $\tau = iy$, then extending to all $\tau \in H$ by analytic continuation.]
