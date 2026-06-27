---
role: proof
locale: en
of_concept: direct-sum-and-tensor-product-of-collapsings
source_book: gtm020
source_chapter: "10. Relative K-Theory"
source_section: "1. Collapsing of Trivialized Bundles"
---

**Proof.** For the direct sum: The collapsing $(\xi \oplus \xi')/(t \oplus t')$ is defined by the quotient construction applied to $\xi \oplus \xi'$ with trivialization $t \oplus t'$ over $A$. On the other hand, $(\xi/t) \oplus (\xi'/t')$ is constructed by first collapsing each bundle individually and then taking the Whitney sum. The natural map
$$(\xi \oplus \xi')/(t \oplus t') \rightarrow (\xi/t) \oplus (\xi'/t')$$
induced by the quotient maps $u \oplus u'$ is a fibrewise linear isomorphism, hence an isomorphism of vector bundles. The verification uses that the quotient defining $(\xi \oplus \xi')/(t \oplus t')$ identifies fibres exactly when both components are identified, which matches the separate identifications in $(\xi/t) \oplus (\xi'/t')$.

For the tensor product: The same reasoning applies. The natural map
$$(\xi \otimes \xi')/(t \otimes t') \rightarrow (\xi/t) \otimes (\xi'/t')$$
induced by $u \otimes u'$ is a fibrewise linear isomorphism. The key point is that the identifications in the quotient $(\xi \otimes \xi')/(t \otimes t')$ correspond precisely to the tensor product of the identifications in $\xi/t$ and $\xi'/t'$, so the induced map is well-defined and bijective on fibres.
