---
role: proof
locale: en
of_concept: corepresentation-of-vect-k
source_book: gtm020
source_chapter: "3"
source_section: "7"
---

The proof proceeds in two steps: establishing that $\phi_B$ is well-defined and natural, and then proving bijectivity.

First, for $[g] \in [B, G_k(F^\infty)]$, the induced bundle $g^*(\gamma_k)$ is a $k$-dimensional vector bundle over $B$, so $\phi_B([g]) = \{g^*(\gamma_k)\}$ is a well-defined element of $\operatorname{Vect}_k(B)$. If $g_0 \simeq g_1$ are homotopic maps, then $g_0^*(\gamma_k)$ and $g_1^*(\gamma_k)$ are $B$-isomorphic by the homotopy invariance of induced bundles (3(5.4) or 3(5.6)), so $\phi_B$ is well-defined on homotopy classes.

For naturality, let $f: B_1 \to B$ be a map. For any $[g] \in [B, G_k(F^\infty)]$, we have
$$
\operatorname{Vect}_k(f) \phi_B([g]) = \operatorname{Vect}_k(f)\{g^*(\gamma_k)\} = \{f^*g^*(\gamma_k)\} = \{(gf)^*(\gamma_k)\},
$$
and
$$
\phi_{B_1}([f], G_k(F^\infty))[g] = \phi_{B_1}([g] \circ [f]) = \phi_{B_1}([gf]) = \{(gf)^*(\gamma_k)\}.
$$
Thus $\phi$ is a natural transformation of cofunctors.

For surjectivity of $\phi_B$: every $k$-dimensional vector bundle over a paracompact space $B$ admits a Gauss map $g: E(\xi) \to F^\infty$ by (5.5), which determines a map $f: B \to G_k(F^\infty)$ with $f^*(\gamma_k) \cong \xi$ by (5.6). Hence $\phi_B([f]) = \{\xi\}$.

For injectivity of $\phi_B$: if $\phi_B([f]) = \phi_B([f_1])$, then $f^*(\gamma_k) \cong f_1^*(\gamma_k)$ as bundles over $B$. By the third homotopy classification theorem (6.2), the maps $f$ and $f_1$ are homotopic, so $[f] = [f_1]$.

Since each $\phi_B$ is a bijection and the family is natural, $\phi$ is a natural isomorphism.
