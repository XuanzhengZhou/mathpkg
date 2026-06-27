---
role: proof
locale: en
of_concept: bernoulli-distribution-congruence
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

Write $c^{-1}x = b/N + y$ with some integer $z$. Since

$$B_k(X) = X^k - \frac{k}{2}X^{k-1} + \text{lower terms},$$

we find the following congruences modulo $\frac{N}{D(k)}\mathbf{Z}[c, 1/c]$:

$$N^{k-1}\left[B_k\left(\left\langle \frac{x}{N} \right\rangle\right) - c^k B_k\left(\left\langle \frac{c^{-1}x}{N} \right\rangle\right)\right]
\equiv N^{k-1}\left[\left(\frac{x}{N}\right)^k - \frac{k}{2}\left(\frac{x}{N}\right)^{k-1}\right]$$

$$- N^{k-1}c^k\left[\left(\frac{b}{N} + y - z\right)^k - \frac{k}{2}\left(\frac{b}{N} + y - z\right)^{k-1}\right]$$

$$\equiv \frac{x^k}{N} - \frac{k}{2}x^{k-1} - \frac{x^k}{N} + kx^{k-1}cz + c^k\frac{k}{2}b^{k-1}$$

$$\equiv kx^{k-1}\left(\frac{x}{N} - c\left\langle \frac{c^{-1}x}{N} \right\rangle + \frac{c-1}{2}\right) \equiv kx^{k-1}E_{1,c}^{(N)}(x).$$

Dividing by $k$ and using the definition of $E_{k,c}^{(N)}$, Property E2 follows from E1.
