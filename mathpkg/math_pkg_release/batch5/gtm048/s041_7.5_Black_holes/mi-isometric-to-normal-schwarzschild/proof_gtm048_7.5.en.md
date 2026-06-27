---
role: proof
locale: en
of_concept: mi-isometric-to-normal-schwarzschild
source_book: gtm048
source_chapter: "7"
source_section: "7.5"
---

Let $t = 2\mu[\ln u - \ln(-v)]|_{M_I}$. Then $t$ is $C^\infty$ and maps $M_I$ onto $(-\infty, \infty)$. Let $\psi: M_I \to (-\infty, \infty) \times (2\mu, \infty) \times \mathcal{S}^2$ be given by $\psi(n) = (t(n), r(n), P(n))$ for every $n \in M_I$. The map $\psi$ is onto and there is a $C^\infty$ inverse determined by
$$u = (r - 2\mu) \exp\left(\frac{r - 2\mu + t}{4\mu}\right), \qquad v = (r - 2\mu) \exp\left(\frac{r - 2\mu - t}{4\mu}\right).$$

Thus $\psi$ is a diffeomorphism. Moreover, on $M_I$ we have
$$dt = 2\mu\left(\frac{dv}{v} - \frac{du}{u}\right), \qquad dr = 2\mu\left(1 - \frac{2\mu}{r}\right)\left(\frac{dv}{v} + \frac{du}{u}\right).$$

A direct computation using the metric on $K$ then yields
$$g|_{M_I} = -\left(1 - \frac{2\mu}{r}\right) dt \otimes dt + \left(1 - \frac{2\mu}{r}\right)^{-1} dr \otimes dr + r^2 h,$$
where $h$ is the standard metric on $\mathcal{S}^2$. This is precisely the normal Schwarzschild metric of active mass $8\pi\mu$, establishing the isometry.
