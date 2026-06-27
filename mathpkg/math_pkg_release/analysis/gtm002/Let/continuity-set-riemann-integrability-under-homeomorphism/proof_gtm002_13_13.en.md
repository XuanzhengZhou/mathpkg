---
role: proof
locale: en
of_concept: continuity-set-riemann-integrability-under-homeomorphism
source_book: gtm002
source_chapter: "13"
source_section: "13"
---

Let $f$ be bounded on $[0,1]$ with discontinuity set $D$. For any automorphism $h$, the composite $f \circ h$ has discontinuity set $h^{-1}(D)$. By Theorem 7.5 (Lebesgue's criterion), $f \circ h$ is Riemann integrable iff $h^{-1}(D)$ is a nullset.

(a) If $D$ is countable, then $h^{-1}(D)$ is countable, hence a nullset, for every $h$. Conversely, if $f \circ h$ is integrable for all $h$, then by Theorem 13.1 (which provides an $h$ mapping any set of first category to a nullset), $D$ cannot be of first category unless it is countable. Since $D$ is $F_\sigma$ (Theorem 7.1), if it were uncountable it would contain an uncountable closed set, which can be mapped to a set of positive measure by some homeomorphism, contradicting integrability.

(b) If $D$ is of first category, Theorem 13.1 provides an $h$ such that $h^{-1}(D)$ is a nullset. Conversely, if $h^{-1}(D)$ is a nullset for some $h$, then $D = h(h^{-1}(D))$ is the homeomorphic image of a nullset. Homeomorphisms preserve first category (but not measure), so if $D$ were of second category, $h^{-1}(D)$ would also be of second category and could not be a nullset.

(c) This is precisely Lebesgue's criterion (Theorem 7.5): $f$ is Riemann integrable iff $D$ is a nullset.
