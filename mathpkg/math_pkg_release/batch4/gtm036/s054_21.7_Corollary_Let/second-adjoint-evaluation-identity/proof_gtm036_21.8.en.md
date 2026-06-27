---
role: proof
locale: en
of_concept: second-adjoint-evaluation-identity
source_book: gtm036
source_chapter: "21"
source_section: "21.8"
---

Using the definitions of adjoint and evaluation, we have, for each $x \in E$ and each $f \in F^*$,

$$
T^{**} \circ I_E(x)(f) = T^{**}(I_E(x))(f) = I_E(x) \circ T^*(f)
= I_E(x)(f \circ T) = (f \circ T)(x) = f(T(x)).
$$

On the other hand,

$$
I_F \circ T(x)(f) = I_F(T(x))(f) = f(T(x)).
$$

Since both expressions equal $f(T(x))$ for all $x \in E$ and all $f \in F^*$, we conclude $T^{**} \circ I_E = I_F \circ T$.
