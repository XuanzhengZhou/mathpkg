---
role: proof
locale: en
of_concept: uniform-limit-of-holomorphic-functions
source_book: gtm038
source_chapter: "I"
source_section: "3. The Cauchy Integral"
---
**Proof.** Let $\mathfrak{z}_0 \in B$. Again, we assume that $\mathfrak{z}_0 = 0$. Let $P$ be a polycylinder about $\mathfrak{z}_0$ with $\bar{P} \subset B$. Let $\mathfrak{z} = (z_1, \ldots, z_n) \in P$. $N(\xi) := (\xi_1 - z_1) \cdot \ldots \cdot (\xi_n - z_n)$ is continuous and $\neq 0$ on $T$; therefore, $1/N(\xi)$ is also continuous on $T$ and there exists an $M \in \mathbb{R}$ such that $|1/N(\xi)| < M$ on $T$. $(f_\nu)$ converges uniformly on $T$ to $f$ so for every $\varepsilon > 0$ there exists a $\nu_0 = \nu_0(\varepsilon)$ such that $|f_\nu - f| < \varepsilon/M$ on all of $T$ for $\nu \geq \nu_0$. But then

$$\left| \left(\frac{1}{2\pi i}\right)^n \int_T \frac{f_\nu(\xi) - f(\xi)}{(\xi_1 - z_1) \cdots (\xi_n - z_n)} d\xi \right| < \varepsilon$$

for all $\nu \geq \nu_0$. Hence $\operatorname{ch}(f_\nu|T)$ converges uniformly to $\operatorname{ch}(f|T)$ on $P$. Since each $f_\nu|P = \operatorname{ch}(f_\nu|T)$ by Theorem 3.1, we have $f|P = \operatorname{ch}(f|T)$, which shows $f$ is holomorphic. $\square$
