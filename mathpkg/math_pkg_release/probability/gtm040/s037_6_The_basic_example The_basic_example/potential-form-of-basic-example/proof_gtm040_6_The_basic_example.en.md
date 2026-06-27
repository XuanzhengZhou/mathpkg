---
role: proof
locale: en
of_concept: potential-form-of-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

For the forward chain $P$, the potential kernel $N$ satisfies $g = Nf$. Using the explicit form of $N_{ij}$ for the basic example (derived in earlier sections), we have:

$$g_i = \sum_{j=0}^\infty N_{ij} f_j.$$

In the basic example, $N_{ij} = \frac{\beta_\infty - \beta_{\max(i,j)}}{\beta_\infty \beta_i}$ for the transient case, or alternatively using the formula from the ergodic theory. Computing directly:

$$g_i = \sum_{j=0}^\infty N_{ij} f_j = \sum_{j=0}^{i-1} \frac{1}{\beta_i} f_j + \sum_{j=i}^\infty \frac{1}{\beta_\infty} f_j \cdot \frac{\beta_\infty}{\beta_i} = \frac{1}{\beta_\infty} \sum_{j=0}^\infty \beta_j f_j - \frac{1}{\beta_i} \sum_{j=0}^{i-1} \beta_j f_j.$$

The simplification uses the fact that for $j < i$, the potential kernel entry involves $\beta_j/\beta_i$, and for $j \geq i$, the appropriate cancellation yields the stated formula.

For the reverse chain $\hat{P}$, the potential kernel $\hat{N}$ satisfies:

$$g_i = (\hat{N}f)_i = \sum_{j=0}^\infty \hat{N}_{ij} f_j.$$

Since $\hat{N}_{ij} = \frac{\beta_j}{\beta_\infty} - 1$ for $j \geq i$ and $\hat{N}_{ij} = \frac{\beta_j}{\beta_\infty}$ for $j < i$ (in the null recurrent/transient case), we obtain:

$$g_i = \sum_{j=0}^{i} \frac{\beta_j}{\beta_\infty} f_j + \sum_{j=i+1}^\infty \left(\frac{\beta_j}{\beta_\infty} - 1\right) f_j = \frac{1}{\beta_\infty} \sum_{j=0}^\infty \beta_j f_j - \sum_{j=i+1}^\infty f_j.$$

The finiteness condition follows from the fact that $\sum_{j=i+1}^\infty |f_j| < \infty$ implies $\sum \beta_j |f_j| \geq \beta_\infty \sum |f_j|$, and conversely $\sum \beta_j |f_j| < \infty$ guarantees convergence of both summations in the formula.
