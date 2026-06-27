---
role: proof
locale: en
of_concept: structure-of-plane-f-case-ii
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

Let $F$ be the plane spanned by the eigenvectors $e$ and $e'$, and write an arbitrary vector $z \in F$ as $z = \xi e + \eta e'$ with scalars $\xi, \eta$. Since $e$ and $e'$ are light-vectors, we have $(e, e) = 0$ and $(e', e') = 0$. Computing the inner product using bilinearity:

$$(z, z) = (\xi e + \eta e', \xi e + \eta e') = \xi^2(e, e) + 2\xi\eta(e, e') + \eta^2(e', e') = 2(e, e')\xi\eta.$$

Since $(e, e') \neq 0$ (as established by the linear independence of two light-vectors, cf. sec. 9.21), the quadratic form $(z,z)$ is nondegenerate on $F$. In the coordinates $(\xi, \eta)$, the metric has the matrix $\begin{pmatrix} 0 & (e,e') \\ (e,e') & 0 \end{pmatrix}$, whose signature is $(1,1)$, hence the index (number of negative eigenvalues) equals $1$. Thus $F$ is a pseudo-Euclidean plane of index $1$.
