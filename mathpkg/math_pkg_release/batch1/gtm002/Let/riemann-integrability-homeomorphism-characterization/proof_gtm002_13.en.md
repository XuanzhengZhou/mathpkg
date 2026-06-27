---
role: proof
locale: en
of_concept: riemann-integrability-homeomorphism-characterization
source_book: gtm002
source_chapter: "13"
source_section: "13. Transforming Linear Sets into Nullsets"
---

Let $D$ be the set of points of discontinuity of $f$. For any homeomorphism $h$, $f \circ h$ has discontinuity set $h^{-1}(D)$. By Theorem 7.1, $D$ is an $F_\sigma$ set. By the Riemann-Lebesgue Theorem (Theorem 7.5), $f \circ h$ is Riemann integrable if and only if $h^{-1}(D)$ is a nullset.

(a) If $D$ is countable, then $h^{-1}(D)$ is countable and hence a nullset for every $h$. Conversely, if $D$ is uncountable, it contains an uncountable closed set. For some $h$, the set $h^{-1}(D)$ has positive measure (one can construct an $h$ that expands the uncountable closed set).

(b) If $D$ is of first category, by Theorem 13.1 there exists an $h$ such that $h^{-1}(D)$ is a nullset. Conversely, if $D$ is of second category, then one of the closed sets of which it is the union must contain an interval. In this case, $h^{-1}(D)$ also contains an interval and is never a nullset.

(c) This is precisely Theorem 7.5 — the Riemann-Lebesgue criterion.
