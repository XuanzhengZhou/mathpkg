---
role: proof
locale: en
of_concept: dedekind-eta-functional-equation
source_book: gtm041
source_chapter: "3"
source_section: "3.1-3.2"
---

**Proof (Siegel).** First we prove (4) for $\tau = iy$, where $y > 0$, and then extend the result to all $\tau$ in $H$ by analytic continuation.

If $\tau = iy$ the transformation formula becomes

$$\eta(i/y) = y^{1/2} \eta(iy),$$

and this is equivalent to

$$\log \eta(i/y) - \log \eta(iy) = \frac{1}{2} \log y.$$

Now

$$\log \eta(iy) = -\frac{\pi y}{12} + \log \prod_{n=1}^{\infty} (1 - e^{-2\pi ny})$$
$$= -\frac{\pi y}{12} + \sum_{n=1}^{\infty} \log(1 - e^{-2\pi ny}) = -\frac{\pi y}{12} - \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{e^{-2\pi mny}}{m}.$$

Therefore

$$\log \eta(i/y) - \log \eta(iy) = -\frac{\pi}{12} \left( \frac{1}{y} - y \right) - \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{1}{m} \left( e^{-2\pi mn/y} - e^{-2\pi mny} \right).$$

Hence we must prove that

$$-\frac{\pi}{12} \left( \frac{1}{y} - y \right) - \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{1}{m} \left( e^{-2\pi mn/y} - e^{-2\pi mny} \right) = \frac{1}{2} \log y. \tag{5}$$

Consider the function

$$F_n(z) = -\frac{1}{8\pi i z^3} \cot(\pi i N z) \cot\left( \frac{\pi N z}{y} \right),$$

where $N = n + \frac{1}{2}$. Let $C$ be the parallelogram joining the vertices $y, i, -y, -i$ in that order. Inside $C$, $F_n$ has simple poles at $z = ik/N$ and at $z = ky/N$ for $k = \pm 1, \pm 2, \ldots, \pm n$. There is also a triple pole at $z = 0$ with residue $i(y - y^{-1})/24$.

The residue at $z = ik/N$ is

$$\frac{1}{8\pi k} \cot \frac{\pi i k}{y}.$$

Since this is an even function of $k$ we have

$$\sum_{k=-n}^{n} \operatorname{Res}_{z=ik/N} F_n(z) = 2 \sum_{k=1}^{n} \frac{1}{8\pi k} \cot \frac{\pi i k}{y}.$$

But

$$\cot i\theta = \frac{\cos i\theta}{\sin i\theta} = i \frac{e^{-\theta} + e^{\theta}}{e^{-\theta} - e^{\theta}} = -i \frac{e^{2\theta} + 1}{e^{2\theta} - 1} = \frac{1}{i} \left(1 - \frac{2}{1 - e^{2\theta}}\right).$$

Using this with $\theta = \pi k/y$ we get

$$\sum_{k=-n}^{n} \operatorname{Res}_{z=ik/N} F_n(z) = \frac{1}{4\pi i} \sum_{k=1}^{n} \frac{1}{k} - \frac{1}{2\pi i} \sum_{k=1}^{n} \frac{1}{k} \frac{1}{1 - e^{2\pi k/y}}.$$

Similarly,

$$\sum_{k=-n}^{n} \operatorname{Res}_{z=ky/N} F_n(z) = \frac{i}{4\pi} \sum_{k=1}^{n} \frac{1}{k} - \frac{i}{2\pi} \sum_{k=1}^{n} \frac{1}{k} \frac{1}{1 - e^{2\pi ky}}.$$

By the residue theorem, the sum of all residues inside $C$ equals $\frac{1}{2\pi i} \int_C F_n(z) \, dz$. Letting $n \to \infty$, the integral over $C$ tends to $0$. Summing all residues and taking the limit, one obtains after simplification

$$-\frac{\pi}{12} \left( \frac{1}{y} - y \right) - \sum_{k=1}^{\infty} \sum_{m=1}^{\infty} \frac{1}{m} \left( e^{-2\pi mk/y} - e^{-2\pi mky} \right) = \frac{1}{2} \log y,$$

which is exactly equation (5). This proves $\eta(i/y) = y^{1/2} \eta(iy)$ for $y > 0$.

To extend to all $\tau \in H$, note that both sides of $\eta(-1/\tau) = (-i\tau)^{1/2} \eta(\tau)$ are analytic functions of $\tau$ on the simply connected domain $H$. Since they agree on the positive imaginary axis $\tau = iy$ ($y > 0$), they agree on all of $H$ by analytic continuation. $\square$
