---
role: proof
locale: en
of_concept: convex-symmetric-line-segment-neighborhood
source_book: gtm027
source_chapter: "6"
source_section: "U"
---

# Proof: Convex Symmetric Sets Containing Line Segments Are Neighborhoods

Let $X$ be a real linear topological space which is not meager in itself. Let $K \subset X$ be a closed convex set such that $K = -K$ and $K$ contains a line segment in each direction: for each $x \in X$, there exists $t > 0$ such that $sx \in K$ for $0 \leq s \leq t$.

First, $K$ is not meager. Since $K$ contains a segment in each direction, we have

$$X = \bigcup_{n=1}^{\infty} nK.$$

Indeed, for any $x \in X$, choose $t > 0$ with $sx \in K$ for $0 \leq s \leq t$. Then for sufficiently large $n$, $x/n \in K$, so $x \in nK$.

Since $X$ is not meager, some $nK$ is not meager. But multiplication by $n$ is a homeomorphism, so $K$ itself is not meager in $X$.

Now $K$ is not meager and is almost open (being closed, it is a Borel set, hence almost open by 6.P(a)). By the Banach-Kuratowski-Pettis theorem (6.P(b)), $K - K$ is a neighborhood of $0$. But $K$ is convex and symmetric, so

$$K - K = K + K = 2K$$

by convexity. Therefore $2K$ is a neighborhood of $0$, and consequently $K$ itself is a neighborhood of $0$.
