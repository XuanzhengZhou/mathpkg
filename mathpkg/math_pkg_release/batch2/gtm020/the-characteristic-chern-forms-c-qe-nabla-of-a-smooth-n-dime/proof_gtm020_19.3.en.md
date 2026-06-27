---
locale: en
of_concept: the-characteristic-chern-forms-c-qe-nabla-of-a-smooth-n-dime
role: proof
source_book: gtm020
source_chapter: 19. Characteristic Classes and Connections
source_section: '3'
---

Firstly, we calculate using the derivation property of $\alpha \mapsto [\theta, \alpha]$ on even forms $\alpha$

$$d \text{Tr}(K^q) = \sum_{i+j=q-1} \text{Tr}(K^i(dK)K^j)$$

we have the relation $c_1(X) = \text{Tr}(X)$ corresponding to the sum of the eigenvalues. Another relation is

$$\text{Tr}(X^2) = c_1(X)^2 - 2c_2(X).$$

This can be seen by squaring the sum of the eigenvalues and subtracting off the sum of products of distinct eigenvalues. In the case of $n = 2$, the Hamilton-Cayley theorem says that

$$X^2 - \text{Tr}(X)X + \det(X)I = 0,$$

and taking the trace of this relation, we obtain

$$\text{Tr}(X^2) = \text{Tr}(X)^2 - 2\det(X)$$

which is another version of this relation. This leads to another interesting characteristic class of bundles

$$a_2(E) = c_1(E)^2 - 2c_2(E).$$

4. Homotopy Properties of Connections and Curvature
