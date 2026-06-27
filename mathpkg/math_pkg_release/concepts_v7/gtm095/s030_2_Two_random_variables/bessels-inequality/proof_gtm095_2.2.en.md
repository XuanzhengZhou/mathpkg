---
role: proof
locale: en
of_concept: bessels-inequality
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Bessel's Inequality for Orthonormal Systems

From the derivation of the best linear estimator, for any $\xi \in L^2$ and orthonormal system $\eta_1, \ldots, \eta_n$, we have

$$E \left| \xi - \sum_{i=1}^{n} (\xi, \eta_i) \eta_i \right|^2 = \|\xi\|^2 - \sum_{i=1}^{n} |(\xi, \eta_i)|^2 \geq 0.$$

Hence

$$\sum_{i=1}^{n} |(\xi, \eta_i)|^2 \leq \|\xi\|^2$$

for every finite $n$. Letting $n \to \infty$, we obtain Bessel's inequality:

$$\sum_{i=1}^{\infty} |(\xi, \eta_i)|^2 \leq \|\xi\|^2.$$

Equality is attained if and only if

$$\left\| \xi - \sum_{i=1}^{n} (\xi, \eta_i) \eta_i \right\| \to 0 \quad \text{as } n \to \infty,$$

i.e., if and only if

$$\xi = \lim_{n \to \infty} \sum_{i=1}^{n} (\xi, \eta_i) \eta_i$$

in the mean-square sense.
