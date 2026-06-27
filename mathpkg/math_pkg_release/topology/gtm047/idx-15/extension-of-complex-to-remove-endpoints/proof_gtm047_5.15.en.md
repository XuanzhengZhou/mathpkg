---
role: proof
locale: en
of_concept: extension-of-complex-to-remove-endpoints
source_book: gtm047
source_chapter: "5"
source_section: "15"
---

The end-points of $K$ are all vertices, and so they form at most a countable set. Therefore to each end-point $v$ of $K$ we can attach a half-open interval of the form $vv' - v'$, such that $vv' \cap |K| = \{v\}$. If the intervals $vv'$ are sufficiently short, are disjoint, and form a contracting collection, then the union of $K$ and all intervals $vv' - \{v'\}$ has a triangulation $K'$ in which $K$ forms a subcomplex.

To obtain such a $K'$, we express each $vv' - \{v\}$ as the union of a countable collection of intervals $v_1v_2, v_2v_3, \ldots$, where $v = v_1$, and the points $v_i$ appear in the stated order on $vv' - \{v\}$, approaching $v'$ as a limit.

It remains to define $f'$. From $|K|$ we delete all end-points of $K$. The resulting space has a triangulation $H$ in which every simplex is a subsimplex of a simplex of $K$. Thus Theorem 7 applies to $H$ and $f||H|$. Let $h$ be as in Theorem 7, and for each edge $\sigma^1$ of $K$ let $e = h(f(\sigma^1))$. Thus each $e$ is either a broken line or an infinite polyhedron plus an end-point $w = h(f(v))$. This construction extends $f$ to $f'$ on $|K'|$.
