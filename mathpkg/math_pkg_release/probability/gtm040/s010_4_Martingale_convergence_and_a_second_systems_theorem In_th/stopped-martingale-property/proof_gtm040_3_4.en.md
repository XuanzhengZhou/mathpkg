---
role: proof
locale: en
of_concept: stopped-martingale-property
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

We first note that $M[|\hat{f}_n|] < \infty$ since

$$|\hat{f}_n| \leq \sum_{j=0}^{n} |f_j|$$

and each $f_j$ is integrable.

Next, let $R$ be a cell in $\mathcal{R}_n$ with $\mu(R) \neq 0$. In $R$ we compute the conditional expectation:

$$M[\hat{f}_{n+1} \mid \mathcal{R}_n] = \frac{1}{\mu(R)} \int_R \hat{f}_{n+1} \, d\mu$$

$$= \frac{1}{\mu(R)} \left[ \int_{R \cap \{t \leq n\}} \hat{f}_{n+1} \, d\mu + \int_{R \cap \{t > n\}} \hat{f}_{n+1} \, d\mu \right].$$

On $R \cap \{t \leq n\}$, we have $\hat{f}_{n+1} = \hat{f}_n$ (since the process has already stopped), so the first integral equals $\int_{R \cap \{t \leq n\}} \hat{f}_n \, d\mu$.

On $R \cap \{t > n\}$, we have $\hat{f}_{n+1} = f_{n+1}$ and $\hat{f}_n = f_n$. Since $\{t > n\}$ is a union of cells of $\mathcal{R}_n$, and $(f_n, \mathcal{R}_n)$ is a martingale,

$$\int_{R \cap \{t > n\}} f_{n+1} \, d\mu = \int_{R \cap \{t > n\}} f_n \, d\mu = \int_{R \cap \{t > n\}} \hat{f}_n \, d\mu.$$

Combining both parts,

$$M[\hat{f}_{n+1} \mid \mathcal{R}_n] = \frac{1}{\mu(R)} \int_R \hat{f}_n \, d\mu = \hat{f}_n$$

on $R$. Therefore $(\hat{f}_n, \mathcal{R}_n)$ satisfies the martingale property and is integrable, hence is a martingale.
