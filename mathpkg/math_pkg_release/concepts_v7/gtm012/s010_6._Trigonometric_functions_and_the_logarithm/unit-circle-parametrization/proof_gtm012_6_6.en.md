---
role: proof
locale: en
of_concept: unit-circle-parametrization
source_book: gtm012
source_chapter: "6"
source_section: "6. Trigonometric functions and the logarithm"
---

# Proof of Parametrization of the Unit Circle by Sine and Cosine

**Theorem 6.3.** Let $\gamma: [0, 2\pi] \to \mathbb{R}^2$ be defined by

$$\gamma(t) = (\cos t, \sin t).$$

Then $\gamma$ is a one-to-one mapping of $[0, 2\pi)$ onto the unit circle about the origin in $\mathbb{R}^2$. The length of the arc of this circle from $\gamma(0)$ to $\gamma(t)$ is $t$. In particular, the circumference of the unit circle is $2\pi$.

*Proof.* We know from Theorem 6.2 that $(\cos t)^2 + (\sin t)^2 = 1$, so $(\cos t, \sin t)$ lies on the unit circle for every $t$.

The discussion in the proof of Theorem 6.2 shows that on the interval $[0, \frac{1}{2}\pi]$, $\cos t$ decreases strictly from $1$ to $0$ while $\sin t$ increases strictly from $0$ to $1$. Therefore, $\gamma$ maps $[0, \frac{1}{2}\pi]$ into the portion of the circle lying in the quadrant $x \geq 0, y \geq 0$ in a one-to-one manner. Furthermore, suppose $0 \leq x \leq 1$, $0 \leq y \leq 1$, and $x^2 + y^2 = 1$. By the Intermediate Value Theorem applied to $\cos t$, there is a unique $t \in [0, \frac{1}{2}\pi]$ such that $\cos t = x$; then by $x^2 + y^2 = 1$ and $\sin^2 t + \cos^2 t = 1$, we have $\sin t = y$ (both nonnegative). Hence $\gamma$ maps $[0, \frac{1}{2}\pi]$ onto the first-quadrant arc of the unit circle.

Similar arguments using the shift relations $S(x + p) = C(x)$ and $C(x + p) = -S(x)$ from the proof of Theorem 6.2 extend this to the remaining three quadrants. Specifically, $\gamma$ maps $[\frac{1}{2}\pi, \pi]$ onto the second quadrant, $[\pi, \frac{3}{2}\pi]$ onto the third quadrant, and $[\frac{3}{2}\pi, 2\pi]$ onto the fourth quadrant, each in a one-to-one manner, and $\gamma(2\pi) = \gamma(0) = (1, 0)$. Thus $\gamma$ is a one-to-one mapping of $[0, 2\pi)$ onto the whole unit circle.

For the arc length, consider a partition $0 = t_0 < t_1 < \cdots < t_n = t$ of $[0, t]$. The length of the polygonal approximation is

$$\sum_{i=1}^{n} \sqrt{(\cos t_i - \cos t_{i-1})^2 + (\sin t_i - \sin t_{i-1})^2}.$$

By the Mean Value Theorem, there exist $t_i', t_i'' \in (t_{i-1}, t_i)$ such that

$$\cos t_i - \cos t_{i-1} = -\sin(t_i') (t_i - t_{i-1}), \qquad \sin t_i - \sin t_{i-1} = \cos(t_i'') (t_i - t_{i-1}).$$

Since sine and cosine are uniformly continuous on $[0, t]$, the difference between using $t_i'$ and $t_i''$ tends to zero as the mesh size tends to zero. Hence the sum approximates

$$\sum_{i=1}^{n} \sqrt{(\sin t_i')^2 + (\cos t_i')^2} \, (t_i - t_{i-1}).$$

Since $(\sin t)^2 + (\cos t)^2 = 1$, this sum simplifies to

$$\sum_{i=1}^{n} (t_i - t_{i-1}) = t.$$

Taking the limit as the maximum length $|t_i - t_{i-1}| \to 0$, the polygonal approximations converge to the arc length $t$. Therefore the length of the arc from $\gamma(0)$ to $\gamma(t)$ is exactly $t$. Setting $t = 2\pi$ gives the circumference of the unit circle as $2\pi$. $\square$
