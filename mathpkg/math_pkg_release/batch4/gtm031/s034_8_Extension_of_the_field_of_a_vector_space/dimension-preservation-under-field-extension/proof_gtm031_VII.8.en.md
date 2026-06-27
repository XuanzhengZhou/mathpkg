---
role: proof
locale: en
of_concept: dimension-preservation-under-field-extension
source_book: gtm031
source_chapter: "VII"
source_section: "8"
---

Let $(e_1, e_2, \dots, e_n)$ be a basis for $\mathfrak{R}$ over $\Phi$ and set $\bar{e}_i = 1 \times e_i$.

First, we show that the $\bar{e}_i$ span $\mathfrak{R}_P$ over $P$. Any $z \in \mathfrak{R}_P = P \times \mathfrak{R}$ has the form

$$z = \sum_{i=1}^n \rho_i \times e_i$$

for some $\rho_i \in P$. Since $\rho_i \times e_i = \rho_i(1 \times e_i) = \rho_i \bar{e}_i$, we obtain

$$z = \sum_{i=1}^n \rho_i \bar{e}_i.$$

Thus every element of $\mathfrak{R}_P$ is a $P$-linear combination of the $\bar{e}_i$.

Next, we show linear independence over $P$. Suppose

$$\sum_{i=1}^n \rho_i \bar{e}_i = 0$$

for some $\rho_i \in P$. Then $\sum_{i=1}^n \rho_i \times e_i = 0$. Since the $e_i$ are linearly independent over $\Phi$, it follows that every $\rho_i = 0$. (The linear independence of the $e_i$ over $\Phi$ implies their $P$-linear independence in the Kronecker product.)

Therefore $(\bar{e}_1, \bar{e}_2, \dots, \bar{e}_n)$ is a basis for $\mathfrak{R}_P$ over $P$, and consequently

$$\dim_P(\mathfrak{R}_P) = n = \dim_\Phi(\mathfrak{R}).$$
