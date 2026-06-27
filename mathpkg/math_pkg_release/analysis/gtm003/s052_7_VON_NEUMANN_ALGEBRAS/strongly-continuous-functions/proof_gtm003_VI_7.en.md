---
role: proof
locale: en
of_concept: strongly-continuous-functions
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

Denote by $C$ the set of all strongly continuous functions on $\mathbb{R}$. Clearly $C \neq \emptyset$, since constant functions and the identity function are strongly continuous (the latter because $a \mapsto a$ is trivially strongly continuous). One verifies that $C$ is a uniformly closed subalgebra of $C_b(\mathbb{R})$ (bounded continuous functions on $\mathbb{R}$).

To prove that every bounded continuous function is strongly continuous, observe that the Stone-Weierstrass theorem implies that the set of functions with compact support (or continuous functions vanishing at infinity) is uniformly dense in $C_b(\mathbb{R})$. Since the map $a \mapsto f(a)$ is continuous for polynomials in $a$ (by continuity of algebraic operations in the strong operator topology on bounded sets, established in 7.2), and since any bounded continuous function can be uniformly approximated by such functions, the result follows.

For the second assertion: if $f$ and $g$ are strongly continuous and $f$ is bounded, then the product $fg$ is strongly continuous because multiplication is continuous on bounded sets for the strong operator topology (Theorem 7.2).
