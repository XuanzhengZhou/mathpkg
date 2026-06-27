---
role: proof
locale: en
of_concept: adjoint-representation-of-lie-algebra
source_book: gtm009
source_chapter: "I"
source_section: "2.2"
---
It is clear that $\operatorname{ad}$ is a linear transformation. To see that it preserves the bracket, we calculate:

$$[\operatorname{ad} x, \operatorname{ad} y](z) = \operatorname{ad} x \operatorname{ad} y(z) - \operatorname{ad} y \operatorname{ad} x(z)$$
$$= \operatorname{ad} x([yz]) - \operatorname{ad} y([xz])$$
$$= [x[yz]] - [y[xz]]$$
$$= [x[yz]] + [[xz]y]$$
$$= [[xy]z]$$
$$= \operatorname{ad}[xy](z).$$

Here we used the Jacobi identity $[x[yz]] + [y[zx]] + [z[xy]] = 0$, which gives $[x[yz]] - [y[xz]] = -[z[xy]]$. Together with $[[xz]y] = -[y[xz]]$, we have $[x[yz]] + [[xz]y] = [[xy]z]$, completing the verification.
