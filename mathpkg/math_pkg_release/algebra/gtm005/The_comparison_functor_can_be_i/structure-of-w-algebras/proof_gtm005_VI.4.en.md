---
role: proof
locale: en
of_concept: structure-of-w-algebras
source_book: gtm005
source_chapter: "VI"
source_section: "4"
---

The structure of a $W$-algebra $\langle S, \theta: WS \to S \rangle$ is determined by the universal property of the coproduct $WS = \coprod_{n=1}^{\infty} S^n$. For each $n \geq 1$, the restriction of the structure map $\theta$ to the $n$-th component $S^n \subseteq WS$ defines an $n$-ary operation
$$v_n = \theta|_{S^n} : S^n \to S.$$

The algebra axioms for $\theta$ translate directly into the coherence conditions on the operations $v_n$. The unit law $\theta \circ \eta_S = 1_S$ gives $v_1 = 1_S$. The associative law $\theta \circ \mu_S = \theta \circ W\theta$ states that for any word of words, first flattening via $\mu_S$ and then applying $\theta$ yields the same result as first applying $\theta$ to each inner word (via $W\theta$) and then applying $\theta$ to the resulting word of elements. Unpacking this for a word of $k$ words of lengths $n_1, \dots, n_k$ yields the identity
$$v_k \circ (v_{n_1} \times \cdots \times v_{n_k}) = v_{n_1 + \cdots + n_k}.$$

Since $v_1 = 1$, applying this with $k=2$, $n_1 = 1$, $n_2 = 1$ shows $v_2(v_2 \times 1) = v_3$, and more generally $v_n$ is the $n$-fold iteration of the binary operation $v_2$.
