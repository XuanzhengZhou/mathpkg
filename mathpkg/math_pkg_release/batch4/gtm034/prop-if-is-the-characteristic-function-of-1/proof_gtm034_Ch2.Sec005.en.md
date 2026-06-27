---
role: proof
locale: en
of_concept: prop-if-is-the-characteristic-function-of-1
source_book: gtm034
source_chapter: "2"
source_section: "005"
---

Proof: The random walk is transient, according to P1.4 if and only if

$$G = \sum_{n=0}^{\infty} P_n(0,0) < \infty.$$

But

$$G = \lim_{t \to 1} \sum_{n=0}^{\infty} t^n P_n(0,0),$$

whether this limit is finite or not. Using P6.3 we have

$$(2\pi)^d G = \lim_{t \to 1} \sum_{n=0}^{\infty} t^n \int \phi^n(\theta) d\theta = \lim_{t \to 1} \int \frac{d\theta}{1 - t\phi(\theta)}.$$

Observing that, for $0 \leq t < 1$,

$$\int \frac{d\theta}{1 - t\phi(\theta)} = \text{Re} \int \frac{d\theta}{1 - t\phi(\theta)} = \text{Re} \left[ \frac{1}{1 - t\phi(\theta)} \right] d\theta,$$

we find

$$(2\pi)^d G = \lim_{t \to 1} \int \text{Re} \left[ \frac{1}{1 - t\phi(\theta)} \right] d\theta,$$

which proves P1.

This criterion may be used to obtain simple sufficient conditions for recurrence or for transience. By analogy with T3.1, which states that one-dimensional random walk is rec
