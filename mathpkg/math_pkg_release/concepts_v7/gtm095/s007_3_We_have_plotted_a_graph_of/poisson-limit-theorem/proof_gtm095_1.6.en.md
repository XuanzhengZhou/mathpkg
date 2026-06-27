---
role: proof
locale: en
of_concept: poisson-limit-theorem
source_book: gtm095
source_chapter: "1"
source_section: "6. De Moivre–Laplace Limit Theorem"
---

# Proof of Poisson Limit Theorem

**Poisson's Theorem.** Let $p = p(n) \to 0$ as $n \to \infty$, in such a way that $np(n) \to \lambda$, where $\lambda > 0$. Then for each $k = 0, 1, 2, \ldots$,

$$P_n(k) \to \pi_k, \quad n \to \infty,$$

where

$$\pi_k = \frac{e^{-\lambda} \lambda^k}{k!}.$$

**Proof.** Write

$$P_n(k) = C_n^k p^k q^{n-k}$$

where $q = 1-p$. Since $np(n) \to \lambda$, we have $p = \frac{\lambda}{n} + o\left(\frac{1}{n}\right)$ and $q = 1 - \frac{\lambda}{n} + o\left(\frac{1}{n}\right)$. Substituting,

$$P_n(k) = \frac{n(n-1) \cdots (n-k+1)}{k!} \left[ \frac{\lambda}{n} + o\left(\frac{1}{n}\right) \right]^k \cdot \left[ 1 - \frac{\lambda}{n} + o\left(\frac{1}{n}\right) \right]^{n-k}.$$

For the first factor, rewrite

$$n(n-1) \cdots (n-k+1) \left[ \frac{\lambda}{n} + o\left(\frac{1}{n}\right) \right]^k = \frac{n(n-1) \cdots (n-k+1)}{n^k} \left[ \lambda + o(1) \right]^k.$$

As $n \to \infty$, the ratio $\frac{n(n-1) \cdots (n-k+1)}{n^k} \to 1$ (since $k$ is fixed), and $[\lambda + o(1)]^k \to \lambda^k$. Hence this factor converges to $\lambda^k$.

For the second factor,

$$\left[ 1 - \frac{\lambda}{n} + o\left(\frac{1}{n}\right) \right]^{n-k} \to e^{-\lambda}, \quad n \to \infty,$$

using the well-known limit $(1 - \lambda/n)^n \to e^{-\lambda}$.

Combining the limits,

$$P_n(k) \to \frac{\lambda^k}{k!} \cdot e^{-\lambda} = \pi_k,$$

which establishes the theorem. $\square$

The set of numbers $\{\pi_k, k = 0, 1, \ldots\}$ defines the Poisson probability distribution. Note that $\pi_k \geq 0$ and $\sum_{k=0}^{\infty} \pi_k = e^{-\lambda} \sum_{k=0}^{\infty} \lambda^k / k! = e^{-\lambda} e^{\lambda} = 1$. This is the first example encountered of a discrete probability distribution concentrated on a countably infinite set of points.
