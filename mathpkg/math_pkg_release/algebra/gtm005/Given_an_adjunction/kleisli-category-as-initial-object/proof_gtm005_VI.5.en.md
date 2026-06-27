---
role: proof
locale: en
of_concept: kleisli-category-as-initial-object
source_book: gtm005
source_chapter: "VI"
source_section: "5. Free Algebras for a Monad"
---

**Proof.** This theorem summarizes the two comparison theorems (Theorems 1 and 2 of this section) together with the corresponding Eilenberg-Moore comparison theorem.

Given any adjunction $\langle F, G, \eta, \varepsilon \rangle : X \to A$ that defines the monad $T$, Theorem 2 (the Kleisli comparison theorem) provides a unique functor $L : X_T \to A$ satisfying $GL = G_T$ and $LF_T = F$. This functor $L$, together with the identity natural transformation on $F_T$ and $G_T$, constitutes a map of adjunctions from the Kleisli adjunction to the given adjunction, with the identity on $X$. The uniqueness of $L$ established in Theorem 2 translates to the uniqueness of the map of adjunctions, making the Kleisli adjunction an initial object in $\mathbf{Adj}(T)$.

Dually, the Eilenberg-Moore category $X^T$ with its canonical adjunction is the terminal object in $\mathbf{Adj}(T)$, via the Eilenberg-Moore comparison theorem. Together, these results show that every adjunction defining the monad $T$ factors uniquely through the Kleisli adjunction and maps uniquely into the Eilenberg-Moore adjunction. $\square$
