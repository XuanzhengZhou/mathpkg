---
role: proof
locale: en
of_concept: riesz-representation
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.12"
---

# Proof of Riesz Representation Theorem

**Theorem.** If $H$ is a Hilbert space, then for every continuous linear form $f \in H'$ there exists a unique vector $y \in H$ such that $f(x) = (x|y)$ for all $x \in H$.

*Proof.* If $f = 0$, take $y = \theta$; then $f(x) = 0 = (x|\theta)$ for all $x$.

Suppose $f \neq 0$. Let $N = \ker f = \{x \in H : f(x) = 0\}$. Since $f$ is continuous, $N$ is a closed linear subspace of $H$. Because $f \neq 0$, $N$ is a proper subspace, so $N \neq H$. By the orthogonal decomposition theorem (42.7), $N^\perp \neq \{\theta\}$ (otherwise $H = N \oplus \{\theta\} = N$, a contradiction). Choose a nonzero vector $w \in N^\perp$ and scale it to obtain $z = \frac{w}{f(w)}$; then $z \in N^\perp$ and $f(z) = 1$.

For any $x \in H$, consider the vector $x - f(x)z$. Applying $f$:

$$f(x - f(x)z) = f(x) - f(x)f(z) = f(x) - f(x) \cdot 1 = 0,$$

so $x - f(x)z \in \ker f = N$. Since $z \in N^\perp$, it is orthogonal to every vector in $N$; in particular,

$$0 = (x - f(x)z \mid z) = (x|z) - f(x)(z|z).$$

Solving for $f(x)$ yields

$$f(x) = \frac{(x|z)}{(z|z)} = \bigl(x \bigm| \|z\|^{-2} z\bigr).$$

Thus the vector $y = \|z\|^{-2}z$ satisfies $f(x) = (x|y)$ for all $x \in H$.

**Uniqueness.** If $y_1, y_2 \in H$ satisfy $(x|y_1) = (x|y_2)$ for all $x \in H$, then $(x|y_1 - y_2) = 0$ for all $x$. Taking $x = y_1 - y_2$ gives $\|y_1 - y_2\|^2 = 0$, hence $y_1 = y_2$.
