---
role: proof
locale: en
of_concept: affine-varieties-isomorphic-iff-coordinate-rings-isomorphic
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

Immediate from Theorem 3.5. If $\varphi: X \to Y$ is an isomorphism with inverse $\psi: Y \to X$, then the induced maps $h: A(Y) \to A(X)$ and $h': A(X) \to A(Y)$ satisfy $h \circ h' = \mathrm{id}_{A(X)}$ and $h' \circ h = \mathrm{id}_{A(Y)}$, so $A(X) \cong A(Y)$ as $k$-algebras.

Conversely, if $h: A(Y) \to A(X)$ is a $k$-algebra isomorphism, then by Theorem 3.5 it comes from a unique morphism $\varphi: X \to Y$, and its inverse $h^{-1}: A(X) \to A(Y)$ comes from a unique morphism $\psi: Y \to X$. The composition $\psi \circ \varphi$ corresponds to $h \circ h^{-1} = \mathrm{id}$, hence equals $\mathrm{id}_X$, and similarly $\varphi \circ \psi = \mathrm{id}_Y$. Thus $\varphi$ is an isomorphism.
