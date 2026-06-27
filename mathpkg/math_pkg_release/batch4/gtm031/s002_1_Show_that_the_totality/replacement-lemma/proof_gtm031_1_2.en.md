---
role: proof
locale: en
of_concept: replacement-lemma
source_book: gtm031
source_chapter: "1"
source_section: "2"
---

Suppose that the $x_i$ are linearly independent and let $\beta_i$ be elements of $\Delta$ such that $\sum \beta_i x_i' = 0$. Then

$$
\beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_{m-1} x_{m-1} + \beta_m(x_m + \rho x_1) = 0,
$$

which expands to

$$
(\beta_1 + \beta_m \rho) x_1 + \beta_2 x_2 + \cdots + \beta_{m-1} x_{m-1} + \beta_m x_m = 0.
$$

Since the $x_i$ are linearly independent, all coefficients vanish: $\beta_m = 0$, $\beta_i = 0$ for $i = 2, \ldots, m-1$, and $\beta_1 + \beta_m \rho = \beta_1 = 0$. Thus all $\beta_i = 0$, proving the $x_i'$ are linearly independent.

Conversely, if the $x_i'$ are linearly independent, we recover the $x_i$ from the $x_i'$ by the inverse operation $x_m = x_m' - \rho x_1'$, and the same argument shows the $x_i$ are linearly independent.
