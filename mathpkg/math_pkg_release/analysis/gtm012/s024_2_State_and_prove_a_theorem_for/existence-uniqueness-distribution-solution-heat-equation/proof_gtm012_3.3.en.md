---
role: proof
locale: en
of_concept: existence-uniqueness-distribution-solution-heat-equation
source_book: gtm012
source_chapter: "3"
source_section: "The heat equation: distribution solutions"
---

# Proof of Existence and uniqueness of distribution solution to the heat equation (Theorem 3.1)

**Theorem 3.1.** For each $G \in \mathcal{P}'$ there is a unique family $(F_t)_{t > 0} \subset \mathcal{P}'$ such that

$$\frac{d}{dt} F_t \bigg|_{t=s} = D^2 F_s, \quad \text{all } s > 0, \tag{7}$$

$$F_t \rightarrow G (\mathcal{P}') \quad \text{as } t \rightarrow 0. \tag{8}$$

For each $t > 0$, $F_t$ is a function $u_t(x) = u(x, t)$ which is infinitely differentiable in both $x$ and $t$, and which satisfies the heat equation

$$\frac{\partial}{\partial t} u(x, t) = \left( \frac{\partial}{\partial x} \right)^2 u(x, t), \quad x \in \mathbb{R}, \quad t > 0,$$

in the classical sense.

**Proof.**

Let the Fourier coefficients of $F_t$ be denoted

$$a_n(t) = F_t(\chi_n), \quad \chi_n(x) = \exp(-inx), \quad n \in \mathbb{Z}.$$

Let $b_n = G(\chi_n)$ be the Fourier coefficients of the initial distribution $G$.

**Uniqueness.** From the definition of the distributional time derivative, condition (7) implies that for each fixed $n$,

$$\frac{d}{dt} a_n(t) = F_t(D^2 \chi_n) = F_t(-n^2 \chi_n) = -n^2 a_n(t).$$

This is an ordinary differential equation for $a_n(t)$ with general solution

$$a_n(t) = c_n \exp(-n^2 t).$$

Condition (8) implies that $a_n(t) \to b_n$ as $t \to 0$, so $c_n = b_n$ and

$$a_n(t) = b_n \exp(-n^2 t), \quad n \in \mathbb{Z}. \tag{11}$$

Thus the Fourier coefficients of $F_t$ are uniquely determined, so the distributions $F_t$ are uniquely determined.

**Existence.** We show that the sequence $(a_n(t))_{-\infty}^{\infty}$ defined by (11) is the sequence of Fourier coefficients of a smooth function for $t > 0$. Since $G \in \mathcal{P}'$, its Fourier coefficients satisfy

$$|b_n| \leq c |n|^k, \quad \text{all } n,$$

for some constants $c$ and $k$. For any $m \in \mathbb{N}$ and $t > 0$, using $e^{y} > (m!)^{-1} y^m$ for $y > 0$, we have

$$e^{-n^2 t} < m! (n^2 t)^{-m} = m! n^{-2m} t^{-m}.$$

Therefore

$$|a_n(t)| = |b_n| e^{-n^2 t} \leq c |n|^k \cdot m! n^{-2m} t^{-m} = c m! |n|^{k-2m} t^{-m}, \quad m = 0, 1, 2, \dots.$$

For any given $t > 0$, we can choose $m$ large enough so that $k - 2m < -1$, which shows $\sum |a_n(t)| < \infty$. It follows that for each $t > 0$, $(a_n(t))_{-\infty}^{\infty}$ is the sequence of Fourier coefficients of a function $u_t \in \mathcal{P}$.

Define the partial sums

$$u_N(x, t) = \sum_{n=-N}^{N} a_n(t) \exp(inx) = \sum_{n=-N}^{N} b_n \exp(inx - n^2 t).$$

Then $u_N(\cdot, t) \to u_t$ uniformly as $N \to \infty$ (by the uniform convergence of Fourier series for smooth periodic functions). Moreover, for any nonnegative integers $l, r$,

$$\left( \frac{\partial}{\partial t} \right)^l \left( \frac{\partial}{\partial x} \right)^r u_N(x, t) = \sum_{n=-N}^{N} b_n (-n^2)^l (in)^r \exp(inx - n^2 t) = \sum_{n=-N}^{N} a_{n,l,r}(t) \exp(inx),$$

where

$$|a_{n,l,r}(t)| = |b_n| n^{2l+r} e^{-n^2 t} \leq c m! |n|^{k+2l+r-2m} t^{-m}, \quad m = 0, 1, 2, \dots.$$

Again, for any fixed $t > 0$ and any fixed $l, r$, we may choose $m$ large enough so that the exponent $k+2l+r-2m < -1$, which implies the absolute convergence of the series of partial derivatives. It follows that each partial derivative of $u_N$ converges uniformly on $\mathbb{R} \times [\delta, \infty)$ for any $\delta > 0$ as $N \to \infty$. Therefore the limit function $u(x,t) = \lim_{N \to \infty} u_N(x,t)$ is infinitely differentiable in $x$ and $t$ for $t > 0$, and its partial derivatives are obtained by termwise differentiation.

**Verification of (8).** By Theorem 2.3, since $u_N \to u$ uniformly (and hence in $\mathcal{P}'$) as $N \to \infty$, and the Fourier coefficients of each $u_N$ converge to those of $G$ as $t \to 0$, we obtain $F_t \to G$ in $\mathcal{P}'$ as $t \to 0$.

**Verification of (7).** Each partial derivative of $u$ is bounded on the region $\{(x, t) : x \in \mathbb{R}, \, t \geq \delta > 0\}$ for any $\delta > 0$. It follows from this and the mean value theorem that

$$(t - s)^{-1}(u_t - u_s) \rightarrow \frac{\partial}{\partial t} u_s$$

uniformly as $t \to s > 0$. Therefore the distributional time derivative coincides with the classical partial derivative, and (7) holds. $\square$
