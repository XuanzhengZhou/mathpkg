---
role: proof
locale: en
of_concept: riemann-functional-equation
source_book: gtm011
source_chapter: "8"
source_section: "8.14"
---

The proof proceeds in several steps, extending the domain of definition of $\zeta$ progressively.

**Step 1: Extension to $\operatorname{Re} z > 0$.** Consider the Laurent expansion of $(e^z-1)^{-1}$:
$$\frac{1}{e^z-1} = \frac{1}{z} - \frac{1}{2} + \sum_{n=1}^{\infty} a_n z^n$$
for some constants $a_1, a_2, \ldots$. Thus $[(e^t-1)^{-1} - t^{-1}]$ remains bounded in a neighborhood of $t = 0$. This implies that the integral
$$\int_0^1 \left( \frac{1}{e^t-1} - \frac{1}{t} \right) t^{z-1} dt$$
converges uniformly on compact subsets of the right half plane $\{z: \operatorname{Re} z > 0\}$ and therefore represents an analytic function there. Hence, from Proposition 8.5,
$$\zeta(z) \Gamma(z) = \int_0^1 \left( \frac{1}{e^t-1} - \frac{1}{t} \right) t^{z-1} dt + \frac{1}{z-1} + \int_1^{\infty} \frac{t^{z-1}}{e^t-1} dt. \tag{8.7}$$
By Corollary 8.4(b), each summand except $(z-1)^{-1}$ is analytic in the right half plane. Thus one may define $\zeta(z)$ for $\operatorname{Re} z > 0$ by setting it equal to $[\Gamma(z)]^{-1}$ times the right hand side of (8.7). In this manner $\zeta$ is meromorphic in the right half plane with a simple pole at $z=1$.

**Step 2: Extension to $\operatorname{Re} z > -1$.** There is a constant $c'$ such that
$$\left( \frac{1}{t} - \frac{1}{e^t-1} \right) \leq \frac{c'}{t}, \quad t \geq 1.$$
This gives that the integral
$$\int_1^\infty \left( \frac{1}{e^t-1} - \frac{1}{t} \right) t^{z-1} dt$$
converges uniformly on compact subsets of $\{z: \operatorname{Re} z < 1\}$. Using these last two integrals with equation (8.8) gives
$$\zeta(z)\Gamma(z) = \int_0^1 \left( \frac{1}{e^t-1} - \frac{1}{t} + \frac{1}{2} \right) t^{z-1} dt - \frac{1}{2z} + \int_1^\infty \left( \frac{1}{e^t-1} - \frac{1}{t} \right) t^{z-1} dt \tag{8.9}$$
for $0 < \operatorname{Re} z < 1$. But since both integrals converge in the strip $-1 < \operatorname{Re} z < 1$, (8.9) can be used to define $\zeta(z)$ in $\{z: -1 < \operatorname{Re} z < 1\}$. At $z = 0$, dividing by $\Gamma(z)$ turns the term $(2z)^{-1}$ into $[2z\Gamma(z)]^{-1} = [2\Gamma(z+1)]^{-1}$, which is analytic at $z=0$. Thus $\zeta$ is analytic in the strip $\{-1 < \operatorname{Re} z < 1\}$. Combined with (8.7), $\zeta(z)$ is defined for $\operatorname{Re} z > -1$.

**Step 3: Derivation of the functional equation.** For $-1 < \operatorname{Re} z < 0$,
$$\zeta(z)\Gamma(z) = 2 \int_0^\infty \left( \sum_{n=1}^{\infty} \frac{1}{t^2 + 4n^2\pi^2} \right) t^z dt$$
$$= 2 \sum_{n=1}^{\infty} \int_0^\infty \frac{t^z}{t^2 + 4n^2\pi^2} dt$$
$$= 2 \sum_{n=1}^{\infty} (2\pi n)^{z-1} \int_0^\infty \frac{t^z}{t^2 + 1} dt$$
$$= 2(2\pi)^{z-1} \zeta(1-z) \int_0^\infty \frac{t^z}{t^2 + 1} dt. \tag{8.11}$$
For $x$ real with $-1 < x < 0$, the change of variable $s = t^2$ gives
$$\int_0^\infty \frac{t^x}{t^2 + 1} dt = \frac{1}{2} \int_0^\infty \frac{s^{\frac{1}{2}(x-1)}}{s+1} ds = \frac{1}{2} \pi \operatorname{cosec}\left[ \frac{1}{2}\pi(1-x) \right] = \frac{1}{2} \pi \sec\left( \frac{1}{2}\pi x \right). \tag{8.12}$$
Using the reflection formula for the Gamma function (Exercise 7.2):
$$\frac{1}{\Gamma(x)} = \frac{\Gamma(1-x)}{\pi} \sin \pi x = \frac{\Gamma(1-x)}{\pi} \left[ 2 \sin\left( \frac{1}{2}\pi x \right) \cos\left( \frac{1}{2}\pi x \right) \right],$$
and combining with (8.11) and (8.12) yields the functional equation. By analytic continuation this identity extends to all $z \neq 1$.

**Conclusion.** The functional equation and the fact that $\Gamma(1-z)$ has simple poles at $z=1,2,3,\ldots$ together imply that $\zeta$ is meromorphic on $\mathbb{C}$ with a single simple pole at $z=1$, and $\operatorname{Res}(\zeta; 1) = 1$.
