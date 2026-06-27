---
role: proof
locale: en
of_concept: kronecker-product-dimension-characterization
source_book: gtm031
source_chapter: "7"
source_section: "4"
---

The necessity of the condition $\dim \mathfrak{P} = \dim \Re \cdot \dim \mathfrak{S}$ has already been proved.

Conversely, let $\dim \mathfrak{P} = \dim \Re \cdot \dim \mathfrak{S}$. Let $(e_1, e_2, \cdots, e_n)$ be a basis for $\Re$ and let $(f_1, f_2, \cdots, f_m)$ be a basis for $\mathfrak{S}$. Then it follows easily that the vectors $e_i \times f_j$ are generators of $\mathfrak{P}$. Since their number is $nm$, they constitute a basis.

Now suppose that $e_1, e_2, \cdots, e_r$ are any linearly independent vectors in $\Re$. Then we can suppose that these are part of a basis for $\Re$. If $\sum e_i \times y_i = 0$, we can write $y_i = \sum \beta_{ij} f_j$ and we obtain $\sum_{i,j} \beta_{ij} e_i \times f_j = 0$. Hence each $\beta_{ij} = 0$, and this means that each $y_i = 0$. In a similar manner we establish the second independence condition. Thus $\mathfrak{P}$ is a Kronecker product of $\Re$ and $\mathfrak{S}$.
