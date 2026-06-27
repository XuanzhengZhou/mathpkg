---
role: proof
locale: en
of_concept: jensens-formula
source_book: gtm011
source_chapter: "Entire Functions"
source_section: "1. Jensen's Formula"
---

If $|b| < 1$ then the map $(z-b)(1-\bar{b}z)^{-1}$ takes the disk $B(0; 1)$ onto itself and maps the boundary onto itself. Hence

$$\frac{r^2(z-a_k)}{r^2 - \bar{a}_k z}$$

maps $B(0; r)$ onto itself and takes the boundary to the boundary. Therefore

$$F(z) = f(z) \prod_{k=1}^{n} \frac{r^2 - \bar{a}_k z}{r(z-a_k)}$$

is analytic in an open set containing $\bar{B}(0; r)$, has no zeros in $B(0; r)$, and $|F(z)| = |f(z)|$ for $|z| = r$. So (1.1) applies to $F$ to give

$$\log |F(0)| = \frac{1}{2\pi} \int_{0}^{2\pi} \log |f(re^{i\theta})| d\theta.$$

However $F(0) = f(0) \prod_{k=1}^{n} \left( -\frac{r}{a_k} \right)$ so that Jensen's Formula results.
