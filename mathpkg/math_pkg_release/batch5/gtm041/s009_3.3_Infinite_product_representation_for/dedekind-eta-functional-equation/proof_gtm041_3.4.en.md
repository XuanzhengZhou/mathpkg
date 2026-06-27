---
role: proof
locale: en
of_concept: dedekind-eta-functional-equation
source_book: gtm041
source_chapter: "3"
source_section: "3.4"
---

Dedekind's formula is a consequence of the following equation, obtained by taking logarithms of both members of (10),

$$\log \eta\!\left( \frac{a\tau + b}{c\tau + d} \right) = \log \eta(\tau) + \pi i \left( \frac{a + d}{12c} + s(-d, c) \right) + \frac{1}{2} \log\{-i(c\tau + d)\}.$$

From the definition of $\eta(\tau)$ as an infinite product we have

$$\log \eta(\tau) = \frac{\pi i \tau}{12} + \sum_{n=1}^{\infty} \log(1 - e^{2\pi in\tau}) = \frac{\pi i \tau}{12} - \sum_{n=1}^{\infty} \lambda(-in\tau),$$

where $\lambda(z)$ is defined in terms of the exponential integral. The proof of Theorem 3.4 proceeds through a sequence of lemmas, the key ingredient being Iseki's transformation formula (Lemma 2 in Section 3.5), which provides the necessary functional equation for the series $\sum \lambda(-in\tau)$. The complete deduction of Theorem 3.4 from Iseki's formula is carried out in Section 3.6.
