---
role: proof
locale: en
of_concept: companion-matrix-of-cyclic-module
source_book: gtm049
source_chapter: "7"
source_section: "7.5"
---

Take the ordered basis $(a, af, \ldots, af^{s-1})$ of Proposition 3. In this basis, applying $f$ sends each basis vector to the next:

$$(af^{i-1})f = af^{i}, \quad i = 1, \ldots, s-1,$$

which accounts for the $1$'s on the superdiagonal. For the last basis vector, since $m_a(f)$ annihilates $a$, we have

$$af^{s} = a(d_1 f^{s-1} + d_2 f^{s-2} + \cdots + d_s),$$

so the last row of the matrix consists of the coefficients $d_s, d_{s-1}, \ldots, d_1$. Thus the matrix of $f$ in the ordered basis $(a, af, \ldots, af^{s-1})$ is precisely the companion matrix $B$.
