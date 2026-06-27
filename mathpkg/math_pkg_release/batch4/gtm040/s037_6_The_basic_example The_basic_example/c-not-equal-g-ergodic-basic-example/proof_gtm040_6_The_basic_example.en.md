---
role: proof
locale: en
of_concept: c-not-equal-g-ergodic-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

Suppose for contradiction that $C_{0j} = G_{0j}$ for all $j$ in an ergodic basic example.

From the formulas derived for the ergodic case:
$$C_{0j} = \frac{\sigma_j}{\sigma_\infty} - \frac{\alpha_j}{\alpha_0} \frac{\sigma_0}{\sigma_\infty} = \frac{\sigma_j}{\sigma_\infty},$$
since $\sigma_0 = 0$ and $\alpha_0 = \beta_0/\sigma_\infty = 1/\sigma_\infty$.

And:
$$G_{0j} = (j-0)\alpha_j = j \alpha_j,$$
since $j \geq 0$.

Equating $C_{0j} = G_{0j}$:
$$\frac{\sigma_j}{\sigma_\infty} = j \alpha_j = j \frac{\beta_j}{\sigma_\infty},$$
so $\sigma_j = j \beta_j$ for all $j$.

Now $\sigma_j = \sum_{k=0}^{j-1} \beta_k$, so:
$$\sum_{k=0}^{j-1} \beta_k = j \beta_j.$$

For $j = 1$: $\beta_0 = 1 \cdot \beta_1$, so $\beta_1 = 1$.
For $j = 2$: $\beta_0 + \beta_1 = 2 \beta_2$, so $1 + 1 = 2\beta_2$, hence $\beta_2 = 1$.

By induction, if $\beta_k = 1$ for all $k < j$, then:
$$\sum_{k=0}^{j-1} \beta_k = j = j \beta_j,$$
so $\beta_j = 1$ for all $j$.

But this contradicts the fact that in any recurrent basic example, $\beta_j \to 0$ as $j \to \infty$ (this is necessary for recurrence). Therefore $C$ cannot equal $G$ in the ergodic case.

Note: In the null recurrent case, $C = G$ does hold (as shown in the null basic example potential kernel result), demonstrating that the equality is a characteristic property of the null recurrent regime.
