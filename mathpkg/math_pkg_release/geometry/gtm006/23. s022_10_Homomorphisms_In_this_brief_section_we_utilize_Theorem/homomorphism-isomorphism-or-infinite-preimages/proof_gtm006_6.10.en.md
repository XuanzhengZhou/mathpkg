---
role: proof
locale: en
of_concept: homomorphism-isomorphism-or-infinite-preimages
source_book: gtm006
source_chapter: "6"
source_section: "10. Homomorphisms"
---

Let $X_2, Y_2, O_2, I_2$ be a coordinatizing quadrangle for $\mathcal{P}_2$ (see Chapter V), and let $(R_2, T_2)$ be a planar ternary ring which corresponds to this quadrangle. Choose $X_1, Y_1, O_1, I_1$ in $\mathcal{P}_1$ such that $X_1^\phi = X_2$, $Y_1^\phi = Y_2$, $O_1^\phi = O_2$, $I_1^\phi = I_2$, and let $(R_1, T_1)$ be a planar ternary ring for $\mathcal{P}_1$ corresponding to this quadrangle choice. We use subscripts to distinguish coordinates in the two planes; e.g., $(x, y)_1$ is a point of $\mathcal{P}_1$, while $(u, v)_2$ is a point of $\mathcal{P}_2$.

Let $Z = \{ x \in R_1 \mid (x, 0)_1^\phi = (0, 0)_2 \}$ be the set of all first coordinates whose corresponding point on the $x$-axis maps to the origin of $\mathcal{P}_2$. Note that $0 \in Z$ (since $O_1^\phi = O_2$) and $1 \notin Z$ (since $I_1^\phi = I_2$ and $(1, 0)_1$ does not map to the origin). 

If $Z = \{0\}$, then the homomorphism $\phi$ is injective on coordinates: distinct coordinates in $\mathcal{P}_1$ map to distinct coordinates in $\mathcal{P}_2$. Since $\phi$ is surjective by hypothesis, this implies $\phi$ is bijective on both points and lines, hence an isomorphism of projective planes.

If $Z$ contains a nonzero element, then using the planar ternary ring structure one can show that $Z$ must be infinite. Specifically, for any $w \in R_1$ with $wz = 1$ for some $z \in Z$, the pre-image structure forces $Z$ to be in bijection with an infinite set. Consequently, the pre-image of $(0, 0)_2$ is infinite.

Now, using the homogeneity of the projective plane (any point can be mapped to any other by a collineation commuting appropriately with $\phi$), if the pre-image of one point is infinite, then the pre-image of every point is infinite. Similarly, the pre-image of every line is infinite.

Thus either $\phi$ is an isomorphism, or the pre-image of every element of $\mathcal{P}_2$ consists of infinitely many elements.
