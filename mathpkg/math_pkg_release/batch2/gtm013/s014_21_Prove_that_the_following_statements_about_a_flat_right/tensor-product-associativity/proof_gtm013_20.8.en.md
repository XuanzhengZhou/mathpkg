---
role: proof
locale: en
of_concept: tensor-product-associativity
source_book: gtm013
source_chapter: "20"
source_section: "20.8"
---

For each $m \in M$, the map $\beta_m: W \times N \to (M \otimes_R W) \otimes_S N$ defined by $\beta_m(w, n) = (m \otimes_R w) \otimes_S n$ is $S$-balanced because

$$\beta_m(ws, n) = (m \otimes_R ws) \otimes_S n = (m \otimes_R w)s \otimes_S n = (m \otimes_R w) \otimes_S sn = \beta_m(w, sn).$$

Thus, for each $m \in M$ there is a unique homomorphism

$$v_m: W \otimes_S N \to (M \otimes_R W) \otimes_S N$$

such that $v_m(\sum_i w_i \otimes_S n_i) = \sum_i ((m \otimes_R w_i) \otimes_S n_i)$.

Now define $\gamma: M \times (W \otimes_S N) \to (M \otimes_R W) \otimes_S N$ by

$$\gamma(m, \sum_i w_i \otimes_S n_i) = v_m(\sum_i w_i \otimes_S n_i).$$

This map is $R$-balanced because $v_{m+m'} = v_m + v_{m'}$ and $v_{mr}(w \otimes n) = (mr \otimes w) \otimes n = (m \otimes rw) \otimes n = v_m(rw \otimes n)$. Hence there is a unique homomorphism

$$v: M \otimes_R (W \otimes_S N) \to (M \otimes_R W) \otimes_S N$$

such that $v(m \otimes_R (w \otimes_S n)) = (m \otimes_R w) \otimes_S n$.

Similarly, define $\mu: (M \otimes_R W) \otimes_S N \to M \otimes_R (W \otimes_S N)$ by $\mu((m \otimes_R w) \otimes_S n) = m \otimes_R (w \otimes_S n)$. Then $\mu \circ v$ and $v \circ \mu$ are identity maps on generators, so $v$ is an isomorphism with inverse $\mu$.

Naturality in $M$, $W$, and $N$ follows from the functoriality of the tensor product: given morphisms in any variable, the isomorphism commutes with the induced maps because both paths send a generator $m \otimes (w \otimes n)$ to the obvious image under the induced tensor product maps.
