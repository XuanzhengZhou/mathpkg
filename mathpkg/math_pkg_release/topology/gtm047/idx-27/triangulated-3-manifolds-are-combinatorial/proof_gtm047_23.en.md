---
role: proof
locale: en
of_concept: triangulated-3-manifolds-are-combinatorial
source_book: gtm047
source_chapter: ""
source_section: "23"
---

Let $K$ be a triangulated 3-manifold, and let $M = |K|$.

(1) Every point of $M$ has arbitrarily small open neighborhoods $V \approx \mathbf{R}^3$. This follows from the definition of a 3-manifold.

(2) In a topological space, let $U$ be open, and let $V$ be a subset of $U$. If $U \approx \mathbf{R}^3$ and $V \approx \mathbf{R}^3$, then $V$ is open. This follows immediately from the Invariance of domain (Theorem 0.4).

(3) Every vertex $v$ of $K$ is such that $|\operatorname{St} v|$ is homeomorphic to $\mathbf{R}^3$.

(4) Every edge $e$ of $K$ lies in at least one 2-simplex $\sigma^2$ of $K$. Because the complement of a point in $\mathbf{R}^3$ is always connected.

(5) Every 2-simplex $\sigma^2$ of $K$ lies in at least one 3-simplex $\sigma^3$ of $K$. Suppose not. Adjoin to $K$ two 3-simplexes $\sigma^3_1$ and $\sigma^3_2$, having $\sigma^2$ as a face, such that $\sigma^3_1 \cap \sigma^3_2 = \sigma^2$ and $\sigma^3_i \cap M = \sigma^2$ for $i = 1, 2$. Let $U = I(\sigma^3_1 \cup \sigma^3_2)$, and let $V$ be an open neighborhood, in $M$, of a point of $\operatorname{Int} \sigma^2$, with $V \subset \operatorname{Int} \sigma^2 \subset U$ and $V \approx \mathbf{R}^3$. By (2), $V$ is open in $U$, which is false.

(6) Every 2-simplex $\sigma^2$ of $K$ lies in at least two 3-simplexes of $K$. Suppose not, and let $\sigma^3_1$ be the only 3-simplex of $K$ that contains $\sigma^2$. Adjoin to $K$ a 3-simplex $\sigma^3_2$, with $\sigma^2$ as a face, such that $\sigma^3_2 \cap M = \sigma^2$. Let $U = I(\sigma^3_1 \cup \sigma^3_2)$, and let $V$ be an open neighborhood of a point of $\operatorname{Int} \sigma^2$ (in $M$), such that $V \subset \operatorname{Int} \sigma^2 \cup I(\sigma^3_1) \subset U$ and $V \approx \mathbf{R}^3$. From (2) it follows that $V$ is open in $U$, which is false.

(7) Every 2-simplex $\sigma^2$ of $K$ lies in exactly two 3-simplexes of $K$.

(8) The link $L$ of each vertex $v$ is a closed 2-manifold.

(9) For each vertex $v$, $|L|$ is a topological 2-sphere.

(10) $|L|$ is simply connected. Take any point $P_0$ of $|L|$ as the base-point of $\pi(|L|)$, and let $p$ be a closed path in $|L|$ with base-point $P_0$. Let $f: [0, 1]^2 \rightarrow |\operatorname{St} v|$ be a contraction of $p$ in $|\operatorname{St} v|$. Let $U \approx \mathbf{R}^3$ be an open neighborhood of $v$, lying in $|\operatorname{St} v|$. Then $f$ can be chosen so that $v$ has a closed neighborhood $N$, lying in $U$, such that $N \cap |f|$ is a finite polyhedron, relative to Cartesian coordinates in $U$, and containing no 3-simplex. Therefore $f$ can be chosen so that $v \notin |f|$. Let $r: |\operatorname{St} v| - \{v\} \rightarrow |L|$ be the obvious retraction, mapping each set $vw - \{v\}$ ($w \in |L|$) onto $w$. Then $p \cong e$ in $|L|$, under the mapping $r(f): [0, 1]^2 \rightarrow |L|$.

(11) For each $v$, $|L|$ is a 2-sphere. Therefore $\operatorname{St} v$ is combinatorially equivalent to a 3-simplex.
