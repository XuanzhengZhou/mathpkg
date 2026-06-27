---
role: proof
locale: en
of_concept: theorem-7-isomorphism-dense-rings
source_book: gtm031
source_chapter: "IX"
source_section: "11"
---
Choose a minimal right ideal $\mathfrak{J}_1$ in $\mathfrak{A}_1$ and let $\mathfrak{J}_2 = \mathfrak{J}_1 \phi$. Let $\psi_i$ be an operator isomorphism of $\mathfrak{J}_i$ into $\mathfrak{R}_i$, determined as in the theory of primitive rings (cf. \S 5, Chapter VIII). Then the mapping $U = \psi_1^{-1} \phi \psi_2$ is a $1$-$1$ semi-linear transformation of $\mathfrak{R}_1$ onto $\mathfrak{R}_2$, and
$$A_1 \phi = U^{-1} A_1 U$$
holds for all $A_1 \in \mathfrak{A}_1$. In particular, the base division rings $\Delta_1$ and $\Delta_2$ are isomorphic, and $\mathfrak{R}_1$ and $\mathfrak{R}_2$ have the same dimensionality.

It remains to verify that the transpose $U^*$ maps $\mathfrak{R}_2'$ onto $\mathfrak{R}_1'$. For any semi-linear transformation $S: \mathfrak{R}_1 \to \mathfrak{R}_2$ with associated isomorphism $s: \Delta_1 \to \Delta_2$, the transpose $S^*: \mathfrak{R}_2^* \to \mathfrak{R}_1^*$ is defined by $S^*(f) = s^{-1} \circ f \circ S$ for $f \in \mathfrak{R}_2^*$. Since $U$ has the property that for any $F_2 \in \mathfrak{J} \cap \mathfrak{A}_2$, the conjugate $U F_2 U^{-1} \in \mathfrak{J} \cap \mathfrak{A}_1$, we obtain
$$\mathfrak{R}_2' U^* = \sum \mathfrak{R}_2^* F_2^* U^* = \sum \mathfrak{R}_2^* U^* F_1^* = \sum \mathfrak{R}_1^* F_1^* = \mathfrak{R}_1'.$$
Thus $U^*$ maps $\mathfrak{R}_2'$ onto $\mathfrak{R}_1'$, completing the proof.
