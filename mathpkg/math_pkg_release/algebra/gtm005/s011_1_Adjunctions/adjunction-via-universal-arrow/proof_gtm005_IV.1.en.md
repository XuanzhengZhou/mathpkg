---
role: proof
locale: en
of_concept: adjunction-via-universal-arrow
source_book: gtm005
source_chapter: "IV"
source_section: "1"
---

Given $G: C \to D$, if for each $d \in D$ there exists an object $F(d) \in C$ and a universal arrow $\eta_d: d \to G(F(d))$ from $d$ to $G$, then $F$ extends uniquely to a functor left adjoint to $G$.

For $f: d \to d'$, compose $\eta_{d'} \circ f: d \to G(F(d'))$. By universality of $\eta_d$, there is a unique $F(f): F(d) \to F(d')$ with $G(F(f)) \circ \eta_d = \eta_{d'} \circ f$.

Functoriality: $F(1_d)$ is the unique arrow satisfying $G(F(1_d)) \circ \eta_d = \eta_d$, so $F(1_d) = 1_{F(d)}$ by uniqueness (since $G(1_{F(d)}) \circ \eta_d = \eta_d$). For $g: d' \to d''$, $F(g \circ f)$ and $F(g) \circ F(f)$ both satisfy the same defining equation, hence are equal by uniqueness.

The adjunction isomorphism is $\varphi_{d,c}(h) = G(h) \circ \eta_d$, which is bijective by the universal property.
