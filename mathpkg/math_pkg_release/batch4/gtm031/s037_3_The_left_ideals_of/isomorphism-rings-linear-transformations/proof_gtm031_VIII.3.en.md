---
role: proof
locale: en
of_concept: isomorphism-rings-linear-transformations
source_book: gtm031
source_chapter: "VIII"
source_section: "3"
---
Let $\phi$ be an isomorphism of $\mathfrak{L}_1$ onto $\mathfrak{L}_2$ and let $\mathfrak{J}_1$ be a minimal right ideal in $\mathfrak{L}_1$. Then the image $\mathfrak{J}_2 = \mathfrak{J}_1\phi$ is a minimal right ideal in $\mathfrak{L}_2$. Let $\chi_i$ be an isomorphism of $\mathfrak{J}_i$ onto $\mathfrak{R}_i$ defined via the action on a vector $x_i$ (by Lemma 1, $x_i \mathfrak{J}_i = \mathfrak{R}_i$, and since $\mathfrak{J}_i$ is minimal, the kernel of $B \mapsto x_i B$ is $0$). Thus

$$A_{1r} = \chi_1 A_1 \chi_1^{-1}, \quad A_{2r} = \chi_2 A_2 \chi_2^{-1}$$

if $A_i \in \mathfrak{L}_i$, where $A_{ir}$ denotes the right multiplication by $A_i$ on $\mathfrak{J}_i$. Also $(B_1 A_1)\phi = (B_1\phi)(A_1\phi)$ if $B_1 \in \mathfrak{J}_1$. Hence $A_{1r}\phi = \phi(A_1\phi)_r$ where $A_1\phi$ denotes the image of $A_1$ under $\phi$. Thus

$$(A_1\phi)_r = \phi^{-1} A_{1r} \phi.$$

Combining these relations we obtain

$$A_1\phi = \chi_2^{-1}(A_1\phi)_r \chi_2 = \chi_2^{-1}\phi^{-1} A_{1r} \phi \chi_2.$$

Set $U = \chi_1 \phi \chi_2^{-1}$. Then $U$ is a 1-1 additive mapping of $\mathfrak{R}_1$ onto $\mathfrak{R}_2$. Moreover, for any $\alpha_1 \in \Delta_1$, let $\alpha_1 l$ denote the scalar multiplication by $\alpha_1$ as a linear transformation in $\mathfrak{L}_1$. Then $(\alpha_1 l)\phi$ is a linear transformation in $\mathfrak{L}_2$ which commutes with every element of $\mathfrak{L}_2$, hence is a scalar multiplication $\alpha_2 l$ for some $\alpha_2 \in \Delta_2$. The mapping $u: \alpha_1 \mapsto \alpha_2$ is an isomorphism of $\Delta_1$ onto $\Delta_2$.

For any $x_1 \in \mathfrak{R}_1$ and any $\alpha_1 \in \Delta_1$, we have

$$(\alpha_1 x_1)U = (x_1 \alpha_1 l)U = (x_1 U)(U^{-1} \alpha_1 l U) = (x_1 U)(\alpha_1^u l),$$

or

$$(\alpha_1 x_1)U = \alpha_1^u (x_1 U).$$

This equation shows that $\mathfrak{R}_1$ and $\mathfrak{R}_2$ have the same dimensionality. Let $(e_1, e_2, \ldots, e_n)$ be a basis for $\mathfrak{R}_1$ over $\Delta_1$. Then any $x = \sum \xi_i e_i$ with $\xi_i \in \Delta_1$. Hence $xU = \sum (\xi_i e_i)U = \sum \xi_i^u (e_i U)$, so the vectors $e_i U$ generate $\mathfrak{R}_2$ over $\Delta_2$. Moreover, if we have a relation $\sum \xi_i^u (e_i U) = 0$, then $(\sum \xi_i e_i)U = 0$, and since $U$ is 1-1, $\sum \xi_i e_i = 0$, forcing all $\xi_i = 0$ and consequently all $\xi_i^u = 0$. Thus the $e_i U$ form a basis for $\mathfrak{R}_2$ over $\Delta_2$, and the dimensions are equal.
