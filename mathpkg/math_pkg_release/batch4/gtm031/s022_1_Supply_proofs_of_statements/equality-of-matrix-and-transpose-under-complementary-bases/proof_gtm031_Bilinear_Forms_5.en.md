---
role: proof
locale: en
of_concept: equality-of-matrix-and-transpose-under-complementary-bases
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "5"
---

Let $\{e_i\}$ be a basis for $\mathfrak{R}_1$ and $\{e_i'\}$ the complementary basis in $\mathfrak{R}_1'$, so that $g_1(e_i, e_j') = \delta_{ij}$. Similarly let $\{f_k\}$ be a basis for $\mathfrak{R}_2$ and $\{f_k'\}$ the complementary basis in $\mathfrak{R}_2'$, so $g_2(f_k, f_l') = \delta_{kl}$.

Suppose $A : \mathfrak{R}_1 \to \mathfrak{R}_2$ has matrix $(\alpha_{ik})$:

$$e_i A = \sum_{k=1}^{n_2} \alpha_{ik} f_k.$$

Let $A' : \mathfrak{R}_2' \to \mathfrak{R}_1'$ be the transpose of $A$, defined by the adjoint relation

$$g_2(x A, y') = g_1(x, y' A')$$

for all $x \in \mathfrak{R}_1$, $y' \in \mathfrak{R}_2'$. Suppose $A'$ has matrix $(\alpha_{jl}')$ relative to the complementary bases:

$$f_l' A' = \sum_{j=1}^{n_1} e_j' \alpha_{jl}'.$$

Now evaluate the adjoint relation with $x = e_i$ and $y' = f_l'$:

$$g_2(e_i A, f_l') = g_1(e_i, f_l' A').$$

The left-hand side expands as

$$g_2\!\left(\sum_{k=1}^{n_2} \alpha_{ik} f_k,\; f_l'\right) = \sum_{k=1}^{n_2} \alpha_{ik}\, g_2(f_k, f_l') = \sum_{k=1}^{n_2} \alpha_{ik} \delta_{kl} = \alpha_{il}.$$

The right-hand side expands as

$$g_1\!\left(e_i,\; \sum_{j=1}^{n_1} e_j' \alpha_{jl}'\right) = \sum_{j=1}^{n_1} g_1(e_i, e_j')\, \alpha_{jl}' = \sum_{j=1}^{n_1} \delta_{ij}\, \alpha_{jl}' = \alpha_{il}'.$$

Therefore $\alpha_{il} = \alpha_{il}'$ for all $i = 1, \dots, n_1$ and $l = 1, \dots, n_2$. Hence the matrices $(\alpha_{ik})$ and $(\alpha_{jl}')$ are equal.
