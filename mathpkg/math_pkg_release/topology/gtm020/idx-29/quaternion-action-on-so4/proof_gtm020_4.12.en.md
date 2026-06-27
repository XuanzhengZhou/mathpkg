---
role: proof
locale: en
of_concept: quaternion-action-on-so4
source_book: gtm020
source_chapter: "4"
source_section: "12"
---

Since $r(x)1 = x1x^{-1} = 1$ and $r(x) = r(-x)$, the map $r$ factors through the projection $f: S^3 \to \mathbf{R}P^3$, giving the existence of $r'$ making the diagram commute. The map $g$ is the natural inclusion of $SO(4)$ into the space of maps that fix the vector $1 \in \mathbf{H}$, identifying $SO(3)$ with the stabilizer of $1$.

To show $r'$ is injective: if $r(x)y = y$ for all $y \in \mathbf{H}$, then $xy = yx$ for all $y \in \mathbf{H}$. This means $x$ lies in the center of $\mathbf{H}$, which is $\mathbf{R}$. Since $x \in S^3$, we have $x = \pm 1$, so the kernel of $r$ is $\{\pm 1\}$ and $r'$ is injective.

To show $r'$ is surjective: using the formula $r(\cos \theta + i \sin \theta) = j \cos 2\theta + k \sin 2\theta$ and the formulas obtained by cyclic permutations of $i, j, k$, the image of $r$ includes all rotations about the three axes $i, j,$ and $k$. Therefore the image of $r'$ is all of $SO(3)$.

Since $\mathbf{R}P^3$ is compact and $SO(3)$ is Hausdorff, $r'$ is a homeomorphism. The uniqueness follows from the fact that $f$ is a surjection.
