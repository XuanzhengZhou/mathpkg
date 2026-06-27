---
role: proof
locale: en
of_concept: poisson-jensen-formula
source_book: gtm011
source_chapter: "XI"
source_section: "1"
---

The proof parallels that of Jensen's Formula but substitutes the Poisson integral formula (Corollary X.2.9) for the Mean Value Property. As before, construct

$$
F(z) = f(z) \prod_{k=1}^{n} \frac{r^2 - \bar{a}_k z}{r(z-a_k)},
$$

which is analytic in an open set containing $\bar{B}(0; r)$, has no zeros in $B(0; r)$, and satisfies $|F(z)| = |f(z)|$ for $|z| = r$. Since $F$ has no zeros in $\bar{B}(0; r)$, $\log |F(z)|$ is harmonic there. By Corollary X.2.9 (the Poisson integral formula for the disk),

$$
\log |F(z)| = \frac{1}{2\pi} \int_{0}^{2\pi} \frac{r^2 - |z|^2}{|re^{i\theta} - z|^2} \log |F(re^{i\theta})| \, d\theta
$$

for $|z| < r$. Since $|F(re^{i\theta})| = |f(re^{i\theta})|$, the integral is the same as that in the formula. Expanding $\log |F(z)|$ using the definition of $F$ yields

$$
\log |f(z)| - \sum_{k=1}^{n} \log \left| \frac{r(z-a_k)}{r^2 - \bar{a}_k z} \right| = \frac{1}{2\pi} \int_{0}^{2\pi} \frac{r^2 - |z|^2}{|re^{i\theta} - z|^2} \log |f(re^{i\theta})| \, d\theta,
$$

which is the Poisson-Jensen Formula.
