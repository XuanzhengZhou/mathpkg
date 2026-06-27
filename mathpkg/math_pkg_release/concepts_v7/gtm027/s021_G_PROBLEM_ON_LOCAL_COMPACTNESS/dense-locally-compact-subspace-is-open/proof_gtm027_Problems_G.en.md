---
role: proof
locale: en
of_concept: dense-locally-compact-subspace-is-open
source_book: gtm027
source_chapter: "Problems"
source_section: "G"
---

# Proof: Dense Locally Compact Subspace of a Hausdorff Space is Open

**Theorem.** Let $X$ be a Hausdorff space and let $Y \subset X$ be a dense locally compact subspace. Then $Y$ is open in $X$.

**Proof.**

Let $y \in Y$. Since $Y$ is locally compact, there exists an open neighborhood $V$ of $y$ in $Y$ and a compact set $K \subset Y$ such that $y \in V \subset K$.

Since $K$ is compact in the Hausdorff space $X$, it is closed in $X$. Now, $V$ is open in $Y$, so $V = Y \cap W$ for some open set $W \subset X$.

We claim that $W \subset Y$. Let $x \in W$. Since $Y$ is dense in $X$, every neighborhood of $x$ intersects $Y$. In particular, $W$ is a neighborhood of $x$. Consider the closed set $K$. If $x \notin K$, then $x \in X \setminus K$, which is open. Then $W \cap (X \setminus K)$ is an open neighborhood of $x$.

But $V \subset K$, and $V = Y \cap W$, so $Y \cap W \subset K$. If $x \in W \setminus K$, then for any neighborhood $N$ of $x$ contained in $W \setminus K$, we have $N \cap Y \subset (W \setminus K) \cap Y = \varnothing$, which contradicts the density of $Y$. Hence $x \in K \subset Y$.

Thus $W \subset Y$, and since $W$ is open in $X$ and contains $y$, we have shown that every point of $Y$ is an interior point of $Y$ in $X$. Therefore $Y$ is open in $X$.
