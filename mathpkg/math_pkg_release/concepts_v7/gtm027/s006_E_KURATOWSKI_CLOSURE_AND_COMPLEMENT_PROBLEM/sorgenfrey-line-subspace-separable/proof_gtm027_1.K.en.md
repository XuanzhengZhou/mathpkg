---
role: proof
locale: en
of_concept: sorgenfrey-line-subspace-separable
source_book: gtm027
source_chapter: "1"
source_section: "K"
---

# Proof that Every Subspace of the Sorgenfrey Line Is Separable

**Theorem.** Every subspace of $(X, \mathfrak{J})$ (the Sorgenfrey line) is separable.

*Proof.* Let $Y \subseteq \mathbb{R}$ be any subset with the subspace topology inherited from the Sorgenfrey line.

For each rational $q \in \mathbb{Q}$ and each positive integer $n \in \mathbb{N}$, if the interval $[q, q+1/n)$ intersects $Y$, pick a point $y_{q,n} \in Y \cap [q, q+1/n)$. Let $D$ be the collection of all such chosen points. Since $\mathbb{Q} \times \mathbb{N}$ is countable, $D$ is a countable subset of $Y$.

We claim $D$ is dense in $Y$. Let $y \in Y$ and let $[a,b)$ be a basic neighborhood of $y$ in the Sorgenfrey line (so $a \leq y < b$). We need to show $[a,b) \cap D \neq \emptyset$.

Since $\mathbb{Q}$ is dense in $\mathbb{R}$ in the usual sense, there exists a rational $q$ with $y \leq q < \min(b, y+\delta)$ for sufficiently small $\delta$. Alternatively, pick $n$ large enough so that $1/n < b - y$. Then there exists a rational $q$ with $y \leq q < y + 1/n$. The interval $[q, q+1/n)$ intersects $Y$ (it contains $y$ or a point arbitrarily close to $y$ on the right). By construction, $D$ contains a point from $Y \cap [q, q+1/n)$, which lies in $[a,b)$.

Thus $D$ is a countable dense subset of $Y$, proving $Y$ is separable. $\square$
