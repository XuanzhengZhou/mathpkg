---
role: proof
locale: en
of_concept: recurrence-criterion-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

For the basic example, the probability of never returning to 0 starting from state $i$ is exactly $\beta_\infty/\beta_i$. This can be seen as follows: from state $i$, to avoid ever hitting 0, the chain must always take the forward step $i \to i+1 \to i+2 \to \cdots$, which has probability $\prod_{k=i+1}^\infty p_k = \beta_\infty/\beta_i$.

The chain starting from 0 is recurrent if and only if the return probability to 0 is 1. The probability of no return to 0 is
$$P_0[\text{never return}] = \sum_{j=1}^\infty P_{0j} \cdot \frac{\beta_\infty}{\beta_j} = \sum_{j=1}^\infty (\beta_j - \beta_{j+1}) \cdot \frac{\beta_\infty}{\beta_j}.$$

When $\beta_\infty = 0$, this sum is 0, so return is almost sure and the chain is recurrent. When $\beta_\infty > 0$, the probability of never returning is
$$\sum_{j=1}^\infty (\beta_j - \beta_{j+1}) \frac{\beta_\infty}{\beta_j} = \beta_\infty \sum_{j=1}^\infty \left(1 - \frac{\beta_{j+1}}{\beta_j}\right) = \beta_\infty \sum_{j=1}^\infty q_{j+1},$$
which equals $\beta_\infty$ times a possibly divergent sum. In particular, it is positive, so the chain is transient.

When $\beta_\infty = 0$ and $\sum_i \beta_i = +\infty$, the expected return time to 0 is infinite (null recurrence). When $\sum_i \beta_i < \infty$, the chain is positive recurrent with stationary distribution $\alpha_j = \beta_j / \sum_k \beta_k$, which can be verified by checking $\alpha P = \alpha$.
