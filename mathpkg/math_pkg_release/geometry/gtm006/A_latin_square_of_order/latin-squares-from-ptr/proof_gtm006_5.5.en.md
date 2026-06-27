---
role: proof
locale: en
of_concept: latin-squares-from-ptr
source_book: gtm006
source_chapter: "5"
source_section: "5. Latin Squares"
---

**Proof of Lemma 5.7.**

(1) Fix $i$. Then $T(x, i, j) = T(x, i, k)$ if and only if $j = k$, by condition (D) of Theorem 5.1 (which states that for $a \neq 0$, the equation $T(a, b, x) = c$ has a unique solution $x$). Hence no two entries in the same row are equal.

For a fixed column $j$, condition (C) of Theorem 5.1 guarantees that there is a unique $x$ satisfying $T(x, i, j) = T(x, k, j)$ with $i \neq k$. But if $x = 0$, then $T(0, i, j) = j = T(0, k, j)$, which would give $j = j$ without forcing $i = k$. So for $x \neq 0$, the equality $T(x, i, j) = T(x, k, j)$ implies $i = k$. Since the square $\{x\}$ is only defined for $x \neq 0$, no two entries in the same column are equal.

Thus each row and each column of $\{x\}$ contains every element of $R$ exactly once, so $\{x\}$ is a Latin square.

(2) Suppose that for some $x \neq y$ the squares $\{x\}$ and $\{y\}$ are not orthogonal. Then there exist positions $(i, j)$ and $(k, \ell)$ such that
$$(T(x, i, j), T(y, i, j)) = (T(x, k, \ell), T(y, k, \ell)).$$
By condition (D), for fixed $x$ and row index $i$, the map $j \mapsto T(x, i, j)$ is a bijection. Moreover, condition (C) ensures that the equation $T(x, i, j) = T(y, i, j)$ has, for $x \neq y$, at most one solution in each coordinate. Specifically, if the ordered pairs coincide at two distinct positions, then by the property of a PTR, the positions must be the same. Therefore the $n^2$ ordered pairs are all distinct, which means the two squares are orthogonal.
