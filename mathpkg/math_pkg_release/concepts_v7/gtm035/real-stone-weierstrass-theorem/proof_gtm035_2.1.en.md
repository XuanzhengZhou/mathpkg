---
role: proof
locale: en
of_concept: real-stone-weierstrass-theorem
source_book: gtm035
source_chapter: "2"
source_section: "2.1"
---

# Proof of Real Stone-Weierstrass Theorem

**Theorem 2.1 (Real Stone-Weierstrass Theorem).** Let $X$ be a compact Hausdorff space and let $\mathfrak{A}$ be a subalgebra of $C_{\mathbb{R}}(X)$ which contains the constants. If $\mathfrak{A}$ separates the points of $X$, then $\mathfrak{A}$ is dense in $C_{\mathbb{R}}(X)$.

## Proof

The result is deduced from the Krein-Milman theorem (Proposition 2.2). Let $\mu$ be a real measure on $X$ with $\mu \perp \mathfrak{A}$. We must show that $\mu = 0$.

Let

$$K = \{ \sigma \in (C_{\mathbb{R}}(X))^* : \|\sigma\| \leq 1,\; \sigma \perp \mathfrak{A} \}.$$

Then $K$ is a nonempty, compact, convex subset of the dual space in the weak-$^*$ topology. By Proposition 2.2 (Krein-Milman), $K$ has an extreme point, call it $\sigma$.

We claim that $\sigma = 0$. Suppose not. Since $\mathfrak{A}$ separates points, there exists $g \in \mathfrak{A}$ and points $x_1, x_2 \in X$ such that $g(x_1) \neq g(x_2)$. Choose $0 < q < 1$. Then

$$\sigma = g \cdot \sigma + (1 - g)\sigma = \|g\sigma\| \frac{g\sigma}{\|g\sigma\|} + \|(1-g)\sigma\| \frac{(1-g)\sigma}{\|(1-g)\sigma\|}.$$

Moreover,

$$\|g\sigma\| + \|(1-g)\sigma\| = \int g\,d|\sigma| + \int(1-g)\,d|\sigma| = \int d|\sigma| = \|\sigma\| = 1.$$

Thus $\sigma$ is a convex combination of $g\sigma/\|g\sigma\|$ and $(1-g)\sigma/\|(1-g)\sigma\|$, both of which lie in $K$. Since $\sigma$ is an extreme point, we must have

$$\sigma = \frac{g\sigma}{\|g\sigma\|},$$

which implies that $g$ is constant almost everywhere with respect to $d|\sigma|$. But $g(x_1) \neq g(x_2)$ and $g$ is continuous -- a contradiction.

Hence $K = \{0\}$, so $\mu \in (C_{\mathbb{R}}(X))^*$ with $\mu \perp \mathfrak{A}$ implies $\mu = 0$. Thus $\mathfrak{A}$ is dense in $C_{\mathbb{R}}(X)$. $\square$
