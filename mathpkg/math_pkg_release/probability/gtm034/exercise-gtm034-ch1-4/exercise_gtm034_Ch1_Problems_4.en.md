---
role: exercise
locale: en
chapter: "1"
section: "Problems"
exercise_number: 4
---

4. When $\mu = 0, \sigma^2 < \infty$, show that

$$E[M_n] = \sum_{k=1}^{n} \frac{1}{k} E[S_k; S_k > 0] \sim \sum_{k=1}^{n} \frac{1}{2k} E[S_k] \sim \sqrt{\frac{2n}{\pi}} \sigma \text{ as } n \to \infty.$$

It is also known that

$$\lim_{n \to \infty} P[M_n \leq x E[M_n]] = \frac{2}{\sqrt{\pi}} \int_0^{\frac{\pi}{2}} e^{-t^2} dt, \quad x \geq 0.$$

This limit theorem (cf. Erdős and Kac [29] and Darling [19]) may be obtained from P19.1 with the aid of the Tauberian theorem in P20.2.
