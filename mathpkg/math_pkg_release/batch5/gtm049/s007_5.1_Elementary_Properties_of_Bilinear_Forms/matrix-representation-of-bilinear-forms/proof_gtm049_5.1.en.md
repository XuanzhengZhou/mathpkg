---
role: proof
locale: en
of_concept: matrix-representation-of-bilinear-forms
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

The mapping $\sigma \mapsto (\sigma; (a_i))$ sends each bilinear form to the matrix $(s_{ij})$ where $s_{ij} = \sigma(a_i, a_j)$. For any scalars $x$, the form $x\sigma$ has matrix $(x s_{ij}) = x(s_{ij})$, and for two forms $\sigma, \tau$, the sum $\sigma + \tau$ has matrix $(\sigma(a_i, a_j) + \tau(a_i, a_j))$. So the mapping is linear.

To show it is an isomorphism, note that given any matrix $(s_{ij})$, one can define a bilinear form by $\sigma(a, b) = \sum s_{ij} x_i y_j$ where $(x_i), (y_j)$ are the coordinate rows of $a, b$. This form maps to $(s_{ij})$, establishing surjectivity. If $(\sigma; (a_i))$ is the zero matrix, then $\sigma(a_i, a_j) = 0$ for all basis vectors, and by bilinearity $\sigma(a, b) = 0$ for all $a, b$, so $\sigma = 0$, establishing injectivity. Thus the mapping is a linear isomorphism.

The second mapping is simply the composition of the first with the obvious linear isomorphism $F^{n \times n} \to \{\text{bilinear polynomials}\}$ sending $(s_{ij})$ to $\sum s_{ij} X_i Y_j$, which is clearly linear, one-to-one, and onto.
