---
role: proof
locale: en
of_concept: isomorphism-semilinear-transformation
source_book: gtm031
source_chapter: "VIII"
source_section: "3"
---
The proof is a direct consequence of the construction in the proof of Theorem 7. Let $\phi$ be an isomorphism of $\mathfrak{L}_1$ onto $\mathfrak{L}_2$. Choose a minimal right ideal $\mathfrak{J}_1$ in $\mathfrak{L}_1$ and let $\mathfrak{J}_2 = \mathfrak{J}_1\phi$. Using Lemma 1, the action on a suitable vector $x_i$ gives isomorphisms $\chi_i: \mathfrak{J}_i \to \mathfrak{R}_i$ of right $\mathfrak{L}_i$-modules.

Define $U = \chi_1 \phi \chi_2^{-1}$. Then $U: \mathfrak{R}_1 \to \mathfrak{R}_2$ is a 1-1 additive mapping onto $\mathfrak{R}_2$. From the proof of Theorem 7, the mapping $u: \Delta_1 \to \Delta_2$ given by $(\alpha_1 l)\phi = \alpha_1^u l$ is an isomorphism of division rings, and for any $x_1 \in \mathfrak{R}_1$, $\alpha_1 \in \Delta_1$,
$$(\alpha_1 x_1)U = \alpha_1^u (x_1 U).$$
Thus $U$ is a semilinear transformation with associated isomorphism $u$.

For any $A_1 \in \mathfrak{L}_1$, the construction gives
$$A_1\phi = \chi_2^{-1} \phi^{-1} A_{1r} \phi \chi_2 = U^{-1} A_1 U,$$
since $A_{1r} = \chi_1 A_1 \chi_1^{-1}$ and $U = \chi_1 \phi \chi_2^{-1}$. This completes the proof.
