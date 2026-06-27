---
role: proof
locale: en
of_concept: symmetric-algebra-isomorphic-to-polynomial-algebra
source_book: gtm009
source_chapter: "V"
source_section: "17.1"
---
Fix a basis $(x_1, \dots, x_n)$ of $V$. Define a map from the polynomial algebra $F[t_1, \dots, t_n]$ to $\mathfrak{S}(V)$ by sending $t_i \mapsto x_i$ (the image of $x_i$ in $\mathfrak{S}(V)$). This is an algebra homomorphism because the polynomial algebra is the free commutative algebra on $n$ generators. Since the $x_i$ commute in $\mathfrak{S}(V)$ (the commutators $x_i \otimes x_j - x_j \otimes x_i$ are in $I$), the images of distinct monomials are linearly independent. Moreover, any element of $S^mV$ is a linear combination of degree-$m$ monomials in the $x_i$, and commutativity allows reordering indices into non-decreasing order. Thus the map is both injective and surjective, giving the canonical isomorphism.
