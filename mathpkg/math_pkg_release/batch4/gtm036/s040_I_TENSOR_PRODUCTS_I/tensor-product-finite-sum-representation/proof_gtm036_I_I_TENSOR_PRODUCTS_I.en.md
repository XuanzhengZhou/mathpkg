---
role: proof
locale: en
of_concept: tensor-product-finite-sum-representation
source_book: gtm036
source_chapter: "I"
source_section: "I TENSOR PRODUCTS I"
---

By definition, $E \otimes F$ is the linear subspace of $B(E', F')$ spanned by $k(E, F) = \{x \otimes y : x \in E, y \in F\}$. Every element of the linear span of a set is, by definition, a finite linear combination of elements of that set. Thus any $z \in E \otimes F$ can be written as
$$z = \sum_{i=1}^{n} \alpha_i (x_i \otimes y_i)$$
for some scalars $\alpha_i$ and vectors $x_i \in E$, $y_i \in F$. Since $x \otimes y$ is bilinear in $(x, y)$, we may absorb the scalar $\alpha_i$ into either $x_i$ or $y_i$ (replacing $x_i$ with $\alpha_i x_i$ or $y_i$ with $\alpha_i y_i$), yielding the representation
$$z = \sum_{i=1}^{n} x_i \otimes y_i.$$

For any $(x', y') \in E' \times F'$, evaluating this bilinear form gives
$$z(x', y') = \left(\sum_{i=1}^{n} x_i \otimes y_i\right)(x', y') = \sum_{i=1}^{n} (x_i \otimes y_i)(x', y') = \sum_{i=1}^{n} \langle x_i, x' \rangle \langle y_i, y' \rangle,$$
where the last equality follows from the definition $(x \otimes y)(x', y') = \langle x, x' \rangle \langle y, y' \rangle$.
