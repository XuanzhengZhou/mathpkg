---
role: proof
locale: en
of_concept: preimage-of-regular-value-euclidean
source_book: gtm033
source_chapter: "1. The Grassmann Manifold"
source_section: "1"
---

# Proof of Preimage of a Regular Value in Euclidean Space

Let $W \subset \mathbb{R}^n$ be an open set and $f: W \to \mathbb{R}^q$ a $C^r$ map, $1 \leqslant r \leqslant \omega$. Suppose $y \in f(W)$ is a regular value of $f$; this means that $f$ has rank $q$ at every point of $f^{-1}(y)$. (Therefore $q \leqslant n$.) Then the subset $f^{-1}(y)$ is a $C^r$ submanifold of $\mathbb{R}^n$ of codimension $q$.

**Proof.** This follows from the implicit function theorem. Let $x_0 \in f^{-1}(y)$. Since $y$ is a regular value, the derivative $Df(x_0): \mathbb{R}^n \to \mathbb{R}^q$ is surjective (rank $q$). By a linear change of coordinates, we may write $\mathbb{R}^n = \mathbb{R}^{n-q} \times \mathbb{R}^q$ such that the restriction of $Df(x_0)$ to $\mathbb{R}^q$ is an isomorphism.

Write points of $\mathbb{R}^n$ as $(u, v)$ with $u \in \mathbb{R}^{n-q}$, $v \in \mathbb{R}^q$, and let $x_0 = (u_0, v_0)$. The implicit function theorem (applied to the $C^r$ map $F(u,v) = f(u,v) - y$) yields a neighborhood $U \times V$ of $(u_0, v_0)$ and a unique $C^r$ map $g: U \to V$ such that

$$f(u, g(u)) = y \quad \text{for all } u \in U,$$

and $(u, v) \in f^{-1}(y) \cap (U \times V)$ if and only if $v = g(u)$.

Thus $f^{-1}(y)$ is locally the graph of a $C^r$ function, which provides a $C^r$ submanifold chart. The map $u \mapsto (u, g(u))$ is a $C^r$ parametrization with inverse $(u, v) \mapsto u$. Hence $f^{-1}(y)$ is a $C^r$ submanifold of $\mathbb{R}^n$ of dimension $n - q$, i.e., codimension $q$. $\square$

This Euclidean-space special case foreshadows the general Regular Value Theorem (Theorem 3.2), which extends the result to maps between arbitrary manifolds.
