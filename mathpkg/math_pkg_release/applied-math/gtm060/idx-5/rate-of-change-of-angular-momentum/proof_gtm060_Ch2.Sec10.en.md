---
role: proof
locale: en
of_concept: rate-of-change-of-angular-momentum
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

**Proof.** Differentiating the total angular momentum:
$$\frac{d\mathbf{M}}{dt} = \sum_{i=1}^{n} [\dot{\mathbf{r}}_i, m_i \dot{\mathbf{r}}_i] + \sum_{i=1}^{n} [\mathbf{r}_i, m_i \ddot{\mathbf{r}}_i] = 0 + \sum_{i=1}^{n} [\mathbf{r}_i, \mathbf{F}_i].$$

Now decompose the forces into internal and external: $\mathbf{F}_i = \sum_{j \neq i} \mathbf{F}_{ij} + \mathbf{F}'_i$. The sum over internal forces vanishes:
$$\sum_{i=1}^{n} \left[\mathbf{r}_i, \sum_{j \neq i} \mathbf{F}_{ij}\right] = 0,$$
because $\mathbf{F}_{ij} = -\mathbf{F}_{ji}$ implies $[\mathbf{r}_i, \mathbf{F}_{ij}] + [\mathbf{r}_j, \mathbf{F}_{ji}] = [\mathbf{r}_i - \mathbf{r}_j, \mathbf{F}_{ij}] = 0$. Thus
$$\frac{d\mathbf{M}}{dt} = \sum_{i=1}^{n} [\mathbf{r}_i, \mathbf{F}'_i] = \mathbf{N}.$$
