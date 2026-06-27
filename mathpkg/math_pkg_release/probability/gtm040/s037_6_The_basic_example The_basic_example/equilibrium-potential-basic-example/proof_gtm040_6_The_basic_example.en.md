---
role: proof
locale: en
of_concept: equilibrium-potential-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

For $P$ and a finite set $E$ with last element $m$: probabilistically, when $i > m$, the only way to avoid hitting $E$ from $i$ is to march straight out to the right forever. The probability of this is $\beta_\infty/\beta_i$, since $\beta_\infty/\beta_i = \prod_{k=i+1}^\infty p_k$ is the probability of never returning to 0 from state $i$. Hence $h_i^E = 1 - \beta_\infty/\beta_i$.

For $i \leq m$, the chain must hit $E$ with probability 1, since eventually it will return to 0 and then enter $E$. Thus $h_i^E = 1$ for $i \leq m$.

The equilibrium charge is $e^E = (I-P)h^E$. Computing:
$$e_i^E = h_i^E - (Ph^E)_i = h_i^E - (p_{i+1} h_{i+1}^E + q_{i+1} h_0^E).$$

For $i = m$: since $h_{m+1}^E = 1 - \beta_\infty/\beta_{m+1}$ and $h_0^E = 1$, we have
$$e_m^E = 1 - \left(p_{m+1}\left(1 - \frac{\beta_\infty}{\beta_{m+1}}\right) + q_{m+1} \cdot 1\right) = 1 - \left(p_{m+1} - \beta_\infty/\beta_m + q_{m+1}\right) = \frac{\beta_\infty}{\beta_m}.$$

For $i < m$ (with $i \in E$): $h_i^E = h_{i+1}^E = 1$, so $e_i^E = 1 - (p_{i+1} \cdot 1 + q_{i+1} \cdot 1) = 0$.

The total capacity is $C(E) = \sum_i e_i^E = \beta_\infty/\beta_m \cdot \beta_m = \beta_\infty$.

For $\hat{P}$ with set $E$ having least element $m$: when $i \geq m$, the process is already in $E$ so $\hat{h}_i^E = 1$. For $i < m$, the chain must reach $m$ by deterministic leftward steps. Since from $i$ it reaches 0 deterministically, $\hat{h}_i^E = \hat{h}_0^E$ for all $i < m$. From state 0, the probability of hitting $m$ before absorption is $\hat{H}_{0m} = \hat{N}_{0m}/\hat{N}_{mm}$. Using the formulas for $\hat{N}$:
$$\hat{H}_{0m} = \frac{(\beta_m/\beta_\infty) - 1}{\beta_m/\beta_\infty} = 1 - \frac{\beta_\infty}{\beta_m}.$$

Thus $\hat{h}_i^E = 1 - \beta_\infty/\beta_m$ for all $i < m$.

For the equilibrium charge when $m > 0$:
$$\hat{e}_m^E = [(I - \hat{P})\hat{h}^E]_m = \hat{h}_m^E - \hat{h}_{m-1}^E = 1 - \left(1 - \frac{\beta_\infty}{\beta_m}\right) = \frac{\beta_\infty}{\beta_m}.$$

When $m = 0$:
$$\hat{e}_0^E = 1 - \sum_j \hat{P}_{0j} = 1 - (1 - \beta_\infty) = \beta_\infty = \frac{\beta_\infty}{\beta_0},$$
since $\beta_0 = 1$.
