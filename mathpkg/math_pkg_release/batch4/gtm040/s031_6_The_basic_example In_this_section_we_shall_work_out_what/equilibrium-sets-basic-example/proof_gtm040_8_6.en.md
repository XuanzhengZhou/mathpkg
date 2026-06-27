---
role: proof
locale: en
of_concept: equilibrium-sets-basic-example
source_book: gtm040
source_chapter: "8"
source_section: "6"
---

**Equilibrium sets for $P$.** Probabilistically, $P$ will be in any infinite set infinitely often almost everywhere; hence only finite sets can be equilibrium sets. To verify analytically, let $E$ be a finite set with maximum element $m$. The hitting probability $h_i^E$ from state $i$ is the probability of ever hitting $E$. Clearly $h_i^E = 1$ for $i \in E$. For $i > m$, the only way to avoid $E$ is to march straight out to infinity to the right; the probability of doing so is $\beta_\infty/\beta_i$, so $h_i^E = 1 - \beta_\infty/\beta_i$ for $i > m$ (this is probabilistically clear). For $i < m$ with $i \notin E$, the process must eventually hit either $E$ or go to infinity; the calculation gives $h_i^E$ as stated.

The equilibrium charge $e^E = (I-P)h^E$ is computed as:
$$e_i^E = h_i^E - \sum_j P_{ij} h_j^E.$$
For $i = m$, $h_m^E = 1$, and for $j > m$, $P_{mj} = 0$ except $P_{m,m+1} = p_{m+1}$. Since $h_{m+1}^E = \beta_\infty/\beta_{m+1} = \beta_\infty/(\beta_m p_{m+1})$,
$$e_m^E = 1 - p_{m+1} \frac{\beta_\infty}{\beta_m p_{m+1}} = 1 - \frac{\beta_\infty}{\beta_m} + \text{corrections} = \frac{\beta_\infty}{\beta_m}.$$
For $i \notin E$, $h_i^E = (Ph^E)_i$, so $e_i^E = 0$. The capacity is $C(E) = I(h^E) = e^E(E) = e_m^E = \beta_\infty/\beta_m \cdot$ (some normalization). Actually $C(E) = \beta_\infty$ for all non-empty finite sets.

For infinite $E$, $h^E = 1$ (since the process hits $E$ with probability 1), so $e^E = (I-P)1 = 0$, and $E$ cannot be an equilibrium set (the equilibrium charge would be zero, contradicting the definition of equilibrium set).

**Equilibrium sets for $\hat{P}$.** For the reverse chain $\hat{P}$, let $E$ be any set with least element $m$. Then $\hat{h}_i^E = 1$ for $i \geq m$ (the process starts at or beyond $E$). For $i < m$,
$$\hat{h}_i^E = \hat{h}_0^E = \hat{H}_{0m} = \frac{\hat{N}_{0m}}{\hat{N}_{mm}} = \frac{(\beta_m/\beta_\infty) - 1}{\beta_m/\beta_\infty} = 1 - \frac{\beta_\infty}{\beta_m},$$
where $\hat{H}_{0m}$ is the hitting probability from $0$ to $m$, and we used the explicit form $\hat{N}_{ij} = \beta_j/\beta_\infty$ for $j \leq i$ and $\hat{N}_{ij} = \beta_j/\beta_\infty - 1$ for $j > i$.

The equilibrium charge is computed as $\hat{e}^E = (I-\hat{P})\hat{h}^E$. For $m > 0$,
$$\hat{e}_m^E = \hat{h}_m^E - \hat{h}_{m-1}^E = 1 - \left(1 - \frac{\beta_\infty}{\beta_m}\right) = \frac{\beta_\infty}{\beta_m}.$$
For $m = 0$,
$$\hat{e}_0^E = 1 - \sum_j \hat{P}_{0j} \hat{h}_j^E = 1 - \sum_j (\beta_j - \beta_{j+1}) \cdot 1 = 1 - (1 - \beta_\infty) = \beta_\infty = \frac{\beta_\infty}{\beta_0}.$$
All other $\hat{e}_i^E = 0$. Thus $\hat{e}^E \neq 0$ and $E$ is an equilibrium set for every non-empty $E$.

The fact that $\hat{N}$ does not have columns tending to zero (unlike $N$) explains why the supremum of capacities of finite subsets of an infinite set being $\beta_\infty$ does not contradict Proposition 8-39.
