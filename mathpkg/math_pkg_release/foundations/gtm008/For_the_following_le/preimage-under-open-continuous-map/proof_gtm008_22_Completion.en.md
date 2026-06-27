---
role: proof
locale: en
of_concept: preimage-under-open-continuous-map
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

**1.** Let $x \in (f^{-1})``(B^{-})$. Then $f(x) \in B^{-}$, and hence for every open neighborhood $N(f(x))$ in $Y$,
$$N(f(x)) \cap B \neq 0.$$

Since $f$ is open and continuous, for every open neighborhood $N(x)$ in $X$, the image $f``N(x)$ is an open neighborhood of $f(x)$ in $Y$. Therefore
$$f``N(x) \cap B \neq 0,$$
which implies $N(x) \cap (f^{-1})``B \neq 0$. Hence $x \in ((f^{-1})``B)^{-}$.

Conversely, let $x \in ((f^{-1})``B)^{-}$. Then for every $N(x)$, $N(x) \cap (f^{-1})``B \neq 0$. Taking images under $f$, for every $N(f(x))$, continuity of $f$ gives $N(f(x)) \cap B \neq 0$, so $f(x) \in B^{-}$ and $x \in (f^{-1})``(B^{-})$.

**2.** Follows from 1 by taking complements: $B^0 = Y - (Y - B)^{-}$ and similarly in $X$.
