---
role: proof
locale: en
of_concept: universal-arrow-to-representation
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

A universal arrow $\langle r, u: c \to G(r) \rangle$ from $c$ to $G: D \to C$ represents the functor $C(c, G(-)): D \to \mathbf{Set}$.

Proof: Define $\phi: D(r, -) \Rightarrow C(c, G(-))$ by $\phi_d(f') = G(f') \circ u$. The universal property states: for every $f: c \to G(d)$, there is a unique $f': r \to d$ with $G(f') \circ u = f$. This means $\phi_d$ is bijective. Naturality in $d$: for $h: d \to d'$, the square commutes because
$$\phi_{d'}(h \circ f') = G(h \circ f') \circ u = G(h) \circ G(f') \circ u = G(h) \circ \phi_d(f').$$
Thus $(r, u)$ is a universal element of $C(c, G(-))$ and $D(r, -) \cong C(c, G(-))$.
