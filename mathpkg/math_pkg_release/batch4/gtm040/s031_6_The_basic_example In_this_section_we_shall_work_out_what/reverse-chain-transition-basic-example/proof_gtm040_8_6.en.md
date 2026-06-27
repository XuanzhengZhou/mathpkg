---
role: proof
locale: en
of_concept: reverse-chain-transition-basic-example
source_book: gtm040
source_chapter: "8"
source_section: "6"
---

The $\beta$-dual transition probabilities are defined by $\hat{P}_{ij} = \frac{\beta_j P_{ji}}{\beta_i}$. For the basic example, the forward chain $P$ has the following non-zero transitions:
$$P_{i,i+1} = p_{i+1}, \quad P_{i,0} = q_{i+1} \quad (i \geq 0),$$
together with $P_{00} = q_1$ (the case $i=0$ of the same formula).

**Case 1:** $i > 0$ and $j = i-1$. Then
$$\hat{P}_{i,i-1} = \frac{\beta_{i-1} P_{i-1,i}}{\beta_i} = \frac{\beta_{i-1} p_i}{\beta_i}.$$
Since $\beta_i = \beta_{i-1} p_i$, we obtain $\hat{P}_{i,i-1} = 1$.

**Case 2:** $i > 0$ and $j = 0$. Then
$$\hat{P}_{i,0} = \frac{\beta_0 P_{0i}}{\beta_i} = \frac{1 \cdot q_{i+1}}{\beta_i} = 0,$$
since $P_{0i} = q_{i+1}$ but this would require $P_{0i} \neq 0$ with the reverse index, which does not occur for the basic example. More systematically, for $i > 0$ and $j \neq i-1$, we have $P_{ji} = 0$ because the only transition into state $i$ in the forward chain comes from $i-1$ (via $P_{i-1,i} = p_i$) or from state $0$ (via $P_{0,i}$ which is not a transition in the basic example—the forward chain goes from $i$ to $i+1$ or to $0$, so the reverse transition $P_{ji}$ for $j \neq i-1$ is zero).

**Case 3:** $i = 0$. Then for any $j \geq 0$,
$$\hat{P}_{0j} = \frac{\beta_j P_{j0}}{\beta_0} = \beta_j \cdot q_{j+1}.$$
Using $q_{j+1} = 1 - p_{j+1}$ and $\beta_{j+1} = \beta_j p_{j+1}$, we have
$$\beta_j q_{j+1} = \beta_j(1 - p_{j+1}) = \beta_j - \beta_j p_{j+1} = \beta_j - \beta_{j+1}.$$

**Interpretation of the reverse process.** For $i > 0$, $\hat{P}_{i,i-1} = 1$ means the reverse process moves deterministically one step left from $i$ to $i-1$. Once at $0$, it jumps to state $j$ with probability $\beta_j - \beta_{j+1}$. The total probability of leaving $0$ is
$$\sum_{j=0}^\infty \hat{P}_{0j} = \sum_{j=0}^\infty (\beta_j - \beta_{j+1}) = \beta_0 - \lim_{j \to \infty} \beta_j = 1 - \beta_\infty.$$
In the transient case $\beta_\infty > 0$, so this sum is strictly less than $1$, meaning the extended chain for $\hat{P}$ is absorbing (the process may remain at $0$ forever with positive probability $\beta_\infty$). Since every state $i > 0$ reaches $0$ in the reverse chain with probability $1$ (deterministically in $i$ steps), the extended chain is indeed absorbing.
