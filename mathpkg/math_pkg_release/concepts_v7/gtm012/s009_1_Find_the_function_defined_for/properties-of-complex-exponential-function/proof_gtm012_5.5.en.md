---
role: proof
locale: en
of_concept: properties-of-complex-exponential-function
source_book: gtm012
source_chapter: "5"
source_section: "5"
---

# Proof of Properties of the Complex Exponential Function

**Theorem 5.5.** For any complex numbers $z, w \in \mathbb{C}$, the complex exponential function

$$E(z) = e^z = \sum_{n=0}^{\infty} \frac{z^n}{n!}$$

satisfies:

(a) $E(z + w) = E(z) E(w)$ for all $z, w \in \mathbb{C}$.

(b) $E(z^*) = E(z)^*$, where $z^*$ denotes the complex conjugate of $z$.

**Proof.** (a) The power series defining $E(z)$ converges absolutely for all $z \in \mathbb{C}$ (by the ratio test). Therefore the Cauchy product formula is valid:

$$E(z) E(w) = \left( \sum_{n=0}^{\infty} \frac{z^n}{n!} \right) \left( \sum_{m=0}^{\infty} \frac{w^m}{m!} \right) = \sum_{k=0}^{\infty} \sum_{j=0}^{k} \frac{z^j}{j!} \frac{w^{k-j}}{(k-j)!}.$$

Multiplying numerator and denominator by $k!$,

$$\sum_{j=0}^{k} \frac{z^j}{j!} \frac{w^{k-j}}{(k-j)!} = \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} z^j w^{k-j} = \frac{(z + w)^k}{k!},$$

where we used the binomial theorem. Hence

$$E(z) E(w) = \sum_{k=0}^{\infty} \frac{(z + w)^k}{k!} = E(z + w).$$

(b) Since the coefficients $1/n!$ of the power series are real, taking the complex conjugate termwise yields

$$E(z)^* = \left( \sum_{n=0}^{\infty} \frac{z^n}{n!} \right)^* = \sum_{n=0}^{\infty} \frac{(z^n)^*}{n!} = \sum_{n=0}^{\infty} \frac{(z^*)^n}{n!} = E(z^*).$$

The interchange of conjugation and summation is justified by the absolute convergence of the series. $\square$
