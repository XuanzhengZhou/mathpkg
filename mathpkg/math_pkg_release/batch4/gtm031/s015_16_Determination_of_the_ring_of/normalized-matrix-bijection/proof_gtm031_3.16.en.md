---
role: proof
locale: en
of_concept: normalized-matrix-bijection
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

We already know that $(\beta) \mapsto B$ is a surjective homomorphism $\mathfrak{M} \to \mathfrak{B}$. The endomorphism $B$ determined by $(\beta)$ is $0$ if and only if $\sum_j \beta_{ij} f_j = 0$ for all $i$, which means $\beta_{ij} \equiv 0 \pmod{\delta_j}$ for all $i, j$. Thus the kernel consists of matrices $(\beta)$ for which there exists $(\mu)$ such that $(\beta) = (\mu) \operatorname{diag}(\delta_1, \ldots, \delta_t)$.

Now suppose two normalized matrices $(\beta), (\beta') \in \mathfrak{U}$ determine the same endomorphism. Then their difference $(\beta - \beta')$ is in the kernel, so for each $i, j$ we have $\beta_{ij} - \beta'_{ij} \equiv 0 \pmod{\delta_j}$. But for normalized matrices, the entries are already reduced modulo the appropriate quantities (by the four defining conditions). In particular, for $i \geq j$, $\beta_{ij}$ is arbitrary but determined modulo $\delta_j$; the normalization fixes a canonical representative in each residue class. The four cases of the normalized form ensure that the only matrix in $\mathfrak{U}$ that lies in the kernel is the zero matrix. Hence $\beta = \beta'$, establishing injectivity on $\mathfrak{U}$.

Surjectivity follows because every $B \in \mathfrak{B}$ has some matrix representation $(\beta) \in \mathfrak{M}$, and by adjusting entries modulo the appropriate $\delta_j$ we can bring it to normalized form without changing the endomorphism.
