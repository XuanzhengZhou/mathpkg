---
role: proof
locale: en
of_concept: substructure-term-evaluation
source_book: gtm037
source_chapter: "19"
source_section: "Elementary Equivalence"
---
The proof proceeds by induction on the structure of the term $\sigma$. If $\sigma$ is a variable, the result is immediate from the assignment $x$. If $\sigma = \mathbf{O}(\sigma_0, \ldots, \sigma_{m-1})$ for an $m$-ary operation symbol $\mathbf{O}$, then by the induction hypothesis, $\sigma_i^{\mathfrak{A}}(x) = \sigma_i^{\mathfrak{B}}(x)$ for each $i < m$. Since $\mathfrak{A} \subseteq \mathfrak{B}$, we have $\mathbf{O}^{\mathfrak{A}} = \mathbf{O}^{\mathfrak{B}} \upharpoonright {}^m A$, hence $\mathbf{O}^{\mathfrak{A}}(\sigma_0^{\mathfrak{A}}(x), \ldots, \sigma_{m-1}^{\mathfrak{A}}(x)) = \mathbf{O}^{\mathfrak{B}}(\sigma_0^{\mathfrak{B}}(x), \ldots, \sigma_{m-1}^{\mathfrak{B}}(x))$. This completes the induction.

[Note: The full proof text in the source section was truncated. The above is a standard reconstruction.]
