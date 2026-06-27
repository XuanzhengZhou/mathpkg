---
role: proof
locale: en
of_concept: tensor-product-universal-property
source_book: gtm003
source_chapter: "III"
source_section: "6.1"
---

Since every element of $E \otimes F$ is a finite sum $\sum \lambda_i (x_i \otimes y_i)$, we define $\tilde{b}\bigl(\sum \lambda_i (x_i \otimes y_i)\bigr) = \sum \lambda_i \, b(x_i, y_i)$. This definition is unambiguous: if $\sum \lambda_i (x_i \otimes y_i) = 0$ in $E \otimes F$, then for every $f \in B(E, F)^*$ we have $\sum \lambda_i f(x_i, y_i) = 0$ by definition of $x_i \otimes y_i$ as the evaluation functional $f \mapsto \langle f, x_i \otimes y_i \rangle = f(x_i, y_i)$. Taking $f$ to be the bilinear form corresponding under the isomorphism $B(E, F; G) \cong L(E \otimes F, G)$ shows the definition is well-defined. The linearity of $\tilde{b}$ follows from the definition, and uniqueness is immediate since the elementary tensors $x \otimes y$ span $E \otimes F$. The isomorphism $L(E \otimes F, G) \cong B(E, F; G)$ follows directly from the universal property.
