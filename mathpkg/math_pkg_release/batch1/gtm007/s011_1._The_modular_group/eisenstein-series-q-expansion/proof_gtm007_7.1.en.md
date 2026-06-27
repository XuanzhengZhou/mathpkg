---
role: proof
locale: en
of_concept: eisenstein-series-q-expansion
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

Start from the well-known formula
$$\pi \cot \pi z = \frac{1}{z} + \sum_{m=1}^{\infty} \left( \frac{1}{z+m} + \frac{1}{z-m} \right).$$
Writing $\pi \cot \pi z = i\pi (q+1)/(q-1) = i\pi - 2i\pi \sum_{n=0}^{\infty} q^n$, we obtain
$$\frac{1}{z} + \sum_{m=1}^{\infty} \left( \frac{1}{z+m} + \frac{1}{z-m} \right) = i\pi - 2i\pi \sum_{n=0}^{\infty} q^n.$$

Differentiating both sides $(k-1)$ times (valid for $k \geq 2$) yields
$$\sum_{m \in \mathbf{Z}} \frac{1}{(m+z)^k} = \frac{1}{(k-1)!} (-2i\pi)^k \sum_{n=1}^{\infty} n^{k-1} q^n.$$

Now write $G_k(z)$ by separating the sum over $m$:
$$G_k(z) = \sum_{m,n} {}' \frac{1}{(mz+n)^{2k}} = \sum_{n \neq 0} \frac{1}{n^{2k}} + \sum_{m \neq 0} \sum_{n \in \mathbf{Z}} \frac{1}{(mz+n)^{2k}}$$
$$= 2\zeta(2k) + \sum_{m=1}^{\infty} \sum_{n \in \mathbf{Z}} \frac{1}{(mz+n)^{2k}} + \sum_{m=1}^{\infty} \sum_{n \in \mathbf{Z}} \frac{1}{(-mz+n)^{2k}}.$$

Applying the differentiated cotangent formula to each inner sum (with $z$ replaced by $mz$) and using $(-1)^{2k} = 1$, we get
$$G_k(z) = 2\zeta(2k) + 2\frac{(2i\pi)^{2k}}{(2k-1)!} \sum_{m=1}^{\infty} \sum_{d=1}^{\infty} d^{2k-1} q^{md}.$$

Collecting terms with $q^n$ (where $n = md$) gives the coefficient $\sum_{d \mid n} d^{2k-1} = \sigma_{2k-1}(n)$. The formula for $\gamma_k$ follows from the value $\zeta(2k) = 2^{2k-1} B_k \pi^{2k}/(2k)!$.
