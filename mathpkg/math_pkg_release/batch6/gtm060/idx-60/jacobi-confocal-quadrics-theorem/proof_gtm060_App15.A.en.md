---
role: proof
locale: en
of_concept: jacobi-confocal-quadrics-theorem
source_book: gtm060
source_chapter: "Appendix 15"
source_section: "A"
---

Each point other than $0$ in our space corresponds to an affine hyperplane in the dual space, consisting of those linear functionals whose value is $1$ at the given point. In terms of the dual space, Theorem 1 means that every hyperplane not passing through $0$ in an $n$-dimensional euclidean space is tangent to precisely $n$ of the quadrics in a euclidean pencil, and the vectors from $0$ to the points of tangency are pairwise orthogonal.

The proof of the property of euclidean pencils just stated is based on the fact that the aforementioned vectors define the principal axes of the quadratic forms

$$B = \frac{1}{2}(Ax, x) - \frac{1}{2}(l, x)^2,$$

where $(l, x) = 1$ is the equation of the hyperplane.

As a matter of fact, on a principal axis of any quadratic form $B$, corresponding to the proper value $\lambda$, the form $B - \lambda E$ reduces to $0$ along with its gradient. The vanishing of this form at the point of intersection of the principal axis and the hyperplane means that the point of intersection lies on the quadric $\frac{1}{2}(Ax, x) = 1$, while the vanishing of the gradient means that the quadric and the hyperplane are tangent at the point.

Jacobi's theorem then follows by duality: the $n$ principal axes of $B$ correspond to $n$ confocal quadrics passing through the original point, and the orthogonality of the principal axes implies the right-angle intersection of the confocal quadrics.
