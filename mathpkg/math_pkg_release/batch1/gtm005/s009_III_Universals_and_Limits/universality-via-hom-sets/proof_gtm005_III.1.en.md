---
role: proof
locale: en
of_concept: universality-via-hom-sets
source_book: gtm005
source_chapter: "III"
source_section: "1"
---

A natural bijection $D(r, d) \cong C(c, G(d))$ (natural in $d$) is equivalent to a universal arrow $u: c \to G(r)$.

Proof ($\Rightarrow$): Given a natural isomorphism $\phi_d: D(r, d) \to C(c, G(d))$, set $u = \phi_r(1_r): c \to G(r)$. For any $f: c \to G(d)$, by surjectivity there exists $f': r \to d$ with $\phi_d(f') = f$. By naturality, $\phi_d(f') = G(f') \circ \phi_r(1_r) = G(f') \circ u$. Uniqueness follows from injectivity of $\phi_d$.

($\Leftarrow$): Given $u: c \to G(r)$ universal, define $\phi_d(f') = G(f') \circ u$. The universal property says each $\phi_d$ is bijective, and naturality holds as shown in the previous proof.
