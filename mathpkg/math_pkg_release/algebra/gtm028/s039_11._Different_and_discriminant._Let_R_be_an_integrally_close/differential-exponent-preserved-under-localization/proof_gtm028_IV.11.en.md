---
role: proof
locale: en
of_concept: differential-exponent-preserved-under-localization
source_book: gtm028
source_chapter: "IV"
source_section: "11. Different and discriminant"
---

Our assertion is equivalent to: the different of $R'_M$ over $R_M$ is the ideal $\prod_i \mathfrak{P}_i^{m(\mathfrak{P}_i)} R'_M$, where the $\mathfrak{P}_i$ denote the prime ideals of $R'$ lying over $\mathfrak{p}$; that is, the ideal $\mathfrak{D}_{R'/R} R'_M$.

We take any element $x$ of $\mathfrak{D}_{R'/R} R'_M$: $x = x'/m$ with $x' \in \mathfrak{D}$ and $m \in M$. If $z$ is an element of the complementary module of $R'_M$ (with respect to $R_M$), we have $T(z R'_M) \subset R_M$. In particular, for any $r' \in R'$, the element $T(z r')$ may be written in the form $r/m'$, with $r \in R$ and $m' \in M$, whence $T(m' z r') = r$ since $T(m' z r') = m' T(z r')$ as $m' \in K$. Since $R'$ is a finite $R$-module (Corollary 1 to Theorem 7 of §4), a common denominator $m' \in M$ may be found for all elements $T(z r')$ with $r' \in R'$. Thus $m' z$ belongs to the complementary module of $R'$, which gives the reverse inclusion $\mathfrak{C}_{R'_M/R_M} \subset \mathfrak{C}_{R'/R} R'_M$. Taking inverses yields $\mathfrak{D}_{R'_M/R_M} = \mathfrak{D}_{R'/R} R'_M$, and the equality of differential exponents follows.
