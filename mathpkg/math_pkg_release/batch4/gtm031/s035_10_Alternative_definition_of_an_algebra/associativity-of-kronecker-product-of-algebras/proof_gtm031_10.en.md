---
role: proof
locale: en
of_concept: associativity-of-kronecker-product-of-algebras
source_book: gtm031
source_chapter: ""
source_section: "10. Alternative definition of an algebra"
---

Let $a = \Sigma x_1 \times x_2$, $b = \Sigma y_1 \times y_2$, $c = \Sigma z_1 \times z_2$ be elements of $\mathfrak{A}_1 \times \mathfrak{A}_2$. Using formula (38):

$$(ab)c = (\Sigma x_1y_1 \times x_2y_2)(\Sigma z_1 \times z_2) = \Sigma (x_1y_1)z_1 \times (x_2y_2)z_2$$

$$a(bc) = (\Sigma x_1 \times x_2)(\Sigma y_1z_1 \times y_2z_2) = \Sigma x_1(y_1z_1) \times x_2(y_2z_2).$$

Since $\mathfrak{A}_1$ and $\mathfrak{A}_2$ are associative, $(x_1y_1)z_1 = x_1(y_1z_1)$ and $(x_2y_2)z_2 = x_2(y_2z_2)$. Hence $(ab)c = a(bc)$, proving associativity of the Kronecker product.
