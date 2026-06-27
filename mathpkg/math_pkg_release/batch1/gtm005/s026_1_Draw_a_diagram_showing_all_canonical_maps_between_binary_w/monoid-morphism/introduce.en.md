---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A monoid morphism between two monoid objects $\langle c, \mu, \eta \rangle$ and $\langle c', \mu', \eta' \rangle$ in a monoidal category $B$ is an arrow $f: c \to c'$ that commutes with the multiplication and unit of the monoids. Specifically, applying the multiplication $\mu$ and then $f$ equals applying $f \otimes f$ and then $\mu'$, and the unit $\eta$ composed with $f$ equals $\eta'$. With these arrows, the monoids in $B$ form a category $\mathbf{Mon}_B$, with the forgetful functor $U: \mathbf{Mon}_B \to B$ sending each monoid to its underlying object.
