---
role: exercise
locale: en
chapter: "V"
section: "21"
exercise_number: 9
---

Show that the limit distribution
$$F(x) = 1 - \frac{4}{\pi} \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} e^{-\frac{\pi^2}{8}(2n+1)^2 x}$$
in P21.5, T23.2, and T23.3 has the Laplace transform
$$\int_0^\infty e^{-sx} \, dF(x) = \frac{\pi}{2} \sum_{n=0}^{\infty} (-1)^n \frac{2n+1}{s + \frac{\pi^2}{8}(2n+1)^2} = (\cosh \sqrt{2s})^{-1}$$
$$= 2 e^{-\sqrt{2s}} \sum_{k=0}^{\infty} (-1)^k e^{-2k\sqrt{2s}}.$$

Inverting the last series (term by term) show that the density of $F$ is
$$f(x) = \frac{dF}{dx} = \sqrt{\frac{2}{\pi}} \sum_{n=0}^{\infty} (-1)^n \frac{2n+1}{x^{3/2}} e^{-\frac{(2n+1)^2}{2x}},$$
which converges fast for small (positive) $x$, while
$$f(x) = \frac{\pi}{2} \sum_{n=0}^{\infty} (-1)^n (2n+1) e^{-\frac{\pi^2}{8}(2n+1)^2 x}$$
converges rapidly for large $x$.
