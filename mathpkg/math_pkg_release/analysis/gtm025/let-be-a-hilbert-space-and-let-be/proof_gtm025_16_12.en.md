---
role: proof
locale: en
of_concept: "let-be-a-hilbert-space-and-let-be"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.12"
---

For $n > m$, it is plain that

$$\left\| \sum_{k=1}^{n} z_k - \sum_{k=1}^{m} z_k \right\|^2 = \left\| \sum_{k=m+1}^{n} z_k \right\|^2 = \sum_{k=1}^{n} \|z_k\|^2 - \sum_{k=1}^{m} \|z_k\|^2.$$

Thus $\left(\sum_{k=1}^{n} z_k\right)_{n=1}^{\infty}$ is a Cauchy sequence in $H$ if and only if $\left(\sum_{k=1}^{n} \|z_k\|^2\right)_{n=1}^{\infty}$ is a Cauchy sequence in $R$. This proves our first assertion.

Now suppose that $\sum_{k=1}^{n} z_k = z$. Writing $s_n = \sum_{k=1}^{n} z_k$, we have $\|z - s_n\| \to 0

In the real Hilbert space $R^3$ [3-dimensional Euclidean space], the vectors $(1, 0, 0), (0, 1, 0)$, and $(0, 0, 1)$ form an orthonormal set, and the Fourier coefficient of a vector $x$ with respect to each of these unit vectors is simply the length of the perpendicular projection of $x$ in the direction determined by that unit vector.

The following example motivates the use of the term "Fourier coefficient" in (16.14).

**(16.15) Example.** Consider the space $\mathfrak{L}_2\left([-\pi, \pi], \mathcal{M}_\lambda, \frac{1}{2\pi} \lambda\right)$. In this space, the inner product is

$$\langle f, g \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) \overline{g(t)} dt$$

for $f, g \in \mathfrak{L}_2$. For $n \in Z$, the functions $\chi_n: t \rightarrow \exp(int)$ are defined and continuous on $R$, and so are in $\mathfrak{L}_2\left([-\pi, \pi]\right)$. We will show that these functions form an orthonormal set. For each $n \in Z$, we have $\|\chi_n\|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |\chi_n(t)|^2 dt = \frac{1}{2\pi} \int_{-\pi}^{1} dt = 1$. If $m \neq n$ in $Z$, we have $\langle \chi_m, \chi_n \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} \chi_m(t) \overline{\chi_n(t)} dt = \frac{1}{2\pi} \int_{-\pi}^{\pi} \exp(i(m-n)t) dt + \frac{i}{2\pi} \int_{-\pi}^{\pi} \sin((m-n)t) dt = 0$. [Use elementary calculus to evaluate these integrals.] Hence $\{\chi_n\}_n = -

Proof. We have

$$\left\| x - \sum_{k=1}^{n} \alpha_k z_k \right\|^2 = \|x\|^2 - \sum_{k=1}^{n} \bar{\alpha}_k \langle x, z_k \rangle - \sum_{k=1}^{n} \alpha_k \langle z_k, x \rangle + \sum_{k=1}^{n} |\alpha_k|^2$$

$$= \|x\|^2 + \sum_{k=1}^{n} \left[ |\langle x, z_k \rangle|^2 - \bar{\alpha}_k \langle x, z_k \rangle - \alpha_k \overline{\langle x, z_k \rangle} + |\alpha_k|^2 \right] - \sum_{k=1}^{n} |\langle x, z_k \rangle|^2$$

$$= \|x\|^2 + \sum_{k=1}^{n} |\langle x, z_k \rangle - \alpha_k|^2 - \sum_{k=1}^{n} |\langle x, z_k \rangle|^2.$$

Hence $f(\alpha_1, \ldots, \alpha_n)$ is a minimum if and only if $\alpha_k = \langle x, z_k \rangle$, $k = 1, \ldots, n$; and in this case we see that

$$0 \leq \|x\|^2 - \sum_{k=1}^{n} |\langle x, z_k \rangle|^2.$$
