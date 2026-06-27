---
role: proof
locale: en
of_concept: matrix-representation-of-bilinear-forms
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

The result follows immediately from the definitions. Given ordered basis $(a_1, \ldots, a_n)$ and vectors $a, b$ with coordinate rows $x = (x_1, \ldots, x_n)$, $y = (y_1, \ldots, y_n)$, the bilinearity of $\sigma$ yields

$$\sigma(a, b) = \sum s_{ij} x_i y_j$$

where $s_{ij} = \sigma(a_i, a_j)$. If $S$ is the $n \times n$ matrix $(s_{ij})$, this may be written in matrix form as $\sigma(a, b) = x S y^t$. The mapping $\sigma \mapsto S$ is clearly linear and bijective, establishing (1). Part (2) follows by the same reasoning applied to the polynomial ring.
