---
role: proof
locale: en
of_concept: theorem-1-8-extension-oriented-to-sphere
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Theorem 1.8 (Extension of Maps to the Sphere — Orientable Case)

**Theorem statement.** Let $W$ be a compact connected oriented $\partial$-manifold of dimension $n + 1 \geqslant 2$. A continuous map $f: \partial W \to S^n$ extends to a continuous map $W \to S^n$ if and only if $\deg f = 0$.

**Proof.** If $f$ extends to $W$, then $\deg f = 0$ by Theorem 1.6(b).

Conversely, suppose $\deg f = 0$. By Lemma 1.5, we may assume $f$ is $C^\infty$. Choose a regular value $y \in S^n$ for $f$. Since $\deg(f, y) = 0$, the number of points in $f^{-1}(y)$ of positive type equals the number of negative type. Hence we can pair each positive point with a negative point and embed disjoint arcs $K_1, \ldots, K_k \subset W$ joining them; each $K_i$ meets $\partial W$ normally at its endpoints. The complement of $\cup K_i$ in $\partial W$ is an arc or a circle; each arc component has endpoints of opposite types (see arrows in Figure 5-1). Thus we obtain disjoint embedded arcs whose total set of endpoints is exactly $f^{-1}(y)$.

Now apply Lemma 1.7 to each arc $K_i$, with $N = S^n$. We obtain an open neighborhood $W_0 \subset W$ of $\cup K_i$ and a map $g: W_0 \to S^n$ which agrees with $f$ on $\partial W_0$, has $y$ as a regular value, and satisfies $g^{-1}(y) = \cup K_i$.

Let $U \subset W_0$ be a smaller open neighborhood of $\cup K_i$ whose closure is contained in $W_0$. Then $\mathrm{Bd}\, U \subset W_0 - \cup K_i$. The maps $g$ and $f$ fit together to form a continuous map

$$h: X = \mathrm{Bd}\, U \cup (\partial W - U) \to S^n - \{y\}.$$

Note that $X$ is a closed subset of $W - U$. Since $S^n - \{y\} \cong \mathbb{R}^n$, the Tietze extension theorem permits an extension of $h$ to a map $H: W - U \to S^n - \{y\}$.

The required extension of $f$ to $W$ is the map equal to $H$ on $W - U$ and to $g$ on $W_0$. These agree on the overlap $(W - U) \cap W_0 = W_0 - U$, giving a well-defined continuous extension.
