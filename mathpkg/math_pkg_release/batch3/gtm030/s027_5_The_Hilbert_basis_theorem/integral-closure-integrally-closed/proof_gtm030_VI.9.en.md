---
role: proof
locale: en
of_concept: integral-closure-integrally-closed
source_book: gtm030
source_chapter: "VI"
source_section: "9. Integral elements"
---

Let $a$ be a $\mathfrak{G}$-integer and let
$$a^n = g_0 + g_1 a + \cdots + g_{n-1} a^{n-1}$$
where $g_i \in \mathfrak{G}$. Each $g_i$ is integral over $\mathfrak{g}$, so by the module criterion every power of each $g_i$ lies in some finitely generated $\mathfrak{g}$-submodule. An extension of the argument used in Theorem 7 shows that there exists a finitely generated $\mathfrak{g}$-submodule $(w_1, \dots, w_l)$ of $\mathfrak{A}$ that contains all monomials in the $g_i$'s.

Using the integral equation for $a$, every power of $a$ is expressible as a $\mathfrak{g}$-linear combination of $1, a, \dots, a^{n-1}$ with coefficients that are monomials in the $g_i$'s. Therefore every power of $a$ is contained in the finitely generated $\mathfrak{g}$-module
$$(w_1, \dots, w_l; w_1 a, \dots, w_l a; \dots; w_1 a^{n-1}, \dots, w_l a^{n-1}).$$

By Theorem 7 (module criterion), $a$ is a $\mathfrak{g}$-integer, i.e., $a \in \mathfrak{G}$. Thus $\mathfrak{G}$ is integrally closed in $\mathfrak{A}$.
