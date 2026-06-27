---
role: proof
locale: en
of_concept: preservation-of-jordan-decomposition
source_book: gtm009
source_chapter: "II"
source_section: "6"
---

Let $\phi: L \rightarrow \mathfrak{gl}(V)$ be a representation. Let $N = N_{\mathfrak{gl}(V)}(\phi(L))$ be the normalizer of $\phi(L)$ in $\mathfrak{gl}(V)$. For any $L$-submodule $W \subset V$, define
$$L_W = \{ y \in \mathfrak{gl}(V) \mid y(W) \subset W \text{ and } \operatorname{Tr}(y|_W) = 0 \}.$$
For example, $L_V = \mathfrak{sl}(V)$. Since $L = [L, L]$, we have $\phi(L) \subset L_W$ for every $W$.

Set $L' = N \cap \bigcap_W L_W$, where the intersection is over all $L$-submodules $W$ of $V$. Clearly $L'$ is a subalgebra of $N$ containing $\phi(L)$ as an ideal. More importantly: if $x \in L$, then the semisimple and nilpotent parts $x_s, x_n$ (viewed as elements of $\mathfrak{gl}(V)$) also lie in each $L_W$, and therefore in $L'$.

It remains to show $L' = \phi(L)$. Since $L'$ is a finite-dimensional $L$-module, Weyl's Theorem (6.3) gives $L' = \phi(L) \oplus M$ for some $L$-submodule $M$. But $[L, L'] \subset \phi(L)$ (since $L' \subset N$), so $L$ acts trivially on $M$.

Let $W$ be any irreducible $L$-submodule of $V$. For $y \in M$, $[L, y] = 0$, so Schur's Lemma implies $y|_W$ is a scalar. But $\operatorname{Tr}(y|_W) = 0$ since $y \in L_W$, forcing $y|_W = 0$. By Weyl's Theorem, $V$ decomposes as a direct sum of irreducible $L$-submodules, so $y = 0$ on all of $V$, hence $M = 0$ and $L' = \phi(L)$.

Therefore $\phi(x)_s, \phi(x)_n \in \phi(L)$, and the semisimple and nilpotent parts $\phi(x)_s, \phi(x)_n$ are precisely $\phi(x_s)$ and $\phi(x_n)$ respectively.
