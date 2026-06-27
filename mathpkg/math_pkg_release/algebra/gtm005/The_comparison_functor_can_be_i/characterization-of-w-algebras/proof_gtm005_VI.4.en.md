---
role: proof
locale: en
of_concept: characterization-of-w-algebras
source_book: gtm005
source_chapter: "VI"
source_section: "4"
---

The forward direction follows from Proposition 2: any $W$-algebra $\langle S, \theta \rangle$ yields operations $v_n$ satisfying the coherence conditions. Setting $k=2$, $n_1 = n$, $n_2 = 1$ gives $v_{n+1} = v_n \circ (v_2 \times 1_S)$ by induction on $n$, and $v_2$ is associative by applying the coherence condition with $k=2, n_1 = n_2 = 1$ and with $k=3, n_1 = n_2 = n_3 = 1$.

Conversely, given a set $S$ with an associative binary operation $v_2$ and $v_1 = 1_S$, define $v_{n+1} = v_n \circ (v_2 \times 1_S)$ inductively for $n \geq 1$. By associativity of $v_2$, an easy induction proves that the coherence conditions of Proposition 2 are satisfied. Thus $\langle S, v_1, v_2, \ldots \rangle$ is a $W$-algebra.

The statement about the comparison functor $K$ follows immediately: $K$ sends a semigroup $\langle S, v \rangle$ to $\langle S, 1_S, v, v_3, \ldots \rangle$ with the iterated operations, and this assignment is clearly bijective on objects and morphisms. A $W$-algebra homomorphism $f: S \to S'$ satisfies $f \circ v_n = v_n' \circ f^n$ for all $n$, which reduces to the semigroup homomorphism condition $f \circ v_2 = v_2' \circ (f \times f)$ since all higher $v_n$ are iterates of $v_2$. Hence $K$ is fully faithful and essentially surjective, i.e., an isomorphism.
