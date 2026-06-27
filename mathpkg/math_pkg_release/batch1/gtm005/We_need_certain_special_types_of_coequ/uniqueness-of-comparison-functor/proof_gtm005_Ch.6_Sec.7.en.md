---
role: proof
locale: en
of_concept: uniqueness-of-comparison-functor
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "7. Beck's Theorem"
---

**Construction of $M$ on objects.** For each $a' \in A'$, consider the canonical presentation of $a'$:
$$F G F G a' \xrightarrow[F G \varepsilon'_{a'}]{\varepsilon'_{F G a'}} F G a' \xrightarrow{\varepsilon'_{a'}} a'.$$
Applying $G'$ gives a fork in $X$ (in fact, a split fork). Since $G' = G M$ must hold, applying $G$ to the desired fork in $A$ gives the same split fork. By hypothesis (iii), $G$ creates the coequalizer, so there exists a unique object $M a' \in A$ and a unique arrow $M \varepsilon'_{a'} : F G a' \to M a'$ in $A$ with $G(M a') = G' a'$ and $G(M \varepsilon'_{a'}) = G' \varepsilon'_{a'}$, which is a coequalizer in $A$.

**Construction of $M$ on morphisms.** Given $f : a' \to b'$ in $A'$, consider the diagram with the canonical presentations. The map $F G f$ induces a morphism between the coequalizer diagrams. By the universal property of the coequalizer defining $M a'$, there exists a unique arrow $M f : M a' \to M b'$ making the square commute. Functoriality follows from uniqueness.

**Verification.** By construction, $G M = G'$ and $M F' = F$ (since on $F x$, both sides give the same coequalizer). The condition $M \varepsilon' = \varepsilon M$ follows from the definition.

**Uniqueness.** If $M_1, M_2$ are two such comparison functors, then for any $a'$, the maps $M_1 \varepsilon'_{a'}$ and $M_2 \varepsilon'_{a'}$ both coequalize the same pair and have the same image under $G$. Since $G$ creates coequalizers, $M_1 a' \cong M_2 a'$ uniquely, forcing $M_1 = M_2$.
