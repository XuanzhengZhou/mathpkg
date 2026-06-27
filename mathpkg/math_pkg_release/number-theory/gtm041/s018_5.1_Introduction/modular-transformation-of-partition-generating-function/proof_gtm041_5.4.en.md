---
role: proof
locale: en
of_concept: modular-transformation-of-partition-generating-function
source_book: gtm041
source_chapter: "5"
source_section: "5.4"
---

If $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma$ with $c > 0$, the functional equation for $\eta(\tau)$ implies

$$\frac{1}{\eta(\tau)} = \frac{1}{\eta(\tau')} \{-i(c\tau + d)\}^{1/2} \exp\left\{\pi i\left(\frac{a + d}{12c} + s(-d, c)\right)\right\},$$

where $\tau' = (a\tau + b)/(c\tau + d)$. Since $F(e^{2\pi i\tau}) = e^{\pi i\tau/12}/\eta(\tau)$, this implies

$$F(e^{2\pi i\tau}) = F(e^{2\pi i\tau'}) \exp\left(\frac{\pi i(\tau - \tau')}{12}\right) \{-i(c\tau + d)\}^{1/2} \exp\left\{\pi i\left(\frac{a + d}{12c} + s(-d, c)\right)\right\}.$$

Now choose

$$a = H,\quad c = k,\quad d = -h,\quad b = -\frac{hH + 1}{k},$$

and $\tau = \frac{iz + h}{k}$. Then

$$\tau' = \frac{iz^{-1} + H}{k},$$

and the transformation formula gives the behavior of $F$ near the root of unity $e^{2\pi ih/k}$ in terms of its value near the origin. For small $|z|$, writing $x = \exp(2\pi ih/k - 2\pi z/k)$, the function $F(x')$ is nearly $F(0) = 1$. Hence, aside from a constant factor, for small $|z|$,

$$F(x) \sim z^{1/2} \exp\left(\frac{\pi}{12z}\right).$$
