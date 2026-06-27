---
role: proof
locale: en
of_concept: hecke-bound-cusp-forms
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

Because $f$ is a cusp form, we have $a_0 = 0$ and can factor $q$ out of the expansion:
$$f(z) = \sum_{n=1}^{\infty} a_n q^n = q \sum_{n=0}^{\infty} a_{n+1} q^n.$$
Hence $|f(z)| = O(|q|) = O(e^{-2\pi y})$ with $y = \operatorname{Im}(z)$, when $q \to 0$ (i.e. $y \to \infty$).

Let $\phi(z) = |f(z)| y^k$. Using formulas (1) and (2) — namely $\operatorname{Im}(gz) = \operatorname{Im}(z)/|cz+d|^2$ and $f(gz) = (cz+d)^{2k} f(z)$ — we verify that $\phi$ is invariant under the modular group $G$:
$$\phi(gz) = |f(gz)| (\operatorname{Im}(gz))^k = |cz+d|^{2k} |f(z)| \frac{y^k}{|cz+d|^{2k}} = |f(z)| y^k = \phi(z).$$

Moreover, $\phi$ is continuous on the fundamental domain $D$, and from the cusp estimate $|f(z)| = O(e^{-2\pi y})$, we have $\phi(z) = O(y^k e^{-2\pi y}) \to 0$ as $y \to \infty$. Hence $\phi$ is bounded on $D$, i.e. there exists $M > 0$ such that
$$|f(z)| \leq M y^{-k} \quad \text{for all } z \in H.$$

Now the Fourier coefficients are given by the contour integral
$$a_n = e^{2\pi n y} \int_0^1 f(x+iy) e^{-2\pi i n x} dx$$
for any fixed $y > 0$. Taking absolute values and using the bound $|f| \leq M y^{-k}$:
$$|a_n| \leq e^{2\pi n y} M y^{-k}.$$

This holds for every $y > 0$. Choosing $y = 1/n$ optimizes the estimate, giving $|a_n| \leq M e^{2\pi} n^k$. Thus $a_n = O(n^k)$.
