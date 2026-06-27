---
role: proof
locale: en
of_concept: configuration-manifold-rigid-body
source_book: gtm060
source_chapter: "6"
source_section: "28"
---

Let $x_1, x_2,$ and $x_3$ be three points of the body which do not lie in a straight line. Consider the right-handed orthonormal frame whose first vector is in the direction of $x_2 - x_1$, and whose second is on the $x_3$ side in the $x_1x_2x_3$-plane (see Figure 112).

It follows from the conditions $|x_i - x_j| = r_{ij}$ (for $i = 1, 2, 3$) that the positions of all the points of the body are uniquely determined by the positions of $x_1, x_2,$ and $x_3$, which are given by the position of the orthonormal frame.

The position of the frame in space is determined by:
- The position of its origin $x_1 \in \mathbb{R}^3$ (3 degrees of freedom),
- The orientation of the frame, which is an element of the rotation group $\text{SO}(3)$ (3 degrees of freedom, since rotations preserve orthonormality and orientation).

The mapping from the body's configuration to $(\text{position of } x_1, \text{ orientation of frame})$ is a bijection onto $\mathbb{R}^3 \times \text{SO}(3)$, establishing the configuration manifold as the six-dimensional product manifold $\mathbb{R}^3 \times \text{SO}(3)$.
