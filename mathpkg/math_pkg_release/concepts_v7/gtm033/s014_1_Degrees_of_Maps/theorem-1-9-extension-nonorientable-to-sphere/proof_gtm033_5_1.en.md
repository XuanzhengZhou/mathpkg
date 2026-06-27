---
role: proof
locale: en
of_concept: theorem-1-9-extension-nonorientable-to-sphere
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Theorem 1.9 (Extension of Maps to the Sphere — Nonorientable Case)

**Theorem statement.** Let $W$ be a connected compact nonorientable $\partial$-manifold of dimension $n + 1 \geqslant 2$. A continuous map $f: \partial W \to S^n$ extends to a continuous map $W \to S^n$ if and only if $\deg_2 f = 0$.

**Proof.** If $f$ extends, then $\deg_2 f = 0$ by Theorem 1.6(b).

Conversely, suppose $\deg_2 f = 0$. By Lemma 1.5, we may assume $f$ is $C^\infty$. We consider two cases.

**Case 1: $\dim W \geqslant 3$.** Let $y \in S^n$ be a regular value for $f$. Since $\deg_2 f = 0$, the set $f^{-1}(y)$ has even cardinality. Pair up the points of $f^{-1}(y)$ and embed disjoint arcs $K_1, \ldots, K_k \subset W$ joining each pair; each $K_i$ meets $\partial W$ normally at its endpoints.

If a pair of endpoints of some $K_i$ happen to be of the same type (both positive or both negative with respect to an arbitrary local orientation of $\partial W$), we change $K_i$ to a new arc $K_i'$ by adding to it an orientation-reversing loop $L$ in $W$ (see Figure 5-2). Because $\dim W \geqslant 3$, we can make $K_i'$ embedded and disjoint from the other arcs $K_j$. Choose an orientation for $TW|_{K_i'}$; this induces orientations on the tangent spaces $T_u \partial W$ and $T_v \partial W$ of the endpoints. With respect to these orientations, $u$ and $v$ are now of opposite type; otherwise $L$ would preserve orientation (contradicting that $W$ is nonorientable).

Thus we can assume each $K_i$ is oriented so that, with respect to the induced orientation of $T(\partial W)|_{f^{-1}(y)}$, the endpoints of each arc are of opposite type. The rest of the proof for $\dim W \geqslant 3$ proceeds exactly as in the oriented case (Theorem 1.8): apply Lemma 1.7 to each $K_i$, construct a neighborhood $W_0$, and use the Tietze extension theorem to extend from $W - U$ to fill in the remaining region.

**Case 2: $\dim W = 2$.** Here $n = 1$ and the target is $S^1$. Let $y \in S^1$ be a regular value for $f$. After a homotopy, we may assume $f$ is in *standard form*: there exist disjoint open intervals $I_1, \ldots, I_v \subset \partial W$ such that:
(a) each $I_j$ contains exactly one point $x_j \in f^{-1}(y)$;
(b) $f$ maps $I_j$ diffeomorphically onto $S^1 - \{-y\}$;
(c) $f(\partial W - \bigcup I_j) = -y$.

Give $\partial W$ any orientation so that the integer $\deg f$ is defined. Since $\deg_2 f = 0$, $\deg f$ is even. Each $I_j$ contributes $\pm 1$ to $\deg f$, hence $v$ is even.

We proceed by induction on $v = v(f)$. If $v = 0$, then $f$ is constant and extends to the constant map on $W$. Suppose $v \geqslant 2$. Let $K \subset W$ be a neat arc joining $x_1$ to $x_2$; give $T_K W$ an orientation $\omega$. Define a new map $g: \partial W \to S^1$ by setting $g = f$ on $\partial W - (I_1 \cup I_2)$ and $g(I_1 \cup I_2) = -y$. Then $g$ is in standard form with $v(g) = v(f) - 2$. By induction, $g$ extends to a map $G: W \to S^1$.

Now consider a tubular neighborhood $N$ of $K$ in $W$ (a $2$-disk). Note that $\deg(G|_{\partial N}) = 0$ by Theorem 1.6(b) since $G$ extends over $N$. With appropriately chosen orientations on the pieces of $\partial N$, the contributions from $f|_{I_1}$ and $f|_{I_2}$ cancel: $\deg f|_{I_1} + \deg f|_{I_2} = 0$. Define $h: \partial N \to S^1$ equal to $G$ on the complementary arcs of $\partial N$ and to $f$ on $I_1 \cup I_2$. Then $\deg h = 0$, so by Theorem 1.8 (adapted to $N$) there is an extension $H: N \to S^1$. The required extension of $f$ equals $H$ on $N$ and $G$ on $W - N$.
