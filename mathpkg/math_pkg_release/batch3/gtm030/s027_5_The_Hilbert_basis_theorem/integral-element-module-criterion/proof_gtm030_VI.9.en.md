---
role: proof
locale: en
of_concept: integral-element-module-criterion
source_book: gtm030
source_chapter: "VI"
source_section: "9. Integral elements"
---

First suppose $a$ satisfies an equation $a^n = g_0 + g_1 a + \cdots + g_{n-1} a^{n-1}$ with $g_i \in \mathfrak{g}$. Then by induction, every power $a^m$ is expressible as a $\mathfrak{g}$-linear combination of $1, a, \dots, a^{n-1}$. Hence all powers of $a$ lie in the finitely generated $\mathfrak{g}$-module $(1, a, \dots, a^{n-1})$.

Conversely, suppose all powers of $a$ are contained in a finitely generated $\mathfrak{g}$-module $\mathfrak{N}$. Since $\mathfrak{g}$ is Noetherian, $\mathfrak{N}$ satisfies the ascending chain condition for submodules. Consider the ascending chain
$$(1) \subseteq (1, a) \subseteq (1, a, a^2) \subseteq \cdots$$
in $\mathfrak{N}$. By the chain condition, there exists $n$ such that $(1, a, \dots, a^{n-1}) = (1, a, \dots, a^n)$. Thus $a^n \in (1, a, \dots, a^{n-1})$, which gives an integral dependence relation for $a$ over $\mathfrak{g}$.
