---
role: proof
locale: en
of_concept: boundary-of-boundary-is-zero
source_book: gtm060
source_chapter: "7"
source_section: "35"
---
By the linearity of $\partial$, it suffices to prove that $\partial \partial D = 0$ for a convex $k$-dimensional polyhedron $D \subset \mathbb{R}^k$, since every cell is of the form $\sigma = (D, f, \text{Or})$, and boundaries are defined by restricting $f$.

Consider a convex oriented $k$-dimensional polyhedron $D$. Its boundary $\partial D$ is a $(k-1)$-chain consisting of the $(k-1)$-dimensional faces $D_i$ of $D$, each with an induced orientation from the outward normal rule.

Now compute $\partial \partial D = \sum_i \partial D_i$. Each $(k-1)$-dimensional face $D_i$ is itself a convex $(k-1)$-dimensional polyhedron, and its boundary $\partial D_i$ consists of its $(k-2)$-dimensional faces.

Consider any particular $(k-2)$-dimensional face $F$ of $D$. This face $F$ is the intersection of exactly two $(k-1)$-dimensional faces of $D$, say $D_i$ and $D_j$. In $\partial \partial D$, the face $F$ appears once as a face of $D_i$ and once as a face of $D_j$.

The crucial observation is that these two occurrences carry opposite signs. When $F$ is regarded as a face of $D_i$, its orientation is determined by taking an outward normal to $D_i$ within the hyperplane containing $D_i$, and then applying the outward-normal-to-$D$ rule from the definition. When $F$ is regarded as a face of $D_j$, a similar procedure applies. Because the outward normals to $D_i$ and $D_j$ point in opposite directions relative to the $(k-2)$-plane of $F$, the two induced orientations on $F$ are opposite.

Thus the two copies of $F$ in $\partial \partial D$ appear with opposite signs and cancel. Since every $(k-2)$-dimensional face of $D$ appears exactly twice in this way, $\partial \partial D = 0$.

By linear extension to chains, $\partial \partial c_k = 0$ for any $k$-chain $c_k$.
