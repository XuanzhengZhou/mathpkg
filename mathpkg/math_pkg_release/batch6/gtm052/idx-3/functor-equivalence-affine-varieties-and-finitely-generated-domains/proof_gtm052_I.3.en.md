---
role: proof
locale: en
of_concept: functor-equivalence-affine-varieties-and-finitely-generated-domains
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

Immediate from Theorem 3.5. The assignment $X \mapsto A(X)$ is a contravariant functor from affine varieties to finitely generated integral $k$-domains: a morphism $\varphi: X \to Y$ induces a $k$-algebra homomorphism $\varphi^*: A(Y) \to A(X)$ by pullback, and this assignment respects composition and identities.

Theorem 3.5 shows this functor is fully faithful: every $k$-algebra homomorphism $A(Y) \to A(X)$ comes from a unique morphism $X \to Y$. Moreover, every finitely generated integral $k$-domain $R$ is isomorphic to $A(Y)$ for some affine variety $Y$ (indeed, write $R = k[x_1, \ldots, x_n]/\mathfrak{p}$ with $\mathfrak{p}$ prime and let $Y = Z(\mathfrak{p})$). Hence the functor is essentially surjective. Therefore it is an (arrow-reversing) equivalence of categories.
