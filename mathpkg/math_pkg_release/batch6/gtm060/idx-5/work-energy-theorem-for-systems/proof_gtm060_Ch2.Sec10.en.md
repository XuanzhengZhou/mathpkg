---
role: proof
locale: en
of_concept: work-energy-theorem-for-systems
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

**Proof.** Start from the definition of kinetic energy:
$$\frac{dT}{dt} = \sum_{i=1}^{n} m_i (\dot{\mathbf{r}}_i, \ddot{\mathbf{r}}_i) = \sum_{i=1}^{n} (\dot{\mathbf{r}}_i, m_i \ddot{\mathbf{r}}_i) = \sum_{i=1}^{n} (\dot{\mathbf{r}}_i, \mathbf{F}_i),$$
since $m_i \ddot{\mathbf{r}}_i = \mathbf{F}_i$. Integrating from $t_0$ to $t_1$ gives the integral form. In configuration space $E^{3n}$, with $\mathbf{r} = (\mathbf{r}_1, \ldots, \mathbf{r}_n)$ and $\mathbf{F} = (\mathbf{F}_1, \ldots, \mathbf{F}_n)$, this becomes
$$T(t_1) - T(t_0) = \int_{t_0}^{t_1} (\dot{\mathbf{r}}, \mathbf{F}) \, dt = \int_{\mathbf{r}(t_0)}^{\mathbf{r}(t_1)} (\mathbf{F}, d\mathbf{r}).$$
