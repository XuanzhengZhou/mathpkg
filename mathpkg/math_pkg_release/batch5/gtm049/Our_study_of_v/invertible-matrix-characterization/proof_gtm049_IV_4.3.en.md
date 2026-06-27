---
role: proof
locale: en
of_concept: invertible-matrix-characterization
source_book: gtm049
source_chapter: "IV"
source_section: "4.3"
---
A square matrix $$A \in F^{n \times n}$$ is invertible if and only if the corresponding linear mapping $$f: F^n \to F^n$$ (defined by $$x \mapsto xA$$) is an isomorphism. An isomorphism of finite-dimensional vector spaces is characterized by being one-one or onto. By the dimension theorem, $$f$$ is one-one iff $$\dim \ker f = 0$$, and $$f$$ is onto iff $$\dim \operatorname{im} f = n$$. Both conditions are equivalent to the rows (or columns) of $$A$$ being linearly independent, which is equivalent to $$\det A \neq 0$$ over any field (or, in elementary terms, $$A$$ having a two-sided inverse).
