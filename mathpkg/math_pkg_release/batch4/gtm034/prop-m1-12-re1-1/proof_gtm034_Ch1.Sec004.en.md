---
role: proof
locale: en
of_concept: prop-m1-12-re1-1
source_book: gtm034
source_chapter: "1"
source_section: "004"
---

Proof: The real part of the characteristic function is

$$\text{Re} \phi(\theta) = \sum P(0,x) \cos x\theta,$$

and therefore $\text{Re}[1 - \phi(\theta)] \geq 0$, and the integral in P6, whether finite or not, equals

$$\sum P(0,x) \frac{1}{2\pi} \int_{-\pi}^{\pi} \frac{1 - \cos x\theta}{1 - \cos \theta} d\theta$$

in the sense that this series diverges if and only if the integral in P6 is infinite. To complete the proof it suffices to verify that

$$\frac{1}{2\pi} \int_{-\pi}^{\pi} \frac{1 - \cos x\theta}{1 - \cos \theta} d\theta = |x|, \quad x \in R,$$

This is easily done by using the trigonometric identity

$$\frac{1 - \cos x\theta}{1 - \cos \theta} = \left( \frac{\sin \frac{x\theta}{2}}{\sin \frac{\theta}{2}} \right)^2 = \left| \sum_{k=1}^{|x|} e^{ik\theta} \right|^2, \quad x \in R.$$

For higher dimensional random

Note that while $m_1$ and $m_2$ are scalars, $\mu$ is of course a $d$-dimensional vector. $Q(\theta)$ is called the moment quadratic form of the random walk, for reasons which will promptly be discernible.

If $X = (X_1, \ldots, X_d)$ is a vector random variable such that $X = x$ with probability $P(0,x)$, then evidently

$$Q(\theta) = \sum_{i=1}^{d} \sum_{j=1}^{d} E[X_i X_j] \theta_i \theta_j$$

when the expected values $E[X_i X_j]$ all exist. But their existence is assured by the assumption that $m_2 = E|X|^2 < \infty$, as one can see from the Schwarz inequality

$$(\theta \cdot X)^2 \leq |\theta|^2 |X|^2.$$

This inequality implies that $Q(\theta) < \infty$ for all $\theta$, and the fact that

$$E[X_i X_j] \leq \{E[X_i^2] E[X_j^2]\}^{1/2} \leq E|X|^2$$

gives another way of seeing that the coefficients in the quadratic form $Q(\theta)$ are well defined.

To illustrate what kind of results can be obtained, we prove
