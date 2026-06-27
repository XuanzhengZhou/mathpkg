---
role: proof
locale: en
of_concept: desargues-theorem-affine
source_book: gtm049
source_chapter: "II"
source_section: "2.4"
---

We may assume that the plane $S$ of the triangles $ABC, A'B'C'$ is contained in an affine geometry $\mathcal{A}(V)$ but does not contain $0_V$.

We choose any homogeneous vector $p$ for $P$ and use Lemma 5 to find homogeneous vectors $a, a'; b, b'; c, c'$ for $A, A'; B, B'; C, C'$, respectively such that

$$a' = p + a, \quad b' = p + b, \quad c' = p + c.$$

Now $b' - c' = b - c = l$, say, is a non-zero vector which is a homogeneous vector for $L = BC \cap B'C'$ (or, if $BC$ is parallel to $B'C'$, it is a vector parallel to these lines). Similarly, $m = c - a$ and $n = a - b$ are homogeneous vectors for $M$ and $N$ respectively. Since $l + m + n = 0$, the vectors $l, m, n$ are linearly dependent; they lie in a 2-dimensional subspace. Hence $L, M, N$ are collinear.

If $BC$ is parallel to $B'C'$, then the vector $l$ is parallel to $S$ but does not correspond to a point of intersection; however, in this case the collinearity still holds when interpreted projectively. The same applies if other sides are parallel.

The proof also yields the theorem when interpreted with homogeneous vectors and allows one or more of the intersection points to be "at infinity" (i.e., corresponding lines are parallel), which becomes fully rigorous in the projective setting.
