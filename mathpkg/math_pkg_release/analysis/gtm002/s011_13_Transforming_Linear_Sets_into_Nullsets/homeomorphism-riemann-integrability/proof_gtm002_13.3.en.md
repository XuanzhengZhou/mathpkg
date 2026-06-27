---
role: proof
locale: en
of_concept: homeomorphism-riemann-integrability
source_book: gtm002
source_chapter: "13"
source_section: "13"
---

Let $f$ be bounded on $[0,1]$ with discontinuity set $D$, and let $h$ be a homeomorphism of $[0,1]$ onto itself. The composite $f \circ h$ is bounded and has discontinuity set $h^{-1}(D)$, because $h$ is a homeomorphism (preserves limits and continuity). By Theorem 7.5, a bounded function is Riemann integrable if and only if its set of discontinuities is a nullset. Hence $f \circ h$ is Riemann integrable precisely when $h^{-1}(D)$ is a nullset.

\textbf{(a)} If $D$ is countable, then $h^{-1}(D)$ is countable for every $h$, hence a nullset, so $f \circ h$ is Riemann integrable for all $h$. Conversely, if $f \circ h$ is Riemann integrable for all $h$, then in particular for $h = \text{id}$ we have $D$ is a nullset; and more strongly, if $h^{-1}(D)$ is a nullset for every homeomorphism $h$, then $D$ must be countable. For if $D$ were uncountable, it would contain a perfect (uncountable closed) subset $P$, and one can construct a homeomorphism $h$ such that $h^{-1}(P)$ has positive measure (by stretching an appropriate portion of $[0,1]$ to "spread out" $P$), contradicting that $h^{-1}(D)$ is always a nullset.

\textbf{(b)} If $D$ is of first category, then by Theorem 13.1 there exists a homeomorphism $h$ such that $h^{-1}(D)$ is a nullset, so $f \circ h$ is Riemann integrable for this $h$. Conversely, if $h^{-1}(D)$ is a nullset for some homeomorphism $h$, then $D = h(h^{-1}(D))$ is the homeomorphic image of a nullset. By Theorem 13.2 (the dual statement), any homeomorphic image of a nullset that is also an $F_\sigma$ set (and $D$ is an $F_\sigma$ by Theorem 7.1) must be of first category. Thus $D$ is of first category.

\textbf{(c)} If $D$ is a nullset, then $f \circ \text{id} = f$ is Riemann integrable by Theorem 7.5. Conversely, if $f$ is Riemann integrable, then $D$ is a nullset by Theorem 7.5. $\square$
