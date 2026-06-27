---
role: proof
locale: en
of_concept: pointwise-kan-extension-characterization
source_book: gtm005
source_chapter: "X"
source_section: "5"
---

A right Kan extension $\operatorname{Ran}_K T$ is pointwise if it is preserved by all representable functors: for each $a \in A$,
$$A(a, \operatorname{Ran}_K T(-)) \cong \operatorname{Ran}_K (A(a, T(-))).$$

This is equivalent to the limit formula
$$(\operatorname{Ran}_K T)(c) = \varprojlim_{(c \downarrow K)} T \circ \Pi.$$

Proof ($\Rightarrow$): If representables preserve the Kan extension, then
$$A(a, (\operatorname{Ran}_K T)(c)) \cong (\operatorname{Ran}_K A(a, T(-)))(c) \cong \varprojlim_{(c \downarrow K)} A(a, T(\Pi(-))) \cong A(a, \varprojlim_{(c \downarrow K)} T \circ \Pi),$$
using that representables preserve limits. By Yoneda, $(\operatorname{Ran}_K T)(c) \cong \varprojlim_{(c \downarrow K)} T \circ \Pi$.

($\Leftarrow$) If the limit formula holds, then applying $A(a, -)$ preserves the limit (since hom preserves limits), yielding the pointwise condition.
