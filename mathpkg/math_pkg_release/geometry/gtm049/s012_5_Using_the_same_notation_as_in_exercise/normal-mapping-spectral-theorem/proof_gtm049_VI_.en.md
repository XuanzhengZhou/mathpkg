---
role: proof
locale: en
of_concept: normal-mapping-spectral-theorem
source_book: gtm049
source_chapter: "VI"
source_section: "6.5"
---
The proof proceeds by induction on $$\dim W$$. We observe that $$\sigma$$-symmetric mappings ($$f^* = f$$) and unitary mappings ($$ff^* = 1$$) are special cases of normal mappings.

By the fundamental theorem of algebra, the minimum polynomial of $$f$$ has a complex root $$x$$, so $$f$$ has an eigenvector. The adjoint $$f^*$$ has eigenvector with eigenvalue $$\bar{x}$$ for the same vector (by the normal property). Using the properties $$[w]f \subset [w] \Rightarrow [w]^\perp f \subset [w]^\perp$$ and its analogue for $$f^*$$, we can decompose:
$$W = [w] \oplus [w]^\perp$$
and apply the induction hypothesis to the restriction of $$f$$ to $$[w]^\perp$$. This yields a Cartesian basis of eigenvectors for all of $$W$$.
