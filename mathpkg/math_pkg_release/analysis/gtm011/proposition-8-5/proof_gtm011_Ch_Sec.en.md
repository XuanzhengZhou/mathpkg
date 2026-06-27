---
role: proof
locale: en
of_concept: proposition-8-5
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. According to the above corollary this integral is an analytic function in the region $\{z : \text{Re } z > 1\}$. Thus, it suffices to show that $\zeta(z) \Gamma(z)$ equals this integral for $z = x > 1$.

From Lemma 8.3 there are numbers $\alpha$ and $\beta$, $0 < \alpha < \beta < \infty$, such that:

$$\int_0^\alpha (e^t - 1)^{-1} t^{x-1} dt < \frac{\epsilon}{4},$$

$$\int_\beta^\infty (e^t - 1)^{-1} t^{x-1} dt < \frac{\epsilon}{4}.$$

Since

$$\sum_{k=1}^n e^{-kt} \leq \sum_{k=1}^{\infty} e^{-kt} = (e^t - 1)^{-1}$$

for all $n \geq 1$,

$$\sum_{n=1}^{\infty} \int_0^\alpha e^{-nt} t^{x-1} dt < \frac{\epsilon}{4},$$

$$\sum_{n=1}^{\infty} \int_\beta^\infty e^{-nt} t^{x-1} dt < \frac{\epsilon}{4}.$$

Using equation (

But $\sum e^{-nt}$ converges to $(e^t - 1)^{-1}$ uniformly on $[\alpha, \beta]$, so that the right hand side is exactly $\epsilon$.

We wish to use Proposition 8.5 to extend the domain of definition of $\zeta$ to $\{z: \text{Re } z > -1\}$ (and eventually to all $\mathbb{C}$). To do this, consider the Laurent expansion of $(e^z - 1)^{-1}$; this is

$$\frac{1}{e^z - 1} = \frac{1}{z} - \frac{1}{2} + \sum_{n=1}^{\infty} a_n z^n$$

for some constants $a_1, a_2, \ldots$. Thus $[(e^t - 1)^{-1} - t^{-1}]$ remains bounded in a neighborhood of $t = 0$. But this implies that the integral

$$\int_0^1 \left( \frac{1}{e^t - 1} - \frac{1}{t} \right) t^{z-1} dt$$

converges uniformly on compact subsets of the right half plane $\{z: \text{Re } z > 0\}$ and therefore represents an analytic function there. Hence

$$\zeta(z) \Gamma(z) = \int_0^1 \left( \frac{1}{e^t - 1} - \frac{1}{t} \right) t^{z-1} dt + (z-1)^{-1} + \int_1^{\infty} \frac{t^{z-1}}{e^t - 1} dt,$$

and (using Corollary 8.4(b)) each of these summands, except $(z-1)^{-1}$, is analytic in the right half plane. Thus one may define $\zeta(z)$ for $\text{Re } z > 0$ by setting it equal to $[\Gamma(z)]^{-1}$ times the right hand side of (8.7). In this manner $\zeta$ is meromorphic in the right half plane with a simple pole at $z = 1 \left( \sum n^{-1} \text{diverges} \right)$

there is a constant $c'$ such that

$$\left( \frac{1}{t} - \frac{1}{e^t - 1} \right) \leq \frac{c'}{t}, \quad t \geq 1.$$

This gives that the integral

$$\int_1^\infty \left( \frac{1}{e^t - 1} - \frac{1}{t} \right) t^{z-1} dt$$

converges uniformly on compact subsets of $\{z: \text{Re } z < 1\}$. Using these last two integrals with equation (8.8) gives

$$\zeta(z)\Gamma(z) = \int_0^1 \left( \frac{1}{e^t - 1} - \frac{1}{t} + \frac{1}{2} \right) t^{z-1} dt - \frac{1}{2z} + \int_1^\infty \left( \frac{1}{e^t - 1} - \frac{1}{t} \right) t^{z-1} dt$$

for $0 < \text{Re } z < 1$. But since both integrals converge in the strip $-1 < \text{Re } z < 1$ (8.9) can be used to define $\zeta(z)$ in $\{z: -1 < \text{Re } z < 1\}$. What happens at $z = 0$? Since the term $(2z)^{-1}$ appears on the right hand side of (8.9) will $\zeta$ have a pole at $z = 0$? The answer is no. To define $\zeta(z)$ we must divide (8.9) by $\Gamma(z)$. When this happens the term in question becomes $[2z\Gamma(z)]^{-1} = [2\Gamma(z+1)]^{-1}$ which is analytic at $z = 0$. Thus, if $\zeta$ is so defined in the strip $\{z: -1 < \text{Re } z < 1\}$ it is analytic there. If this is combined with (8.7), $\zeta(z)$ is defined for $\text{Re } z > -1$ with a

Applying this to (8.10) gives

8.11 $$\zeta(z)\Gamma(z) = 2 \int_0^\infty \left( \sum_{n=1}^{\infty} \frac{1}{t^2 + 4n^2\pi^2} \right) t^z dt$$

$$= 2 \sum_{n=1}^{\infty} \int_0^\infty \frac{t^z}{t^2 + 4n^2\pi^2} dt$$

$$= 2 \sum_{n=1}^{\infty} (2\pi n)^{z-1} \int_0^\infty \frac{t^z}{t^2 + 1} dt$$

$$= 2(2\pi)^{z-1} \zeta(1-z) \int_0^\infty \frac{t^z}{t^2 + 1} dt,$$

for $-1 < \text{Re } z < 0$. (It is left to the reader to justify the interchanging of the sum and the integral.) Now for $x$ a real number with $-1 < x < 0$, the change of variable $s = t^2$ gives (by Example V. 2.12)

8.12 $$\int_0^\infty \frac{t^x}{t^2 + 1} dt = \frac{1}{2} \int_0^\infty \frac{s^{\frac{1}{2}(x-1)}}{s+1} ds$$

$$= \frac{1}{2} \pi \text{cosec} \left[ \frac{1}{2}\pi(1-x) \right]$$

$$= \frac{1}{2} \pi \text{sec} \left( \frac{1}{2}\pi x \right).$$

But Exercise 7.2 gives

$$\frac{1}{\Gamma(x)} = \frac{\Gamma(1-x)}{\pi} \sin \pi x = \frac{\Gamma(1-x)}{\pi} \left[ 2 \sin \left( \frac{1}{2}\pi x \right) \cos \left( \frac{1}{2}\pi x \right) \right]$$

Combining this with (
