---
role: proof
locale: en
of_concept: weak-law-of-large-numbers
source_book: gtm017
source_chapter: "II"
source_section: "e"
---
Let $\sigma^2$ be the common variance. Then
$$P\left(\left|\frac{S_n}{n} - m\right| \geq \varepsilon\right) = P\left(\left|\sum_{i=1}^{n} (X_i - m)/n\right| \geq \varepsilon\right)$$
$$\leq E\left[\sum_{i=1}^{n} (X_i - m)/n\right]^2 / \varepsilon^2$$
$$= \frac{1}{n^2 \varepsilon^2} E\left(\sum_{i=1}^{n} (X_i - m)\right)^2 = \frac{\sigma^2}{n \varepsilon^2} \to 0$$
as $n \to \infty$, using Chebyshevs inequality and independence of $X_i$.
