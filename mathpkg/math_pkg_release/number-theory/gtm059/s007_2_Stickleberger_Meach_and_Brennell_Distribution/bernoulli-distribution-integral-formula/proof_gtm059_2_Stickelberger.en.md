---
role: proof
locale: en
of_concept: bernoulli-distribution-integral-formula
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

We have

$$E_{1,c}^{(N)}(x) = \mathbf{B}_1\left( \left\langle \frac{x}{N} \right\rangle \right) - c \,\mathbf{B}_1\left( \left\langle \frac{c^{-1}x}{N} \right\rangle \right).$$

Recall that the first Bernoulli polynomial is $\mathbf{B}_1(X) = X - \frac{1}{2}$. Substituting this in yields

$$E_{1,c}^{(N)}(x) = \left\langle \frac{x}{N} \right\rangle - \frac{1}{2} - c\left( \left\langle \frac{c^{-1}x}{N} \right\rangle - \frac{1}{2} \right)
= \left\langle \frac{x}{N} \right\rangle - c\left\langle \frac{c^{-1}x}{N} \right\rangle + \frac{c-1}{2},$$

which is the desired formula.
