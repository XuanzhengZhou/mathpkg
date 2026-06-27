---
role: proof
locale: en
of_concept: canonical-isomorphism-pullback-associated-bundle
source_book: gtm020
source_chapter: "6"
source_section: "6.3"
---

The total space $X_1$ of $f^*(\xi[F])$ consists of pairs $(b_1, (x, y)G)$, where $f(b_1) = p_F((x, y)G) = p(x)$, and the morphism $f_{\xi[F]}$ is given by $f_{\xi[F]}(b_1, (x, y)G) = (x, y)G$.

The total space $X_2$ of $f^*(\xi)[F]$ consists of pairs $((b_1, x), y)G$, where $f(b_1) = p(x)$, and the morphism $(f_{\xi})_F$ is given by $(f_{\xi})_F(((b_1, x), y)G) = (x, y)G$.

Define the isomorphism $g$ by
$$g(b_1, (x, y)G) = ((b_1, x), y)G.$$
This map is well-defined because if $(x, y)G = (x', y')G$, then there exists $s \in G$ with $x' = xs$ and $y' = s^{-1}y$, and $(b_1, x') = (b_1, xs)$ implies $((b_1, x'), y')G = ((b_1, xs), s^{-1}y)G = ((b_1, x), y)G$. The isomorphism arises from applying the quotient space functor to the canonical $G$-isomorphism $B_1 \times (X \times F) \to (B_1 \times X) \times F$ given by $(b_1, (x, y)) \mapsto ((b_1, x), y)$.

The factorization $f_{\xi[F]} = (f_{\xi})_F \circ g$ follows directly from the definitions, since
$$(f_{\xi})_F(g(b_1, (x, y)G)) = (f_{\xi})_F(((b_1, x), y)G) = (x, y)G = f_{\xi[F]}(b_1, (x, y)G).$$
