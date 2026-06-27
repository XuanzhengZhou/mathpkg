---
role: proof
locale: en
of_concept: zeta-even-values-bernoulli
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

From the definition of the Bernoulli numbers via $x/(e^x-1)$, substituting $x = 2iz$ yields
$$z \cot z = 1 - \sum_{k=1}^{\infty} B_k \frac{2^{2k} z^{2k}}{(2k)!}.$$

On the other hand, taking the logarithmic derivative of the infinite product
$$\sin z = z \prod_{n=1}^{\infty} \left(1 - \frac{z^2}{n^2 \pi^2}\right)$$
gives
$$z \cot z = 1 - 2 \sum_{n=1}^{\infty} \sum_{k=1}^{\infty} \left(\frac{z^2}{n^2 \pi^2}\right)^k = 1 - 2 \sum_{k=1}^{\infty} \frac{\zeta(2k)}{\pi^{2k}} z^{2k}.$$

Comparing the coefficients of $z^{2k}$ in the two expressions:
$$\frac{B_k 2^{2k}}{(2k)!} = \frac{2\zeta(2k)}{\pi^{2k}},$$
which gives
$$\zeta(2k) = \frac{2^{2k-1}}{(2k)!} B_k \pi^{2k}.$$
