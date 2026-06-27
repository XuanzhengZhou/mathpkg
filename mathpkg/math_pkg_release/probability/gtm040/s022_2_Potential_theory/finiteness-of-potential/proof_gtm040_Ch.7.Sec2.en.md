---
role: proof
locale: en
of_concept: finiteness-of-potential
source_book: gtm040
source_chapter: "7"
source_section: "2"
---

It suffices to prove the lemma for the case where $\mu$ is a measure, since the general case follows by taking differences. Let $K_n$ denote the closed ball about the origin of radius $n$, and form

$$\int_{K_n} g(x) \, dx = \frac{1}{2\pi} \int_{K_n} \int_{\mathbb{R}^3} \frac{1}{|x - y|} \, d\mu(y) \, dx.$$

By Fubini's Theorem we may interchange the order of integration to get

$$\int_{K_n} g(x) \, dx = \frac{1}{2\pi} \int_{\mathbb{R}^3} \left[ \int_{K_n} \frac{1}{|x - y|} \, dx \right] d\mu(y).$$

The inside integral on the right is bounded by its value at the origin, which is some finite number $c$. Thus the right side does not exceed

$$\frac{1}{2\pi} c \, \mu(\mathbb{R}^3) < \infty,$$

and $g$ must be finite almost everywhere on $K_n$. Since the countable union of the sets $K_n$ is $\mathbb{R}^3$, we conclude that $g$ is finite almost everywhere on $\mathbb{R}^3$.
