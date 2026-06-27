---
role: proof
locale: en
of_concept: universal-arrow-and-representable-functor
source_book: gtm005
source_chapter: "III"
source_section: "1"
---

A universal arrow $\langle r, u: c \to G(r) \rangle$ from $c$ to $G: D \to C$ yields a representation of $C(c, G(-)): D \to \mathbf{Set}$.

Proof: The universal property states: for every $f: c \to G(d)$, there exists a unique $f': r \to d$ with $G(f') \circ u = f$. Define $\phi_d: D(r, d) \to C(c, G(d))$ by $\phi_d(f') = G(f') \circ u$. The universal property states each $\phi_d$ is bijective. Naturality in $d$: for $h: d \to d'$, $\phi_{d'} \circ D(r, h) = C(c, G(h)) \circ \phi_d$ because both sides send $f': r \to d$ to $G(h \circ f') \circ u$. Thus $\phi$ is a natural isomorphism, so $(r, u)$ represents $C(c, G(-))$.

Conversely, a representation $\phi: D(r, -) \cong C(c, G(-))$ yields the universal arrow $u = \phi_r(1_r): c \to G(r)$.
