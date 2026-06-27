---
role: proof
locale: en
of_concept: isomorphism-semilinear-transformation
source_book: gtm031
source_chapter: "VIII"
source_section: "5"
---

Let $\phi$ be an isomorphism of $\mathfrak{L}_1$ onto $\mathfrak{L}_2$ and let $\mathfrak{J}_1$ be a minimal right ideal in $\mathfrak{L}_1$. Then the image $\mathfrak{J}_2 = \mathfrak{J}_1\phi$ is a minimal right ideal in $\mathfrak{L}_2$. Let $\chi_i$ be an isomorphism of $\mathfrak{J}_i$ onto $\mathfrak{R}_i$ defined by choosing a vector $x_i$ such that $x_i\mathfrak{J}_i \neq 0$ and setting $B\chi_i = x_i B$. Then
$$A_{1r} = \chi_1 A_1 \chi_1^{-1}, \quad A_{2r} = \chi_2 A_2 \chi_2^{-1}$$
if $A_i \in \mathfrak{L}_i$. Also $(B_1 A_1)\phi = (B_1\phi)(A_1\phi)$ if $B_1 \in \mathfrak{J}_1$. Hence $A_{1r}\phi = \phi(A_1\phi)_r$. Thus
$$(A_1\phi)_r = \phi^{-1} A_{1r} \phi.$$
Combining these equations we obtain
$$A_1\phi = \chi_2^{-1}(A_1\phi)_r \chi_2 = \chi_2^{-1} \phi^{-1} A_{1r} \phi \chi_2.$$
Set $U = \chi_1^{-1} \phi \chi_2$. Then $U$ is a 1-1 additive mapping of $\mathfrak{R}_1$ onto $\mathfrak{R}_2$, and we have $A_1\phi = U^{-1} A_1 U$. Moreover, $U$ determines an isomorphism $u: \Delta_1 \to \Delta_2$ such that $(\alpha x)U = \alpha^u(xU)$ for all $\alpha \in \Delta_1$, $x \in \mathfrak{R}_1$. Thus $U$ is a semilinear transformation. The fact that $U$ is 1-1 and onto follows from the corresponding properties of $\phi$, $\chi_1$, and $\chi_2$.
