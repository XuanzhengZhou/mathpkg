---
role: proof
locale: en
of_concept: bounded-tensor-product-is-algebraic
source_book: gtm026
source_chapter: "6"
source_section: "1"
---

By Lemma 6.9, $\mathbf{Set}^S \otimes T$ is a Birkhoff subcategory of $\mathbf{Set}^S \times \mathbf{Set}^T$ and $U^S \otimes T$ is a Beck functor. By results 1.19, 1.18, 3.6, and 3.3, it suffices to prove that the underlying set functor
$$
U: \mathbf{Set}^S \times \mathbf{Set}^T \to \mathbf{Set}
$$
is algebraic.

By 1.5.40, present $\mathbf{Set}^S$ as $(\Omega_S, E_S)$-algebras and $\mathbf{Set}^T$ as $(\Omega_T, E_T)$-algebras. Define $\Omega$ by
$$
\Omega_n = (\Omega_S)_n + (\Omega_T)_n
$$
for each arity $n$, and set $E = E_S + E_T$. Then $U$ is isomorphic to the underlying set functor from $(\Omega, E)$-algebras.

Since $S$ and $T$ are bounded, it follows from the construction in 1.5.40 that there exists a cardinal $n_0$ such that $\Omega_n = \varnothing$ for all $n > n_0$. Hence $\Omega$ is a finitary (indeed, bounded) presentation. By Theorem 1.27, the underlying set functor from $(\Omega, E)$-algebras is algebraic, completing the proof.
