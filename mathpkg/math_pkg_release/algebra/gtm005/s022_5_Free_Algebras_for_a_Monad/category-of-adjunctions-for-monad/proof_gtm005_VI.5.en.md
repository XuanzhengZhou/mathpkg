---
role: proof
locale: en
of_concept: category-of-adjunctions-for-monad
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "5. Free Algebras for a Monad"
---

This theorem summarizes the two comparison results established earlier in the chapter.

**Initial object: the Kleisli construction.** Theorem 2 (the comparison theorem for the Kleisli construction) establishes that for any adjunction $\langle F, G, \eta, \varepsilon \rangle : X \rightleftharpoons A$ defining the monad $T$, there is a unique functor $L : X_T \to A$ with $GL = G_T$ and $L F_T = F$. This functor $L$ is precisely a map of adjunctions from the Kleisli adjunction $F_T \dashv G_T$ to the given adjunction $F \dashv G$, with the identity on $X$. The uniqueness of $L$ means that the Kleisli adjunction is an initial object in the category $\mathbf{Adj}(T)$.

**Terminal object: the Eilenberg–Moore construction.** Dually, the comparison theorem for the Eilenberg–Moore construction (proved earlier in Chapter VI) states that for any adjunction $\langle F, G, \eta, \varepsilon \rangle : X \rightleftharpoons A$ defining $T$, there is a unique functor $K : A \to X^T$ with $G^T K = G$ and $K F = F^T$, where $F^T \dashv G^T : X \rightleftharpoons X^T$ is the Eilenberg–Moore adjunction. This makes the Eilenberg–Moore adjunction a terminal object in $\mathbf{Adj}(T)$.

**Morphism composition.** Maps of adjunctions (as defined in § IV.7) compose in the evident way, and the identity-on-$X$ condition is preserved under composition, so $\mathbf{Adj}(T)$ is indeed a category with the claimed initial and terminal objects.
