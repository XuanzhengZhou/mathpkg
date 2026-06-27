---
role: proof
locale: en
of_concept: linear-dependence-extension-lemma
source_book: gtm031
source_chapter: "1"
source_section: "2"
---

We have $\beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_m x_m + \beta_{m+1} x_{m+1} = 0$ where some $\beta_k \neq 0$. If $\beta_{m+1} = 0$, this implies that $x_1, \cdots, x_m$ are linearly dependent, contrary to assumption. Hence $\beta_{m+1} \neq 0$. We may therefore solve for $x_{m+1}$, obtaining an expression for it in terms of $x_1, \cdots, x_m$:

$$
x_{m+1} = -\beta_{m+1}^{-1}(\beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_m x_m).
$$

Thus $x_{m+1}$ is linearly dependent on $x_1, \cdots, x_m$.
