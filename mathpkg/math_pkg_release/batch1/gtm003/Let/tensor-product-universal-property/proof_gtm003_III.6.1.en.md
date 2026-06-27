---
role: proof
locale: en
of_concept: tensor-product-universal-property
source_book: gtm003
source_chapter: "III"
source_section: "6.1"
---

Let $f: E \times F \to G$ be a bilinear map. For each $(x, y) \in E \times F$, the mapping $f \mapsto f(x, y)$ is a linear form on $B(E, F)$, hence an element $u_{x,y}$ of $B(E, F)^*$. The canonical bilinear map is $\chi(x, y) = u_{x,y} =: x \otimes y$.

Define $\tilde{f}$ on the generators by $\tilde{f}(x \otimes y) = f(x, y)$ and extend linearly. This is well-defined because every element of $E \otimes F$ is a finite sum $\sum_i \lambda_i (x_i \otimes y_i)$, and the relations in $E \otimes F$ (bilinearity of $\otimes$) correspond exactly to the bilinearity relations satisfied by $f$. Concretely, if $\sum_i \lambda_i (x_i \otimes y_i) = 0$ in $E \otimes F$, then for any bilinear form on $E \times F$, the corresponding evaluation vanishes; since $f$ composed with any linear form on $G$ yields a bilinear form on $E \times F$, it follows that $\sum_i \lambda_i f(x_i, y_i) = 0$ in $G$, so $\tilde{f}$ is well-defined.

Uniqueness is immediate: any linear map $\tilde{g}$ satisfying $\tilde{g} \circ \chi = f$ must agree with $\tilde{f}$ on all generators $x \otimes y$, hence everywhere by linearity.

The mapping $\tilde{f} \mapsto \tilde{f} \circ \chi$ is clearly linear and injective (since $f = 0$ implies $\tilde{f} = 0$ on all generators), and surjective by the construction above. Hence it is a vector space isomorphism $L(E \otimes F, G) \cong B(E, F; G)$.
