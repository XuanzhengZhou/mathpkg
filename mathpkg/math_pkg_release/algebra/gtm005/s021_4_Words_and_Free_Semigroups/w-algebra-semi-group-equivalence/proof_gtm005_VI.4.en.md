---
role: proof
locale: en
of_concept: w-algebra-semi-group-equivalence
source_book: gtm005
source_chapter: "VI"
source_section: "4. Words and Free Semigroups"
---

The proof follows by induction on $n$ using the $W$-algebra associative law derived in Proposition 2.

By Proposition 2, the structure map $\theta : WS \to S$ satisfies $\theta(\langle s_1 \rangle \dots \langle s_n \rangle) = v_n(s_1, \dots, s_n)$. The algebra associative law $v_{n_1 + \dots + n_k} = v_k \circ (v_{n_1} \times \dots \times v_{n_k})$ specializes for $k = 2$, $n_1 = n$, $n_2 = 1$ to
$$v_{n+1}(s_1, \dots, s_n, s_{n+1}) = v_2(v_n(s_1, \dots, s_n), s_{n+1}) = v_n(s_1, \dots, s_n) \cdot s_{n+1}$$
where $\cdot$ denotes the binary operation $v_2$. This is exactly $v_{n+1} = v_n \circ (v_2 \times 1)$.

By induction, $v_n$ is the $n$-fold iterated product: $v_2 = \cdot$ is the binary operation, and assuming $v_n$ is the $n$-fold product, then $v_{n+1}(s_1, \dots, s_{n+1}) = (s_1 \cdots s_n) \cdot s_{n+1} = s_1 \cdots s_n s_{n+1}$, so $v_{n+1}$ is the $(n+1)$-fold product.

Conversely, given any semigroup $\langle S, v \rangle$ with associative binary $v$, define $v_2 = v$, $v_1 = 1_S$, and $v_{n+1} = v_n \circ (v \times 1)$. Then the associative law for the monad algebra follows from associativity of $v$ by induction, and the $W$-algebra unit law holds because $v_1 = 1_S$.

Thus the comparison functor $K : \mathbf{Smgrp} \to \mathbf{Set}^W$ sending $\langle S, v \rangle$ to $\langle S, 1, v, v_3, \dots \rangle$ is bijective on objects (each $W$-algebra determines a unique semigroup, and each semigroup determines a unique $W$-algebra) and fully faithful, hence an isomorphism of categories.
