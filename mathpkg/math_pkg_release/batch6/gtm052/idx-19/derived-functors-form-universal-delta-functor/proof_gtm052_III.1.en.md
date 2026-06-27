---
role: proof
locale: en
of_concept: derived-functors-form-universal-delta-functor
source_book: gtm052
source_chapter: "III"
source_section: "1"
---

For the first statement: by Theorem 1.1A, the derived functors $(R^i F)$ form a $\delta$-functor with $R^0 F \cong F$. For any $i > 0$ and any object $A$, since $\mathfrak{A}$ has enough injectives, there exists a monomorphism $u: A \hookrightarrow I$ with $I$ injective. By Theorem 1.1A(e), $R^i F(I) = 0$ for $i > 0$. In particular, the induced map $R^i F(u): R^i F(A) \to R^i F(I) = 0$ is the zero map, so $R^i F$ is effaceable for each $i > 0$. By Theorem 1.3A, $(R^i F)$ is a universal $\delta$-functor.

For the converse: if $T$ is a universal $\delta$-functor with $T^0 \cong F$, then by the universal property applied to the identity map $T^0 \to R^0 F \cong F$, there exists a unique morphism of $\delta$-functors $T \to (R^i F)$ extending this isomorphism. Conversely, the universal property of $T$ gives a morphism $(R^i F) \to T$. By uniqueness, these are inverse isomorphisms, so $T^i \cong R^i F$ for all $i$.
