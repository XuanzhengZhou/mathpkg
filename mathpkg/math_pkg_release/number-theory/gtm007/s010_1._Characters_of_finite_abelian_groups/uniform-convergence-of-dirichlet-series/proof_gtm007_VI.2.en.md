---
role: proof
locale: en
of_concept: uniform-convergence-of-dirichlet-series
source_book: gtm007
source_chapter: "VI"
source_section: "§2"
---

After making a translation on $z$, we can suppose that $z_0 = 0$. The hypothesis then means that the series $\sum a_n$ is convergent. We must prove uniform convergence in every domain $\Re(z) \geq 0$, $|z|/\Re(z) \leq k$.

Let $\varepsilon > 0$. Since $\sum a_n$ converges, there exists $N$ such that for $m, m' \geq N$, $|A_{m,m'}| \leq \varepsilon$, where $A_{m,p} = \sum_{n=m}^{p} a_n$. Applying Abel's lemma (Lemma 2) with $b_n = e^{-\lambda_n z}$, we obtain
$$S_{m,m'} = \sum_{n=m}^{m'-1} A_{m,n} (e^{-\lambda_n z} - e^{-\lambda_{n+1} z}) + A_{m,m'} e^{-\lambda_{m'} z}.$$

Let $z = x + iy$ with $x = \Re(z)$. By Lemma 3, $|e^{-\lambda_n z} - e^{-\lambda_{n+1} z}| \leq \frac{|z|}{x} (e^{-\lambda_n x} - e^{-\lambda_{n+1} x})$. Therefore
$$|S_{m,m'}| \leq \varepsilon \left(1 + \frac{|z|}{x} \sum_{n=m}^{m'-1} (e^{-\lambda_n x} - e^{-\lambda_{n+1} x})\right) \leq \varepsilon(1 + k(e^{-\lambda_m x} - e^{-\lambda_{m'} x})) \leq \varepsilon(1+k),$$
which proves uniform convergence in the specified domain.
