---
role: proof
locale: en
of_concept: dual-space-linear-functionals-right-vector-space
source_book: gtm006
source_chapter: "I"
source_section: "4. Vector Spaces"
---

The text states this result with the definitions of the operations but omits the detailed verification. To verify: for any $f', g' \in V'$, the sum $f' + g'$ defined by $v(f'+g') = vf' + vg'$ is linear because $(v+w)(f'+g') = (v+w)f' + (v+w)g' = vf' + wf' + vg' + wg' = v(f'+g') + w(f'+g')$ and $(kv)(f'+g') = (kv)f' + (kv)g' = k(vf') + k(vg') = k(v(f'+g'))$. Scalar multiplication $f'b$ defined by $v(f'b) = (vf')b$ preserves linearity in a similar fashion. The right-action axiom $(f'b)c = f'(bc)$ holds by associativity of multiplication in $K$. Thus $V'$ is a right vector space.
