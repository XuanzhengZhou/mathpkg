---
role: proof
locale: en
of_concept: acyclic-resolution-computes-derived-functors
source_book: gtm052
source_chapter: "III"
source_section: "1"
---

Let $J^\bullet$ be an $F$-acyclic resolution of $A$. Truncate $J^\bullet$ to obtain short exact sequences
$$0 \to Z^0 \to J^0 \to Z^1 \to 0,$$
$$0 \to Z^1 \to J^1 \to Z^2 \to 0,$$
and so on, where $Z^i = \ker(J^i \to J^{i+1})$. Note that $Z^0 \cong A$ and each $Z^i$ fits into a short exact sequence with $J^i$ and $Z^{i+1}$. Since $J^i$ is $F$-acyclic, the long exact sequence of derived functors yields isomorphisms
$$R^{j} F(Z^{i+1}) \cong R^{j+1} F(Z^i)$$
for all $j \geqslant 1$. By descending induction, one obtains
$$R^i F(A) \cong R^1 F(Z^{i-1}) \cong \cdots$$
and relates these to the cohomology of $F(J^\bullet)$. The naturality follows from the functoriality of the derived functors and the resolution. A complete proof can be found in Grothendieck [1, I, 2.2] or by applying the spectral sequence of a double complex to the resolution.
