---
role: proof
locale: en
of_concept: properties-of-complex-trigonometric-exponential
source_book: gtm012
source_chapter: "6"
source_section: "6. Trigonometric functions and the logarithm"
---

# Proof of Properties of Complex Trigonometric and Exponential Functions

**Theorem 6.4.** The sine, cosine, and exponential functions have the following properties:

(a) $\exp(iz) = \cos z + i \sin z$ for all $z \in \mathbb{C}$.

(b) $\sin(z + 2\pi) = \sin z$, $\cos(z + 2\pi) = \cos z$, and $\exp(z + 2\pi i) = \exp z$ for all $z \in \mathbb{C}$.

(c) If $w \in \mathbb{C}$ and $w \neq 0$, there exists $z \in \mathbb{C}$ such that $w = \exp(z)$. If also $w = \exp(z')$, then there is an integer $n$ such that $z' = z + 2n\pi i$.

*Proof.* (a) The identity follows from solving the defining equations (6.5) and (6.6) for $\exp(iz)$. Recall

$$\sin z = \frac{1}{2i}(e^{iz} - e^{-iz}), \qquad \cos z = \frac{1}{2}(e^{iz} + e^{-iz}).$$

Adding $i \sin z$ to $\cos z$ gives

$$\cos z + i \sin z = \frac{1}{2}(e^{iz} + e^{-iz}) + i \cdot \frac{1}{2i}(e^{iz} - e^{-iz}) = \frac{1}{2}(e^{iz} + e^{-iz}) + \frac{1}{2}(e^{iz} - e^{-iz}) = e^{iz} = \exp(iz).$$

(b) By Theorem 6.2 and the definition of $\pi$ (where $\pi = 2p$ with $p$ the smallest positive zero of $C$), we have

$$\exp(2\pi i) = \exp(i \cdot 2\pi) = \cos 2\pi + i \sin 2\pi.$$

Since $C(2\pi) = C(4p) = C(0) = 1$ and $S(2\pi) = S(4p) = S(0) = 0$ by the periodicity proved in Theorem 6.2(d), we obtain

$$\exp(2\pi i) = 1 + i \cdot 0 = 1.$$

Then since $\exp(z + w) = \exp z \exp w$ (by the basic property of the exponential function),

$$\exp(z + 2\pi i) = \exp z \cdot \exp(2\pi i) = \exp z.$$

This identity together with the definitions (6.5) and (6.6) implies

$$\sin(z + 2\pi) = \frac{1}{2i}\big(e^{i(z+2\pi)} - e^{-i(z+2\pi)}\big) = \frac{1}{2i}\big(e^{iz} e^{2\pi i} - e^{-iz} e^{-2\pi i}\big) = \frac{1}{2i}(e^{iz} - e^{-iz}) = \sin z,$$

and similarly $\cos(z + 2\pi) = \cos z$.

(c) Suppose $w \in \mathbb{C}$, $w \neq 0$. Write $w$ in polar form: let $r = |w| > 0$ and let $\theta \in \mathbb{R}$ be such that $w/|w| = e^{i\theta}$ (such $\theta$ exists by Theorem 6.3, since $w/|w|$ lies on the unit circle and $\gamma$ maps $[0, 2\pi)$ onto the unit circle). Since the real exponential function $\exp: \mathbb{R} \to (0, \infty)$ is surjective, there exists $x = \log r \in \mathbb{R}$ such that $\exp(x) = r$. Set $z = x + i\theta$. Then

$$\exp(z) = \exp(x + i\theta) = \exp(x) \exp(i\theta) = r \cdot \frac{w}{r} = w.$$

This proves existence.

For uniqueness modulo $2\pi i$, suppose $\exp(z) = \exp(z') = w$. Write $z = x + iy$ and $z' = x' + iy'$ with $x, x', y, y' \in \mathbb{R}$. Since

$$|\exp(z)| = |\exp(x + iy)| = e^x |e^{iy}| = e^x,$$
$$|\exp(z')| = e^{x'},$$

and both equal $|w|$, we have $e^x = e^{x'}$, so $x = x'$ (the real exponential is injective). Now

$$\exp(iy) = \frac{w}{e^x} = \frac{w}{e^{x'}} = \exp(iy'),$$

so $\exp(i(y' - y)) = 1$. Let $h = y' - y$. By Theorem 6.3, the map $t \mapsto (\cos t, \sin t)$ is one-to-one on $[0, 2\pi)$ with image the full unit circle, and $\cos t + i \sin t = e^{it} = 1$ only at $t = 0$ in $[0, 2\pi)$. Writing $h = 2n\pi + h_0$ with $n \in \mathbb{Z}$ and $h_0 \in [0, 2\pi)$, we have

$$\exp(ih) = \exp(i(2n\pi + h_0)) = \exp(2n\pi i) \exp(ih_0) = \exp(ih_0).$$

Since $\exp(ih) = 1$, this gives $\exp(ih_0) = 1$. But for $h_0 \in [0, 2\pi)$, $\exp(ih_0) = 1$ implies $h_0 = 0$. Hence $y' = y + 2n\pi$, and therefore $z' = z + 2n\pi i$. $\square$
