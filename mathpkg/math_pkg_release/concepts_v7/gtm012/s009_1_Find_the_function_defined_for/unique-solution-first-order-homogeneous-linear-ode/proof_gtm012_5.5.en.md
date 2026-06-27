---
role: proof
locale: en
of_concept: unique-solution-first-order-homogeneous-linear-ode
source_book: gtm012
source_chapter: "5"
source_section: "5"
---

# Proof of Unique Solution of First-Order Homogeneous Linear ODE

**Theorem 5.1.** For each $a, c \in \mathbb{C}$ there is a unique continuously differentiable function $f: \mathbb{R} \to \mathbb{C}$ such that

$$f(0) = c, \quad f'(x) = a f(x), \quad x \in \mathbb{R}. \tag{5.3}$$

This function is

$$f(x) = c E(ax) = c \sum_{n=0}^{\infty} (n!)^{-1} a^n x^n. \tag{5.4}$$

**Proof.** We first show that the function defined by (5.4) indeed satisfies (5.3). The series for $E(ax)$ can be differentiated termwise by Theorem 4.4, yielding

$$\frac{d}{dx} E(ax) = \sum_{n=1}^{\infty} (n!)^{-1} a^n \cdot n x^{n-1} = a \sum_{n=1}^{\infty} ((n-1)!)^{-1} a^{n-1} x^{n-1} = a E(ax).$$

Moreover, $E(a \cdot 0) = E(0) = 1$. Hence $f(x) = c E(ax)$ satisfies $f(0) = c$ and $f'(x) = a f(x)$, so existence is established.

For uniqueness, suppose $f$ is any solution of (5.3). Define $g(x) = E(-ax)$. As shown above, $g'(x) = -a g(x)$. Consider the product $fg$:

$$(fg)'(x) = f'(x) g(x) + f(x) g'(x) = a f(x) g(x) + f(x) (-a g(x)) = a f(x) g(x) - a f(x) g(x) = 0.$$

Therefore $fg$ is constant on $\mathbb{R}$, and

$$f(x) g(x) = f(0) g(0) = c \cdot E(0) = c \cdot 1 = c, \quad \text{for all } x \in \mathbb{R}.$$

Since $g(x) = E(-ax)$ satisfies $g(x) E(ax) = E(-ax) E(ax) = E(0) = 1$ (as shown by the power series multiplication), we have $g(x) \neq 0$ for all $x$. Hence

$$f(x) = \frac{c}{g(x)} = c E(ax), \quad \text{for all } x \in \mathbb{R}.$$

Thus $f$ is uniquely determined. $\square$
