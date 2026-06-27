---
role: proof
locale: en
of_concept: differential-of-multiplication-in-algebraic-group
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
Write $\mu^* f = \sum f_i \otimes g_i$, so $f(xy) = \sum f_i(x) g_i(y)$. In particular, evaluating at $e$ gives the identity
$$f = \sum g_i(e) f_i = \sum f_i(e) g_i.$$

For $(X, Y) \in \mathfrak{g} \oplus \mathfrak{g}$, the differential is given by
$$d\mu_{(e,e)}(X, Y)(f) = (X, Y)\left(\sum f_i \otimes g_i\right) = \sum X(f_i) g_i(e) + \sum f_i(e) Y(g_i).$$

Using the identity above, this equals $X(f) + Y(f)$, so $d\mu_{(e,e)}(X, Y) = X + Y$.
