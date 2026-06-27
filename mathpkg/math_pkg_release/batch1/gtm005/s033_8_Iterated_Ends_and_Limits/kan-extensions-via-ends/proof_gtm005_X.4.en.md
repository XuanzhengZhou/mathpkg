---
role: proof
locale: en
of_concept: kan-extensions-via-ends
source_book: gtm005
source_chapter: "X"
source_section: "4"
---

The right Kan extension can be expressed as an end:
$$(\operatorname{Ran}_K T)(c) = \int_{m \in M} \mathbf{Set}(C(c, K(m)), T(m))$$
(using the power/cotensor, written $X \pitchfork A$ for $A^X$ in $A$ if powers exist).

Proof: By definition, $\operatorname{Ran}_K T$ is characterized by
$$A(a, (\operatorname{Ran}_K T)(c)) \cong \operatorname{Nat}_M(C(c, K(-)), A(a, T(-))).$$
A natural transformation $C(c, K(-)) \Rightarrow A(a, T(-))$ consists of maps $\phi_m: C(c, K(m)) \to A(a, T(m))$ natural in $m$. By the universal property of the end,
$$\{ \phi_m \}_m \in \int_m \mathbf{Set}(C(c, K(m)), A(a, T(m))) \cong A\left(a, \int_m \mathbf{Set}(C(c, K(m)), T(m))\right),$$
assuming the end in $A$ exists. The Yoneda Lemma then gives the formula for $\operatorname{Ran}_K T$.

Dually, $(\operatorname{Lan}_K T)(c) = \int^m C(K(m), c) \cdot T(m)$ (using copower/copower notation).
