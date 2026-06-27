---
role: proof
locale: en
of_concept: minkowski-functional
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Minkowski functional — balanced convex body as closed unit ball of a seminorm

Let $E$ be a TVS over $\mathbb{K}$ and let $B$ be a balanced, convex body in $E$ (i.e., a balanced, closed convex set with nonempty interior).

Define $B(x) = \{\alpha > 0 : x \in \alpha B\}$ for each $x \in E$, and set

$$p(x) = \inf B(x).$$

Since $B$ has nonempty interior, $B$ is absorbent, hence $B(x)$ is nonempty and $p(x)$ is a well-defined nonnegative real number.

**Properties of $B(x)$:**
- (i) $B(\theta) = (0, +\infty)$, so $p(\theta) = 0$.
- (ii) If $|\mu| = 1$, then $B(\mu x) = B(x)$ since $B$ is balanced (so $\mu B = B$).
- (iii) If $\rho > 0$, then $B(\rho x) = \rho B(x)$. Indeed, $\alpha \in B(\rho x) \iff \rho x \in \alpha B \iff x \in \rho^{-1}\alpha B \iff \rho^{-1}\alpha \in B(x) \iff \alpha \in \rho B(x)$.
- (iv) If $\lambda \in \mathbb{K}, \lambda \neq 0$, then writing $\lambda = \rho\mu$ with $\rho = |\lambda| > 0$ and $|\mu| = 1$, we have $B(\lambda x) = B(\mu\rho x) = B(\rho x) = \rho B(x) = |\lambda|B(x)$ by (ii) and (iii).
- (v) $B(x) + B(y) \subset B(x + y)$, i.e., if $\alpha \in B(x)$ and $\beta \in B(y)$, then $\alpha + \beta \in B(x + y)$. This follows from $x + y \in \alpha B + \beta B = (\alpha + \beta)B$.
- (vi) If $\alpha \in B(x)$ and $\beta > \alpha$, then $\beta \in B(x)$, because $x \in \alpha B \subset \beta B$ (since $B$ is balanced).

From these properties, $p$ is a seminorm: $p(x) \geq 0$ by definition; $p(\theta) = 0$ by (i); $p(\lambda x) = |\lambda|p(x)$ by (iv); and the triangle inequality $p(x + y) \leq p(x) + p(y)$ follows from (v) by taking infimum.

Moreover, $\{x : p(x) \leq 1\} = B$ and $\{x : p(x) < 1\} = \operatorname{int} B$, and $p$ is continuous on $E$. Uniqueness follows from (37.2): if two seminorms have the same closed unit ball, they are equal.
