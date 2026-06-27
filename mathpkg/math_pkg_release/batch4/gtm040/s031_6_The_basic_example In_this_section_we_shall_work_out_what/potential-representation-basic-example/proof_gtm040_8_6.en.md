---
role: proof
locale: en
of_concept: potential-representation-basic-example
source_book: gtm040
source_chapter: "8"
source_section: "6"
---

These formulas are obtained by direct computation using the explicit form of the potential kernel $N = (I-P)^{-1}$ for the basic example.

**Derivation of formula (1).** For the basic example, the potential kernel entries are known to be
$$N_{ij} = \begin{cases} \dfrac{\beta_j}{\beta_\infty} - \dfrac{\beta_j}{\beta_i} & \text{if } j < i \\[8pt] \dfrac{\beta_j}{\beta_\infty} & \text{if } j \geq i. \end{cases}$$
Then for $g = Nf$, we compute componentwise:
$$g_i = \sum_{j=0}^{\infty} N_{ij} f_j = \sum_{j=0}^{i-1} \left(\frac{\beta_j}{\beta_\infty} - \frac{\beta_j}{\beta_i}\right) f_j + \sum_{j=i}^{\infty} \frac{\beta_j}{\beta_\infty} f_j$$
$$= \frac{1}{\beta_\infty} \sum_{j=0}^{\infty} \beta_j f_j - \frac{1}{\beta_i} \sum_{j=0}^{i-1} \beta_j f_j.$$

**Derivation of formula (2).** For the reverse chain $\hat{P}$, the potential kernel $\hat{N} = (I-\hat{P})^{-1}$ has entries
$$\hat{N}_{ij} = \begin{cases} \dfrac{\beta_j}{\beta_\infty} - 1 & \text{if } j > i \\[8pt] \dfrac{\beta_j}{\beta_\infty} & \text{if } j \leq i. \end{cases}$$
Then for $g = \hat{N}f$,
$$g_i = \sum_{j=0}^{\infty} \hat{N}_{ij} f_j = \sum_{j=0}^{i} \frac{\beta_j}{\beta_\infty} f_j + \sum_{j=i+1}^{\infty} \left(\frac{\beta_j}{\beta_\infty} - 1\right) f_j$$
$$= \frac{1}{\beta_\infty} \sum_{j=0}^{\infty} \beta_j f_j - \sum_{j=i+1}^{\infty} f_j.$$

**Finiteness criterion.** If $\beta|f| < \infty$, then both expressions are finite-valued:
- For (1): $|g_i| \leq \frac{1}{\beta_\infty} \sum \beta_j |f_j| + \frac{1}{\beta_i} \sum_{j=0}^{i-1} \beta_j |f_j| < \infty$.
- For (2): Since $\beta_j \geq \beta_\infty$ for all $j$, we have $\sum_j |f_j| \leq \frac{1}{\beta_\infty} \sum_j \beta_j |f_j| < \infty$, and then $|g_i| \leq \frac{1}{\beta_\infty} \sum \beta_j |f_j| + \sum_{j=i+1}^\infty |f_j| < \infty$.

These results agree with Lemma 8-2, which states that a charge $f$ has a finite potential if and only if $\beta|f| < \infty$.

**Duality.** Let $\mu_i = \beta_i f_i$ (dual charge) and $\nu_i = \beta_i g_i$ (dual potential). Then from (1),
$$\nu_i = \frac{\beta_i}{\beta_\infty} \sum_{j=0}^{\infty} \mu_j - \sum_{j=0}^{i-1} \mu_j = (\mu \hat{N})_i,$$
confirming that $\mu$ is a left charge for $\hat{P}$ with potential measure $\nu$, as required by the duality between $P$ and $\hat{P}$.
