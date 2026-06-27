---
role: proof
locale: en
of_concept: lemma-3-fourier-expansion-reciprocal-powers
source_book: gtm041
source_chapter: "1"
source_section: "1.14"
---

Start with the partial fraction decomposition of the cotangent:

$$\pi \cot \pi\tau = \frac{1}{\tau} + \sum_{m=-\infty}^{+\infty} \left( \frac{1}{\tau+m} - \frac{1}{m} \right).$$

Let $x = e^{2\pi i\tau}$. If $\tau \in H$ then $|x| < 1$ and we find

$$\pi \cot \pi\tau = \pi \frac{\cos \pi\tau}{\sin \pi\tau} = \pi i \frac{e^{2\pi i\tau} + 1}{e^{2\pi i\tau} - 1} = \pi i \frac{x+1}{x-1} = -\pi i \left( \frac{x}{1-x} + \frac{1}{1-x} \right)$$

$$= -\pi i \left( \sum_{r=1}^{\infty} x^r + \sum_{r=0}^{\infty} x^r \right) = -\pi i \left( 1 + 2 \sum_{r=1}^{\infty} x^r \right).$$

On the other hand, from the partial fraction formula we also have

$$\pi \cot \pi\tau = \frac{1}{\tau} + \sum_{m=1}^{\infty} \frac{2\tau}{\tau^2 - m^2}.$$

Differentiating both expressions three times with respect to $\tau$ yields the expansion for $\sum (m+\tau)^{-4}$. Replacing $\tau$ by $n\tau$ gives the stated formula. Differentiating five times similarly yields the formula for $\sum (m+n\tau)^{-6}$. $\square$
