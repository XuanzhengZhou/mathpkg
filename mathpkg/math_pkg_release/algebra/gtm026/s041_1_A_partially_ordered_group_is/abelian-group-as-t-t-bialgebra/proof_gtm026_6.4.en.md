---
role: proof
locale: en
of_concept: abelian-group-as-t-t-bialgebra
source_book: gtm026
source_chapter: "6"
source_section: "4"
---

**Proof.** Let $T$ be the algebraic theory of abelian groups. A $T$-algebra $(X, \xi)$ is an abelian group. To verify that $(X, \xi, \xi)$ is a $T$-$T$ bialgebra, we must show that every semantic $T$-operation is a $T$-homomorphism with respect to $\xi$.

The key semantic $T$-operations are:

- **Zero:** The constant operation $0 \in X$. The map $x \mapsto 0$ is trivially a $T$-homomorphism because it sends the group identity to itself and commutes with all operations.
- **Minus:** The unary operation $x \mapsto -x$. In an abelian group, $-(x + y) = (-x) + (-y)$ and $-0 = 0$, so negation is a group homomorphism.
- **Plus:** The binary operation $(x, y) \mapsto x + y$. In an abelian group, addition is itself a group homomorphism: $(x + y) + (u + v) = (x + u) + (y + v)$ by commutativity and associativity.

Since all generating operations are $T$-homomorphisms, and the class of $T$-homomorphisms is closed under composition, every semantic $T$-operation $\alpha: (U^T)^n \to U^T$ gives rise to a map $(X, \xi)\alpha: (X, \xi)^n \to (X, \xi)$ that is a $T$-homomorphism. Therefore $(X, \xi, \xi)$ satisfies the bialgebra condition.

This reasoning fails for non-abelian groups because the group multiplication is not a group homomorphism when the group is non-abelian. $\square$
