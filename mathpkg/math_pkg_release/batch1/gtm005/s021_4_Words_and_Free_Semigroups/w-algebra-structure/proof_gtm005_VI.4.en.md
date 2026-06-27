---
role: proof
locale: en
of_concept: w-algebra-structure
source_book: gtm005
source_chapter: "VI"
source_section: "4. Words and Free Semigroups"
---

A $W$-algebra is a set $S$ together with a structure map $\theta : WS \to S$ satisfying the unit law $\theta \circ \eta_S = 1_S$ and the associative law $\theta \circ \mu_S = \theta \circ W\theta$.

For each positive integer $n$, define the $n$-ary operation $v_n : S^n \to S$ by
$$v_n(s_1, \dots, s_n) = \theta(\langle s_1 \rangle \dots \langle s_n \rangle),$$
where $\langle s_1 \rangle \dots \langle s_n \rangle$ is the word of length $n$ in $WS = \prod_{n=1}^{\infty} S^n$.

The unit law $\theta(\eta_S(s)) = s$ for each $s \in S$ gives
$$v_1(s) = \theta(\langle s \rangle) = \theta(\eta_S(s)) = s,$$
so $v_1 = 1_S$.

The associative law requires that for any word of words,
$$\theta(\mu_S(\langle \langle s_{11} \rangle \dots \langle s_{1n_1} \rangle \rangle \dots \langle \langle s_{k1} \rangle \dots \langle s_{kn_k} \rangle \rangle))
= \theta(W\theta(\langle \langle s_{11} \rangle \dots \langle s_{1n_1} \rangle \rangle \dots \langle \langle s_{k1} \rangle \dots \langle s_{kn_k} \rangle \rangle)).$$

The left side applies $\theta$ to the flattened word:
$$\theta(\langle s_{11} \rangle \dots \langle s_{1n_1} \rangle \dots \langle s_{k1} \rangle \dots \langle s_{kn_k} \rangle) = v_{n_1 + \dots + n_k}(s_{11}, \dots, s_{kn_k}).$$

The right side applies $W\theta$ first, which applies $\theta$ to each inner word, then $\theta$ to the resulting word:
$$\theta(\langle \theta(\langle s_{11} \rangle \dots \langle s_{1n_1} \rangle) \rangle \dots \langle \theta(\langle s_{k1} \rangle \dots \langle s_{kn_k} \rangle) \rangle)
= v_k(v_{n_1}(s_{11}, \dots, s_{1n_1}), \dots, v_{n_k}(s_{k1}, \dots, s_{kn_k})).$$

Thus $v_{n_1 + \dots + n_k} = v_k \circ (v_{n_1} \times \dots \times v_{n_k})$. In particular, $v_n$ is the $n$-fold iteration of the binary $v_2$, and $v_2$ is associative.
