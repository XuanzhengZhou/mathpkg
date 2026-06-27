---
role: proof
locale: en
of_concept: dense-iff-total-in-finite-topology
source_book: gtm031
source_chapter: "Chapter VIII: The Ring of Linear Transformations"
source_section: "7. Total subspaces of R*"
---
**Proof.** First, if $\mathfrak{R}'$ is dense in $\mathfrak{R}^*$, then for any $u \neq 0$ in $\mathfrak{R}$, there exists a basic open set containing some $f$ with $f(u) \neq 0$ that intersects $\mathfrak{R}'$, so $\mathfrak{R}'$ is total.

Conversely, assume $\mathfrak{R}'$ is total. By the Lemma on complementary vectors, for any linearly independent $x_1, \ldots, x_m$ in $\mathfrak{R}$, $\mathfrak{R}'$ contains vectors $x_1^*, \ldots, x_m^*$ with $x_i^*(x_j) = \delta_{ij}$. If $\beta_i$ ($i = 1, \ldots, m$) are arbitrary elements of $\Delta$, then $f = \sum x_i^* \beta_i \in \mathfrak{R}'$ and $f(x_i) = \beta_i$. Hence $\mathfrak{R}'$ is dense by the criterion for density in the finite topology.
