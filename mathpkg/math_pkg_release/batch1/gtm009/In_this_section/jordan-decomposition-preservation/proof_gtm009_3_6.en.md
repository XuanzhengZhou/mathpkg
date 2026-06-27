---
role: proof
locale: en
of_concept: jordan-decomposition-preservation
source_book: gtm009
source_chapter: "3"
source_section: "6"
---

Let $V$ be a finite dimensional vector space and $L \subset \mathfrak{gl}(V)$ a semisimple Lie subalgebra. For each $x \in L$, write its Jordan decomposition in $\mathfrak{gl}(V)$ as $x = x_s + x_n$ with $x_s$ semisimple, $x_n$ nilpotent, and $[x_s, x_n] = 0$.

Define $N = N_{\mathfrak{gl}(V)}(L) = \{y \in \mathfrak{gl}(V) \mid [y, L] \subset L\}$, the normalizer of $L$ in $\mathfrak{gl}(V)$. Clearly $L \subset N$ as an ideal.

For any $L$-submodule $W \subset V$, define $L_W = \{y \in \mathfrak{gl}(V) \mid y(W) \subset W \text{ and } \operatorname{Tr}(y|_W) = 0\}$. Note that $L_V = \mathfrak{sl}(V)$. Since $L = [L, L]$, we have $L \subset L_W$ for all such $W$.

Set $L' = N \cap \bigcap_W L_W$, where the intersection runs over all $L$-submodules $W$ of $V$. Then $L'$ is a subalgebra of $N$ containing $L$ as an ideal. Moreover, for any $x \in L$, its components $x_s, x_n$ also lie in each $L_W$ and in $N$ (by standard properties of Jordan decomposition), hence $x_s, x_n \in L'$.

Now $L'$ is a finite dimensional $L$-module (via the adjoint action). By Weyl's Theorem (6.3), $L' = L \oplus M$ for some $L$-submodule $M$, with $[L, M] \subset M$. But $L' \subset N$ implies $[L, L'] \subset L$, so $[L, M] \subset L \cap M = 0$. Thus the action of $L$ on $M$ is trivial.

Let $W$ be any irreducible $L$-submodule of $V$. For $y \in M$, $[L, y] = 0$, so $y$ commutes with the action of $L$ on $W$. By Schur's Lemma, $y$ acts on $W$ as a scalar. But $y \in L_W$, so $\operatorname{Tr}(y|_W) = 0$, forcing this scalar to be $0$. Since $V$ is a direct sum of irreducible $L$-submodules (Weyl's Theorem), $y = 0$ on all of $V$. Hence $M = 0$ and $L = L'$, so $x_s, x_n \in L$ for all $x \in L$.
