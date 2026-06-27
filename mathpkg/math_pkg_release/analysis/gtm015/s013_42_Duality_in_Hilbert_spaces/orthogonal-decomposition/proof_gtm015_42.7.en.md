---
role: proof
locale: en
of_concept: orthogonal-decomposition
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.7"
---

# Proof of Orthogonal Decomposition Theorem

**Theorem.** Let $N$ be a closed linear subspace of a Hilbert space $H$. For each $x \in H$ there exists a unique representation $x = y + z$ with $y \in N$ and $z \in N^\perp$.

*Proof.* **Uniqueness.** Suppose $x = y_1 + z_1 = y_2 + z_2$ with $y_1, y_2 \in N$ and $z_1, z_2 \in N^\perp$. Then the vector

$$y_1 - y_2 = z_2 - z_1$$

belongs both to $N$ (since $N$ is a linear subspace) and to $N^\perp$ (since $N^\perp$ is a linear subspace). By (42.5), $N \cap N^\perp = \{\theta\}$, hence $y_1 - y_2 = \theta$ and $z_2 - z_1 = \theta$. Thus $y_1 = y_2$ and $z_1 = z_2$.

**Existence.** By Theorem (42.3) applied to the closed convex set $N$, there exists $y_0 \in N$ such that

$$\|x - y_0\| \leq \|x - y\| \quad \text{for all } y \in N.$$

Set $z_0 = x - y_0$; it suffices to show that $z_0 \perp N$, i.e., $(z_0|y) = 0$ for all $y \in N$. We may assume $\|y\| = 1$ (otherwise replace $y$ by $y/\|y\|$).

Observe that the vector $z_0 - (z_0|y)y$ is orthogonal to $y$, since

$$(z_0 - (z_0|y)y \mid y) = (z_0|y) - (z_0|y)(y|y) = (z_0|y) - (z_0|y) \cdot 1 = 0.$$

Consequently, $z_0 - (z_0|y)y$ is also orthogonal to $(z_0|y)y$. Writing

$$z_0 = [z_0 - (z_0|y)y] + (z_0|y)y$$

as a sum of orthogonal vectors, the Pythagorean law (42.6) yields

$$\|z_0\|^2 = \|z_0 - (z_0|y)y\|^2 + \|(z_0|y)y\|^2. \tag{1}$$

On the other hand, since $y_0 \in N$ and $y \in N$, we have $y_0 + (z_0|y)y \in N$. By the minimizing property of $y_0$,

$$\|z_0\|^2 = \|x - y_0\|^2 \leq \|x - [y_0 + (z_0|y)y]\|^2 = \|z_0 - (z_0|y)y\|^2. \tag{2}$$

Comparing (1) and (2), we obtain $\|(z_0|y)y\|^2 \leq 0$, whence $\|(z_0|y)y\|^2 = 0$ and therefore $(z_0|y) = 0$. This holds for every $y \in N$, so $z_0 \in N^\perp$.
