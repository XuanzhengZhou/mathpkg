---
role: proof
locale: en
of_concept: extension-along-arcs
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Lemma 1.7 (Extension of a Map Along an Arc)

We may take $(N, y) = (\mathbb{R}^n, 0)$. Let the endpoints of $K$ be $x_0, x_1$. Since $0$ is a regular value, each $x_i$ has a neighborhood $U_i \subset V$ such that $f$ restricts to an embedding $f_i: (U_i, x_i) \to (\mathbb{R}^n, 0)$.

It suffices to prove the lemma for any map agreeing with $f$ near $K$. Therefore, we can assume that each $f_i$ is a diffeomorphism. Then $f_i^{-1}$ can be regarded as a tubular neighborhood of $x_i$ in $W$; together, $f_0^{-1}$ and $f_1^{-1}$ form a tubular neighborhood of $\partial K$ in $\partial W$.

By Theorem 4.6.4 (extension of tubular neighborhoods), this tubular neighborhood extends to a tubular neighborhood $E$ of $K$ in $V$. We may assume $W = E$. Since $K$ is an arc, $E$ is a trivial vector bundle over $K$, and we may write

$$(W, K) = (I \times \mathbb{R}^n, I \times 0)$$

with $(N, y) = (\mathbb{R}^n, 0)$. With this notation,

$$V = 0 \times \mathbb{R}^n \cup 1 \times \mathbb{R}^n$$

and each $f_i: i \times \mathbb{R}^n \to \mathbb{R}^n$, $i = 0, 1$, is given by a linear isomorphism $L_i \in \mathrm{GL}(n)$. The degree assumptions and the convention for orienting $\partial(I \times \mathbb{R}^n)$ imply that $L_0$ and $L_1$ have determinants of the same sign. Therefore, $L_0$ and $L_1$ can be joined by a continuous path $L_t$ in $\mathrm{GL}(n)$, $0 \leqslant t \leqslant 1$.

The required extension of $f$ is the map

$$I \times \mathbb{R}^n \to \mathbb{R}^n, \qquad (t, y) \mapsto L_t(y).$$

This map agrees with $f$ on $V = (\{0\} \times \mathbb{R}^n) \cup (\{1\} \times \mathbb{R}^n)$ and has $0$ as a regular value (since each $L_t$ is an isomorphism, the preimage of $0$ is precisely $I \times 0 = K$).
