---
role: proof
locale: en
of_concept: product-convexity-characterization
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Characterization of convexity in product spaces

Let $E = \prod_{\iota \in I} E_\iota$ be the product vector space and $A = \prod_{\iota \in I} A_\iota$ with $A_\iota \subset E_\iota$. If $A$ is convex, then for every $\iota \in I$, $A_\iota = \pi_\iota(A)$ is convex by (25.6)(i). Conversely, if every $A_\iota$ is convex then, by (25.6)(ii), $\pi_\iota^{-1}(A_\iota)$ is convex for all $\iota \in I$, therefore

$$A = \bigcap_{\iota \in I} \pi_\iota^{-1}(A_\iota)$$

is also convex by (25.3) (the intersection of convex sets is convex).
