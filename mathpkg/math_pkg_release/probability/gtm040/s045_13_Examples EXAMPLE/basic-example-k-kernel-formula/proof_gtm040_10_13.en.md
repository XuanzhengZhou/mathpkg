---
role: proof
locale: en
of_concept: basic-example-k-kernel-formula
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

Recall from Chapter 5 that

$$N_{ij} = \begin{cases} \frac{\beta_j}{\beta_\infty} & \text{if } i \leq j \\ \frac{\beta_j}{\beta_\infty} - \frac{\beta_j}{\beta_i} & \text{if } i > j. \end{cases}$$

With $\pi$ chosen as a unit mass at $0$, the Martin kernel is $K(i,j) = N_{ij}/N_{0j}$. Since $0 \leq j$ for all $j$ (state space is $\{0,1,2,\ldots\}$), we have $N_{0j} = \beta_j/\beta_\infty$. Therefore for $i \leq j$,

$$K(i,j) = \frac{\beta_j/\beta_\infty}{\beta_j/\beta_\infty} = 1,$$

and for $i > j$,

$$K(i,j) = \frac{\frac{\beta_j}{\beta_\infty} - \frac{\beta_j}{\beta_i}}{\frac{\beta_j}{\beta_\infty}} = 1 - \frac{\beta_\infty}{\beta_i} = \frac{\beta_i - \beta_\infty}{\beta_i}.$$
