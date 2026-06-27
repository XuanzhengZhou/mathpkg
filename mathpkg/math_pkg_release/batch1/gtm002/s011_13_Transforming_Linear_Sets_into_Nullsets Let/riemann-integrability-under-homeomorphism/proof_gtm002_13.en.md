---
role: proof
locale: en
of_concept: riemann-integrability-under-homeomorphism
source_book: gtm002
source_chapter: "13"
source_section: "Transforming Linear Sets into Nullsets"
---

Let $f$ be a bounded function on $I = [0,1]$ and let $D$ be its set of points of discontinuity. For any homeomorphism $h$ of $I$ onto itself, the composite function $f \circ h$ is bounded and has $h^{-1}(D)$ as its set of points of discontinuity. By Theorem 7.5, a bounded function is Riemann integrable if and only if it is continuous almost everywhere (i.e., its set of discontinuities is a nullset).

(a) Suppose $D$ is countable. Then $h^{-1}(D)$ is countable for every $h$, hence a nullset. Thus $f \circ h$ is Riemann integrable for all $h$. Conversely, if $f \circ h$ is Riemann integrable for all $h$, then in particular $f$ itself is Riemann integrable, so $D$ is a nullset. But if $D$ were uncountable, it would contain an uncountable closed set $C$. By a standard result (every uncountable closed set contains a perfect set of positive measure), there exists a homeomorphism $h$ such that $h^{-1}(C)$ has positive measure, contradicting that $f \circ h$ is Riemann integrable for all $h$. Hence $D$ must be countable.

(b) If $D$ is of first category, then by Theorem 13.1 there exists $h \in H$ such that $h^{-1}(D)$ is a nullset. Hence $f \circ h$ is Riemann integrable for this $h$. Conversely, suppose $f \circ h$ is Riemann integrable for some $h$. Then $h^{-1}(D)$ is a nullset. A nullset is of first category (Theorem 3.19), so $h^{-1}(D)$ is of first category. Since homeomorphisms preserve first category (as a topological invariant), $D = h(h^{-1}(D))$ is also of first category. On the other hand, if $D$ is of second category, then as an $F_\sigma$ set (Theorem 7.1), one of the closed sets of which it is the union must contain an interval. In this case $h^{-1}(D)$ also contains an interval and can never be a nullset, so $f \circ h$ is never Riemann integrable.

(c) For the identity $h$, $f \circ h = f$ is Riemann integrable if and only if $D$ is a nullset, directly by Theorem 7.5. $\square$
