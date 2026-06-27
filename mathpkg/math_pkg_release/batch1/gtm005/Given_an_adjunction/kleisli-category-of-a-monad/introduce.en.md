---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Kleisli category $X_T$ provides a canonical construction that recovers an adjunction from a given monad $\langle T, \eta, \mu \rangle$ on a category $X$. Its objects are formal symbols $x_T$ corresponding to objects of $X$, while its arrows $f^\flat : x_T \to y_T$ correspond to arrows $f : x \to Ty$ in $X$, with composition defined using the monad multiplication $\mu$. The resulting adjunction $F_T \dashv G_T$ between $X$ and $X_T$ reproduces the original monad $T$, demonstrating that every monad arises from an adjunction.
