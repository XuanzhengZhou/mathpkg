---
role: proof
locale: en
of_concept: thom-space-product-homeomorphic-to-smash-product
source_book: gtm020
source_chapter: "16"
source_section: "1"
---

The space $T(\xi \times \eta)$ is the one-point compactification of $E(\xi \times \eta)$ and $T(\xi) \wedge T(\eta)$ is the one-point compactification of $E(\xi) \times E(\eta)$. The result follows from the equality $E(\xi \times \eta) = E(\xi) \times E(\eta)$.

For the more general construction, the map
$$f: (D(\xi \times \eta), S(\xi \times \eta)) \rightarrow (D(\xi) \times D(\eta), S(\xi) \times D(\eta) \cup D(\xi) \times S(\eta))$$
defined by
$$f(x, y) = \left( \max \left( \|x\|, \|y\| \right) \right)^{-1} \left( \|x\|^2 + \|y\|^2 \right)^{-1/2}(x, y)$$
provides a homeomorphism of pairs, which upon passage to quotients yields the required homeomorphism $T(\xi \times \eta) \rightarrow T(\xi) \wedge T(\eta)$.
