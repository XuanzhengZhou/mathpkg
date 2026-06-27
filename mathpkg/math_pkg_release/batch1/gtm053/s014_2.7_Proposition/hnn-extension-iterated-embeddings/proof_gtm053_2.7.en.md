---
role: proof
locale: en
of_concept: hnn-extension-iterated-embeddings
source_book: gtm053
source_chapter: "2"
source_section: "2.7"
---
(a) If the relations in $K_G$ implied a nontrivial relation between the $t_i$, this relation would be preserved in the quotient of $K_G$ by the smallest normal divisor containing $G$. But in this quotient the relations $t_i^{-1}\alpha_i(a)t_i = \beta_i(a)$ become trivial ($1 = 1$), and no restrictions are imposed on the $t_i$. Hence the $t_i$ freely generate a free subgroup.

For part (b), one first considers the case of finite $I$. In the context of the free product with amalgamation, the following intersection is taken in $(G * \langle u^n \rangle) * W(G * \langle v^n \rangle)$:

$$\left(H * \langle u^n \rangle\right) * W_0 \left(H * \langle v^n \rangle\right) \cap G * u^{-1} \alpha(A)u = H * u^{-1} \alpha(B)u,$$

so that intersecting further with $G$ yields $H$. It follows a fortiori that $K_H \cap G = H$.

The proof of (b) for finite $I$ proceeds by induction on $n = |I|$. For infinite $I$, one passes to the inductive limit (which here is a union). The details are left to the reader. The key point is verifying the conditions of Proposition 2.6(b) concerning the intersection of the amalgamation with the embedded subgroups.
