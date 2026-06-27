---
role: proof
locale: en
of_concept: construction-of-anti-isomorphic-ring
source_book: gtm030
source_chapter: "III"
source_section: "9"
---

*Proof.* We first verify that $(\mathfrak{A}, +, \times)$ satisfies the ring axioms. Addition remains unchanged and forms an abelian group. For associativity of $\times$:
\begin{align*}
(a \times b) \times c &= (b \cdot a) \times c = c \cdot (b \cdot a) = (c \cdot b) \cdot a, \\
a \times (b \times c) &= (b \times c) \cdot a = (c \cdot b) \cdot a.
\end{align*}
Thus $(a \times b) \times c = a \times (b \times c)$. For distributivity:
\begin{align*}
a \times (b + c) &= (b + c) \cdot a = b \cdot a + c \cdot a = a \times b + a \times c, \\
(b + c) \times a &= a \cdot (b + c) = a \cdot b + a \cdot c = b \times a + c \times a.
\end{align*}
Therefore $(\mathfrak{A}, +, \times)$ is a ring.

The identity mapping $\iota$ satisfies $\iota(a + b) = a + b = \iota(a) + \iota(b)$ and $\iota(a \times b) = b \cdot a = \iota(b) \cdot \iota(a)$, which are precisely the conditions for an anti-isomorphism. Moreover, $\iota$ is bijective, so it is an anti-isomorphism.
