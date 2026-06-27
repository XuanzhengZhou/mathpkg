---
role: proof
locale: en
of_concept: levy-khinchin-stable-representation
source_book: gtm095
source_chapter: "3"
source_section: "§6. Infinitely divisible and stable distributions"
---

# Lévy–Khinchin Representation of Stable Distributions (Proof Omitted)

The textbook (GTM 095, Probability-1, 3rd ed., A.N. Shiryaev) states this theorem without proof:

> We quote without proof a theorem on the general form of the characteristic functions of stable distributions.

**Theorem.** A random variable $T$ is stable if and only if its characteristic function $\varphi(t)$ has the form $\varphi(t) = \exp \psi(t)$, where

$$\psi(t) = i t \beta - d |t|^\alpha \left(1 + i \theta \frac{t}{|t|} G(t, \alpha)\right),$$

with $0 < \alpha \leq 2$, $\beta \in \mathbb{R}$, $d \geq 0$, $|\theta| \leq 1$, $t/|t| = 0$ for $t = 0$, and

$$G(t, \alpha) = \begin{cases}
\tan \frac{1}{2} \pi \alpha, & \text{if } \alpha \neq 1, \\[4pt]
\frac{2}{\pi} \log |t|, & \text{if } \alpha = 1.
\end{cases}$$

The parameter $\alpha$ is called the **index of stability** (or characteristic exponent), $\beta$ is a shift parameter, $d$ is a scale parameter, and $\theta$ is a skewness parameter.

**Symmetric stable distributions.** When $\beta = 0$ and $\theta = 0$, the characteristic function simplifies to

$$\varphi(t) = e^{-d |t|^\alpha}, \quad 0 < \alpha \leq 2, \; d \geq 0.$$

The proof follows from the Kolmogorov–Lévy–Khinchin representation for infinitely divisible distributions by imposing the additional stability condition $[\varphi(t)]^n = \varphi(a_n t) e^{i b_n t}$. Standard references include:

- B.V. Gnedenko and A.N. Kolmogorov, *Limit Distributions for Sums of Independent Random Variables*, Addison-Wesley, 1954.
- V.M. Zolotarev, *One-Dimensional Stable Distributions*, AMS, 1986.
