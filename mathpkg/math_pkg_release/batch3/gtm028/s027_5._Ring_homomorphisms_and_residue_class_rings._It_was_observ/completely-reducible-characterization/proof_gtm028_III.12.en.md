---
role: proof
locale: en
of_concept: completely-reducible-characterization
source_book: gtm028
source_chapter: "III"
source_section: "§12"
---

We regard $(0)$ as the direct sum of the empty collection of submodules.

Suppose first that $M$ is completely reducible and of finite length. By induction on $l(M)$: if $l(M) = 0$, then $M = (0)$ and the statement holds vacuously. If $l(M) > 0$, then $M$ contains a simple submodule $S$ (since we can take a minimal non-zero submodule using the minimum condition, which follows from finite length). Since $M$ is completely reducible, $S$ has a complement, so $M = S \oplus M'$. By additivity of length, $l(M') = l(M) - 1$, so by induction $M'$ is a direct sum of simple submodules. Hence $M$ is too.

Now suppose $M = M_1 + \cdots + M_r$ where each $M_i$ is simple. We first show that $M$ is completely reducible. Let $N$ be any proper submodule of $M$, and let $M_{i_1}$ be the first of the modules $M_1, \cdots, M_r$ which is not contained in $N$. Since $M_{i_1}$ is simple, $N \cap M_{i_1} = (0)$, so the sum $N + M_{i_1}$ is direct. If $N \oplus M_{i_1} = M$, then $M_{i_1}$ is a complement of $N$; otherwise let $M_{i_2}$ be the first $M_i$ not contained in $N \oplus M_{i_1}$. Continuing in this way we obtain $N \oplus M_{i_1} \oplus M_{i_2} \oplus \cdots \oplus M_{i_s} = M$. Thus $N$ has a complement, and $M$ is completely reducible. Furthermore, taking $N = (0)$ gives $M = N_1 \oplus \cdots \oplus N_t$ where the $N_j$ are certain of the $M_i$, so $M$ is a direct sum of simple submodules, and $l(M) = t$.

Uniqueness of the simple summands up to isomorphism follows from the Jordan-Hölder theorem, since the decomposition provides a composition series.
