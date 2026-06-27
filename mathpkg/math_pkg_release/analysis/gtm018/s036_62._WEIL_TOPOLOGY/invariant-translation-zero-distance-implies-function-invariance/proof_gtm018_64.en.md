---
role: proof
locale: en
of_concept: invariant-translation-zero-distance-implies-function-invariance
source_book: gtm018
source_chapter: "64"
source_section: "Weil Topology"
---

**Theorem C.** If $E$ is any set of finite measure in $\mathbf{T}$, then

$$0 = \rho(yE, E) = \int |\chi_{yE}(x) - \chi_E(x)| d\mu(x) = \int |\chi_E(y^{-1}x) - \chi_E(x)| d\mu(x).$$

It follows that

$$\int |g(y^{-1}x) - g(x)| d\mu(x) = 0$$

for every integrable simple function $g$ which is measurable $(\mathbf{T})$, and hence, by approximation, that $\int |f(y^{-1}x) - f(x)| d\mu(x) = 0$ for any $f \in \mathcal{L}$ measurable $(\mathbf{T})$.

Since the integrand of the last written integral belongs to $\mathcal{L}_+$, the desired conclusion $f(y^{-1}x) = f(x)$ for every $x \in X$ follows from 55.B (which states that a nonnegative integrable function with zero integral vanishes almost everywhere). $\blacksquare$
