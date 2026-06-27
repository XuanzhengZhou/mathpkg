---
role: proof
locale: en
of_concept: zeta-even-values
source_book: gtm007
source_chapter: "VII"
source_section: "§1. The modular group"
---

The formula follows from the computation of the Fourier expansion of $G_{2k}$:
$$
G_{2k}(z) = \sum_{(m,n) \neq (0,0)} \frac{1}{(mz+n)^{2k}} = 2\zeta(2k) + 2\frac{(2\pi i)^{2k}}{(2k-1)!} \sum_{n=1}^\infty \sigma_{2k-1}(n) q^n.
$$
On the other hand, the theory of Eisenstein series shows that the normalized form $E_{2k} = G_{2k}/(2\zeta(2k))$ has rational Fourier coefficients expressible in Bernoulli numbers, yielding Euler\'s formula.
