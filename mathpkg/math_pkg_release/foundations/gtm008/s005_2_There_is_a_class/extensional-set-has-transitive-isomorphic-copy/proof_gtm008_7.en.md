---
role: proof
locale: en
of_concept: extensional-set-has-transitive-isomorphic-copy
source_book: gtm008
source_chapter: "7"
source_section: "Relative Constructibility"
---
We define $f$ recursively by

$$f(y) = \{f(x) \mid x \in A \cap y\}.$$

The conclusion is then immediate from the recursive definition: $f$ is well-defined by transfinite induction on the rank of elements in $A$. One verifies that $f$ is one-to-one: if $f(x) = f(y)$ then by the extensionality condition on $A$, there exists $z \in A$ distinguishing $x$ and $y$, which would lead to a contradiction. Moreover, $f$ preserves the $\in$-relation by construction. Finally, if $b$ is a transitive subset of $A$, then by induction on rank one shows $f(x) = x$ for all $x \in b$, so $f \upharpoonright b = I \upharpoonright b$.
