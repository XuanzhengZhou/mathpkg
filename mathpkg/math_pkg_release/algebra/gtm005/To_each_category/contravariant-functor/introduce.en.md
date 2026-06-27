---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A contravariant functor $\bar{S}: C \to B$ is a mapping that reverses the direction of arrows: it assigns to each object of $C$ an object of $B$ and to each arrow $f: a \to b$ in $C$ an arrow $\bar{S}f: \bar{S}b \to \bar{S}a$ in $B$, respecting identities and composition with reversal. Rather than treating contravariant functors as a separate notion, Mac Lane defines them uniformly as ordinary covariant functors from the opposite category: $S: C^{\text{op}} \to B$. This convention simplifies the general theory by reducing all functors to the covariant case, with the opposite category absorbing the direction reversal.
