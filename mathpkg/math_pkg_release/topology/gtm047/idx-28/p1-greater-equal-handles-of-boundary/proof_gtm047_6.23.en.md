---
role: proof
locale: en
of_concept: p1-greater-equal-handles-of-boundary
source_book: gtm047
source_chapter: "6"
source_section: "23"
---

**Proof.** (1) By Theorem 16, the theorem reduces to the case in which $|K| = N(L)$, where $L$ is a finite subcomplex of a triangulated 3-manifold $K'$.

(2) We shall show that the theorem reduces to the case in which $L$ is at most 2-dimensional. Suppose that we have given an $L$ such that

$$p^1(N(L)) \geqslant h(\text{Bd } N(L)). \tag{a}$$

Suppose that we adjoin to $L$ a $\sigma^3$ such that $\partial \sigma^3 \subset L$. Then $H_1(N(L))$ is unchanged; and so also is $h(\text{Bd } N(L))$, since we have merely deleted a 2-sphere from Bd $N(L)$. Thus (a) is preserved by the adjunction of $\sigma^3$.

Hereafter we assume that $\dim L \leqslant 2$. By Theorem 18, we know that (a) holds when $\dim L \leqslant 1$. It remains to show that (a) is preserved when we adjoin to $L$ a $\sigma^2$ such that $\partial \sigma^2 \subset L$, but $\sigma^2 \notin L$. Let $L' = L \cup \sigma^2$, and let $A = \partial \sigma^2$. Let $J$ be a regular neighborhood of $A$ in Bd $N(L)$. Then $J$ is a polygon.

Bd $N(L')$ is obtainable from Bd $N(L)$ by "splitting and spanning," as in Problems 22.11 and 22.12. By the results of these problems, this never increases the total number of handles. Therefore $h(N(L')) \leqslant h(N(L))$. Thus, in Case 1, adjunction of $\sigma^2$ preserves (a).

Case 2. Suppose that $Z_A \notin T^1$. Then

$$Z_A = \sum_{i=1}^{p} n_i Z_i + t_Z,$$

where the numbers $n_i$ are not all equal to 0; say, $n_p \neq 0$. Then $\{Z_1, Z_2, \ldots, Z_{p-1}\}$ is linearly independent over $\mathbb{Z}$ modulo $G$, and $p^1(N(L')) \geqslant p^1(N(L)) - 1$. Now Bd $N(L')$ is obtained by "splitting and spanning" the component $M$ of Bd $N(L)$ that contains $A$. If $M - J$ were not connected, then we would have $Z_A = 0$ in $H_1(M)$, and hence $Z_A = 0$ in $H_1 = H_1(N(L))$, which is false. Therefore $M - J$ is connected. By the result of Problem 22.11, we have

$$h(\text{Bd } N(L')) = h(\text{Bd } N(L)) - 1.$$

Therefore (a) is preserved by the adjunction of $\sigma^2$.

The theorem follows, by induction on the number of 2-simplexes of $L$.
