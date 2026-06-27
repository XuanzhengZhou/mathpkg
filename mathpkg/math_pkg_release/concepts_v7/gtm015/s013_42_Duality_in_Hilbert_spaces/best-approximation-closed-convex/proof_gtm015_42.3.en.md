---
role: proof
locale: en
of_concept: best-approximation-closed-convex
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.3"
---

# Proof of Best Approximation from a Closed Convex Set in Hilbert Space

**Theorem.** Let $A$ be a nonempty closed convex subset of a Hilbert space $H$. For each $x \in H$, there exists a unique $y_0 \in A$ such that $\|x - y_0\| \leq \|x - y\|$ for all $y \in A$.

*Proof.* Let $\delta = \inf \{\|x - y\| : y \in A\}$. Choose a sequence $(y_n)$ in $A$ such that $\|x - y_n\| \to \delta$.

The key tool is the parallelogram law (41.6). For any $y, z \in H$,

$$\|z - y\|^2 = 2\|x - y\|^2 + 2\|x - z\|^2 - \|2x - (y + z)\|^2. \tag{*}$$

Since

$$\|2x - (y+z)\|^2 = 4\left\|x - \tfrac{1}{2}(y+z)\right\|^2$$

and $\tfrac{1}{2}(y+z) \in A$ by convexity of $A$, we have

$$\|2x - (y+z)\|^2 \geq 4\delta^2$$

by definition of $\delta$. Substituting this into $(*)$ yields

$$\|z - y\|^2 \leq 2\|x - y\|^2 + 2\|x - z\|^2 - 4\delta^2. \tag{**}$$

Setting $y = y_n$, $z = y_m$ in $(**)$ gives

$$\|y_m - y_n\|^2 \leq 2\|x - y_n\|^2 + 2\|x - y_m\|^2 - 4\delta^2.$$

As $m, n \to \infty$, the right-hand side tends to $2\delta^2 + 2\delta^2 - 4\delta^2 = 0$, hence $\|y_m - y_n\| \to 0$. Thus $(y_n)$ is a Cauchy sequence.

Since $H$ is complete, there exists $y_0 \in H$ such that $\|y_n - y_0\| \to 0$. Because $A$ is closed, $y_0 \in A$. By continuity of the norm (16.4), $\|x - y_n\| \to \|x - y_0\|$, so $\|x - y_0\| = \delta$. This proves existence.

**Uniqueness.** Suppose $z_0 \in A$ also satisfies $\|x - z_0\| = \delta$. Applying $(**)$ with $y = y_0$, $z = z_0$,

$$\|z_0 - y_0\|^2 \leq 2\delta^2 + 2\delta^2 - 4\delta^2 = 0,$$

thus $z_0 = y_0$.
