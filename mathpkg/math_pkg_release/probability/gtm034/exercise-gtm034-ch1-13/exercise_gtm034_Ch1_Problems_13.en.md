---
role: exercise
locale: en
chapter: "1"
section: "Problems"
exercise_number: 13
---

13. Suppose that $\mathbf{X}_1, \mathbf{X}_2, \ldots$, are independent real valued random variables (not integer valued!) with common distribution

$$F(y) = \mathbf{P}[\mathbf{X}_k \leq y], \quad -\infty < y < \infty.$$

Show, by replacing all Fourier series in the unit circle by Fourier transforms in the upper half plane, that every result of Chapter IV remains correct, with obvious modifications.

Now suppose in addition that $F(y)$ is continuous and symmetric, i.e., $F(y) = 1 - F(-y)$ for all real $y$. If

$$\phi(\theta) = \int_{-\infty}^{\infty} e^{i\theta y} dF(y), \quad -\infty < \theta < \infty,$$

show that

(a) $$1 - t\phi(\theta) = |1 - \mathbf{E}[t^T e^{i\theta Z}]|^2, \quad 0 \leq t < 1,$$

(b) $$\mathbf{P}[\mathbf{T} = k] = (-1)^{k+1} \binom{1/2}{k}, \quad k \geq 1,$$

(c) $$\mathbf{P}[\mathbf{N}_k = 0] = (-1)^k \binom{-1/2}{k}, \quad k \geq 0,$$

(d) $$\sum_{n=0}^{\infty} \mathbf{E}[e^{i\theta(2\mathbf{N}_n-n)}] t^n = |1 - e^{i\theta t}|^{-1}$$

$$= \frac{1}{\sqrt{1 + t^2 - 2t \cos \theta}}, \quad 0 \leq t < 1,$$

so that

(e) $$\mathbf{E}[e^{i\theta(2\mathbf{N

so that the arc-sine law yields a well-known theorem concerning the asymptotic behavior of Legendre polynomials:

$$\lim_{n \to \infty} P_n \left[ \cos \left( \frac{\theta}{n} \right) \right] = J_0(\theta), \quad -\infty < \theta < \infty.$$
