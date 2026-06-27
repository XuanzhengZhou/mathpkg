---
role: proof
locale: en
of_concept: fourier-transform-gauss-sum-property
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

**Proof of Theorem 1.2.**

For any $x \in \mathbb{Z}/n\mathbb{Z}$, consider the Fourier transform:
$$(T\chi)(x) = \sum_{a \in \mathbb{Z}/n\mathbb{Z}} \chi(a) \zeta^{ax}.$$

When $\gcd(x, n) = 1$, we make the change of variable $a \mapsto a x^{-1}$ (since $x$ is invertible modulo $n$):
$$(T\chi)(x) = \sum_{a \in \mathbb{Z}/n\mathbb{Z}} \chi(a x^{-1}) \zeta^{a} = \chi(x^{-1}) \sum_{a \in \mathbb{Z}/n\mathbb{Z}} \chi(a) \zeta^{a} = \overline{\chi(x)} \, \tau(\chi),$$
since $\chi(x^{-1}) = \overline{\chi(x)}$ for the unitary character $\chi$.

When $\gcd(x, n) > 1$, the fact that $\chi$ is primitive implies that $(T\chi)(x) = 0$ by Theorem 1.1. The formula still holds since $\overline{\chi(x)}$ is interpreted as $0$ when $x$ is not prime to $n$, consistent with the convention that characters on the non-invertible elements vanish.

For the absolute value, compute the squared modulus using the first relation:
$$|\tau(\chi)|^2 = \tau(\chi) \overline{\tau(\chi)} = \sum_{x} |(T\chi)(x)|^2 = \sum_{x} |\chi(x)|^2 |\tau(\chi)|^2 \cdot \frac{1}{n}.$$

Alternatively, using the Fourier inversion formula and the orthogonality of characters on $\mathbb{Z}/n\mathbb{Z}$:
$$\sum_{x \in \mathbb{Z}/n\mathbb{Z}} |(T\chi)(x)|^2 = \sum_{x} \sum_{a,b} \chi(a) \overline{\chi(b)} \zeta^{x(a-b)} = n \sum_{a} |\chi(a)|^2 = n \cdot \varphi(n).$$

But from $(T\chi)(x) = \tau(\chi) \overline{\chi(x)}$ for primitive $\chi$, we also have:
$$\sum_{x} |(T\chi)(x)|^2 = |\tau(\chi)|^2 \sum_{x \in (\mathbb{Z}/n\mathbb{Z})^\times} 1 = |\tau(\chi)|^2 \varphi(n).$$

Comparing the two expressions yields $|\tau(\chi)|^2 = n$, completing the proof.
