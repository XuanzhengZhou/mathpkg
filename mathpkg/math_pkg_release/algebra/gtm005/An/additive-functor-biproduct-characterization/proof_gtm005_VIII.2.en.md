---
role: proof
locale: en
of_concept: additive-functor-biproduct-characterization
source_book: gtm005
source_chapter: "VIII"
source_section: "2"
---

Each of the equations $p_1 i_1 = 1, p_2 i_2 = 1$, and $i_1 p_1 + i_2 p_2 = 1$ describing a biproduct in terms of its injections $i_j$ and projections $p_j$ is preserved by an additive functor; therefore each additive functor preserves biproducts.

Conversely, suppose that $T$ preserves all binary biproducts. Then a parallel pair of arrows $f_1, f_2 : a \rightarrow a'$ has $T(f_1 \oplus f_2) = Tf_1 \oplus Tf_2$ and therefore $T(f_1 + f_2) = Tf_1 + Tf_2$ by the formula for sum in terms of direct sum and the equations

$$T(\delta_a) = \delta_{Ta}, \quad T(\check{\delta}_a) = \check{\delta}_{Ta},$$

which follow at once from the definition of the diagonal $\delta$ and the codiagonal $\check{\delta}$ in terms of product and coproduct.
