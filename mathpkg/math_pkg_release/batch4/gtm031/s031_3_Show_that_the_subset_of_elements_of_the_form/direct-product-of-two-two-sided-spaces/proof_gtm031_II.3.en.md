---
role: proof
locale: en
of_concept: direct-product-of-two-two-sided-spaces
source_book: gtm031
source_chapter: "II"
source_section: "3"
---

Let $\mathfrak{R}$ and $\mathfrak{S}$ be two-sided vector spaces over $\Delta$. Using formula (9), define a left scalar multiplication on $\mathfrak{P} = \mathfrak{R} \times \mathfrak{S}$ by

$$\alpha\left(\sum x_i \times y_i\right) = \sum \alpha x_i \times y_i$$

for $\alpha \in \Delta$, where the multiplication on the right side uses the left scalar multiplication in $\mathfrak{R}$. Using formula (10), define a right scalar multiplication on $\mathfrak{P}$ by

$$\left(\sum x_i \times y_i\right) \alpha = \sum x_i \times y_i \alpha$$

for $\alpha \in \Delta$, where the multiplication on the right side uses the right scalar multiplication in $\mathfrak{S}$.

We must verify that these left and right multiplications commute. Since $\mathfrak{R}$ is two-sided, the mapping $x \to \alpha x$ (left multiplication by $\alpha$) is a linear transformation in $\mathfrak{R}$ regarded as a right vector space. This is precisely condition (8) for a two-sided vector space. Consequently, for any left multiplication $\alpha$ and right multiplication $\beta$ on $\mathfrak{P}$,

$$\alpha\left(\left(\sum x_i \times y_i\right)\beta\right) = \alpha\left(\sum x_i \times y_i\beta\right) = \sum \alpha x_i \times y_i\beta$$

and

$$\left(\alpha\left(\sum x_i \times y_i\right)\right)\beta = \left(\sum \alpha x_i \times y_i\right)\beta = \sum \alpha x_i \times y_i\beta.$$

The equality holds because the left and right multiplications act on different components and do not interfere. More precisely, the commutation follows from the fact that left multiplication in $\mathfrak{R}$ is a linear transformation in the right space $\mathfrak{R}$. Hence $\mathfrak{P}$ satisfies the defining property of a two-sided vector space.
