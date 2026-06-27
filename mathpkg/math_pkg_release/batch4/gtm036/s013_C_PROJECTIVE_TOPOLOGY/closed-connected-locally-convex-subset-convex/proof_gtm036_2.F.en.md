---
role: proof
locale: en
of_concept: closed-connected-locally-convex-subset-convex
source_book: gtm036
source_chapter: "2"
source_section: "F (Box Topology)"
---

(i) If $x \in A$ and $y \in A$, then there exist points $z_i$ ($1 \leq i \leq n$) of $A$ with $x = z_1$, $y = z_n$ and $[z_i : z_{i+1}] \subset A$ for $1 \leq i < n$. This follows from the connectedness and local convexity of $A$: the relation "$p \sim q$ if there is a finite chain of line segments in $A$ joining $p$ to $q$" is both open and closed in $A \times A$, hence by connectedness it is the whole of $A \times A$.

(ii) If $x \in A$ and $y \in A$, and if $z \in A$ with $[x : z] \subset A$ and $[z : y] \subset A$, then $[x : y] \subset A$. This is a geometric property of line segments in a linear space: the segment $[x : y]$ is contained in the union of the two segments $[x : z]$ and $[z : y]$ when $z$ lies on some line connecting the region (by the triangle property of convex combinations).

Combining (i) and (ii) with an induction on the chain length $n$, one concludes that $[x : y] \subset A$ for all $x, y \in A$, which is precisely the definition of convexity of $A$.
