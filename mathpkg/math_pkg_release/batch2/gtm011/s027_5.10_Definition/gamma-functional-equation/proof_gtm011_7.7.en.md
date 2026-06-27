---
role: proof
locale: en
of_concept: gamma-functional-equation
source_book: gtm011
source_chapter: "7"
source_section: "7.7"
---

Substitute $z+1$ for $z$ in Gauss's formula (7.6):

$$\Gamma(z+1) = \lim_{n \to \infty} \frac{n! \, n^{z+1}}{(z+1)(z+2) \cdots (z+n+1)}.$$

Factor the expression:

$$\Gamma(z+1) = z \lim_{n \to \infty} \left[ \frac{n! \, n^z}{z(z+1) \cdots (z+n)} \right] \left[ \frac{n}{z+n+1} \right].$$

The first factor in brackets converges to $\Gamma(z)$ by Gauss's formula. The second factor satisfies $\lim_{n \to \infty} \frac{n}{z+n+1} = 1$. Therefore,

$$\Gamma(z+1) = z \Gamma(z).$$
