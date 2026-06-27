---
role: proof
locale: en
of_concept: universal-property-of-cartesian-product
source_book: gtm013
source_chapter: "0"
source_section: "0.4"
---

The proof is elementary and omitted in the text. Define $f: Y \to \prod X_{\alpha}$ by $f(y)(\alpha) = f_{\alpha}(y)$ for each $y \in Y$ and $\alpha \in A$. Then $\pi_{\alpha}(f(y)) = f(y)(\alpha) = f_{\alpha}(y)$, so $\pi_{\alpha} \circ f = f_{\alpha}$. Uniqueness follows from the observation that two elements $\sigma, \sigma'$ of the product are equal iff $\pi_{\alpha}(\sigma) = \pi_{\alpha}(\sigma')$ for all $\alpha \in A$.
