---
role: proof
locale: en
of_concept: best-approximation-complete-convex
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.13"
---

# Proof of Best Approximation from a Complete Convex Set in an Inner Product Space

**Theorem (Exercise 42.13).** Let $A$ be a complete, nonempty convex subset of an inner product space $E$. Then, given any $x \in E$, there exists a unique $y_0 \in A$ such that $\|x - y_0\| \leq \|x - y\|$ for all $y \in A$.

*Proof.* The argument is identical to that of Theorem (42.3), with the completeness of $A$ replacing the joint hypothesis "Hilbert space $H$ and closed $A$" used there.

Let $\delta = \inf \{\|x - y\| : y \in A\}$. Choose a sequence $(y_n)$ in $A$ such that $\|x - y_n\| \to \delta$.

By the parallelogram law, for any $y, z \in E$,

$$\|z - y\|^2 = 2\|x - y\|^2 + 2\|x - z\|^2 - 4\left\|x - \tfrac{1}{2}(y+z)\right\|^2.$$

Since $\tfrac{1}{2}(y+z) \in A$ by convexity, $\|x - \tfrac{1}{2}(y+z)\| \geq \delta$. Hence

$$\|z - y\|^2 \leq 2\|x - y\|^2 + 2\|x - z\|^2 - 4\delta^2.$$

Applying this with $y = y_n$, $z = y_m$ yields

$$\|y_m - y_n\|^2 \leq 2\|x - y_n\|^2 + 2\|x - y_m\|^2 - 4\delta^2 \to 0$$

as $m, n \to \infty$. Thus $(y_n)$ is a Cauchy sequence in $A$. Since $A$ is complete, there exists $y_0 \in A$ with $\|y_n - y_0\| \to 0$. By continuity of the norm, $\|x - y_0\| = \delta$, proving existence.

Uniqueness follows from the same inequality: if $z_0 \in A$ also satisfies $\|x - z_0\| = \delta$, then

$$\|z_0 - y_0\|^2 \leq 2\delta^2 + 2\delta^2 - 4\delta^2 = 0,$$

so $z_0 = y_0$.
