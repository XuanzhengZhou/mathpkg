---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This corollary to the rank-nullity theorem (Theorem 23) states that for a linear operator $T: V \to V$ on a finite-dimensional vector space, injectivity and surjectivity are equivalent properties: $T$ is one-to-one if and only if $T$ is onto. The proof follows immediately from the dimension formula: $\dim(V) = \dim(\ker T) + \dim(\operatorname{im} T)$. If $T$ is injective then $\ker T = \{0\}$, so $\dim(\operatorname{im} T) = \dim(V)$, giving $\operatorname{im} T = V$. Conversely, if $T$ is surjective then $\dim(\operatorname{im} T) = \dim(V)$, forcing $\dim(\ker T) = 0$ and thus $\ker T = \{0\}$.
