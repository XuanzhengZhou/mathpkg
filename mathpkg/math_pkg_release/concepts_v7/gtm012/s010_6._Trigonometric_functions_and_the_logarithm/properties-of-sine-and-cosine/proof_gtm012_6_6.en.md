---
role: proof
locale: en
of_concept: properties-of-sine-and-cosine
source_book: gtm012
source_chapter: "6"
source_section: "6. Trigonometric functions and the logarithm"
---

# Proof of Fundamental Properties of Sine and Cosine

**Theorem 6.2.** The functions $S$ and $C$ of Theorem 6.1 have the following properties.

(a) $S$ and $C$ are of class $C^\infty$ and real-valued. In fact,

$$S(x) = \frac{1}{2i}(e^{ix} - e^{-ix}), \qquad C(x) = \frac{1}{2}(e^{ix} + e^{-ix}),$$

so $e^{ix} = C(x) + iS(x)$ for all $x \in \mathbb{R}$.

(b) $S' = C$, $C' = -S$, and $S(x)^2 + C(x)^2 = 1$ for all $x \in \mathbb{R}$.

(c) There exists a smallest positive number $p$ such that $C(p) = 0$.

(d) If $p$ is the number in (c), then

$$S(x + 4p) = S(x), \qquad C(x + 4p) = C(x), \qquad \text{all } x \in \mathbb{R}.$$

*Proof.* Since the exponential function $\exp(ax)$ is of class $C^\infty$ as a function of $x$ for each $a \in \mathbb{C}$, the integral representations

$$S(x) = \frac{1}{2i}(e^{ix} - e^{-ix}), \qquad C(x) = \frac{1}{2}(e^{ix} + e^{-ix})$$

show that $S$ and $C$ are of class $C^\infty$. Since $(e^{ix})^* = e^{-ix}$ (where $*$ denotes complex conjugation), $S$ and $C$ are real-valued. In fact,

$$C(x) = \operatorname{Re}(e^{ix}), \qquad S(x) = \operatorname{Im}(e^{ix}),$$

so

$$e^{ix} = C(x) + iS(x).$$

This proves (a).

Differentiation of the integral formulas gives

$$S'(x) = \frac{1}{2i}(ie^{ix} + ie^{-ix}) = \frac{1}{2}(e^{ix} + e^{-ix}) = C(x),$$

$$C'(x) = \frac{1}{2}(ie^{ix} - ie^{-ix}) = \frac{i}{2}(e^{ix} - e^{-ix}) = -\frac{1}{2i}(e^{ix} - e^{-ix}) = -S(x).$$

Differentiation of $S(x)^2 + C(x)^2$ shows that it is constant:

$$\frac{d}{dx}\big(S(x)^2 + C(x)^2\big) = 2S(x)S'(x) + 2C(x)C'(x) = 2S(x)C(x) - 2C(x)S(x) = 0.$$

The value at $x = 0$ is $S(0)^2 + C(0)^2 = 0^2 + 1^2 = 1$. Hence $S(x)^2 + C(x)^2 = 1$ for all $x$. This proves (b).

To prove (c), suppose that $C(x) \neq 0$ for all $x > 0$. Since $C(0) = 1$ and $C$ is continuous, the Intermediate Value Theorem implies $C(x) > 0$ for all $x > 0$. Since $S' = C$, $S$ is then strictly increasing for $x \geq 0$. In particular, $S(x) \geq S(1) > 0$ for all $x \geq 1$ (note $S(1) > 0$ because $S(0) = 0$ and $S$ is strictly increasing). But then

$$0 < C(x) = C(1) + \int_1^x C'(t)\,dt = C(1) - \int_1^x S(t)\,dt$$

$$\leq C(1) - \int_1^x S(1)\,dt = C(1) - (x - 1)S(1), \qquad x \geq 1.$$

For large $x$ the last expression is negative, a contradiction. Therefore $C(x) = 0$ for some $x > 0$. Since $C$ is continuous and $C(0) = 1$, the set $\{x > 0 : C(x) = 0\}$ is closed and nonempty, so it has a smallest element. Call this smallest positive number $p$.

To prove (d), note that from (b) we have $S(p)^2 = 1$ since $C(p) = 0$. Moreover, since $S' = C > 0$ on $(0, p)$, $S$ is strictly increasing there from $S(0) = 0$, so $S(p) = 1$.

Now define functions $\tilde{S}(x) = S(x + p)$ and $\tilde{C}(x) = C(x + p)$. These satisfy the same differential equations:

$$\tilde{S}''(x) + \tilde{S}(x) = S''(x + p) + S(x + p) = 0,$$
$$\tilde{C}''(x) + \tilde{C}(x) = C''(x + p) + C(x + p) = 0.$$

Their initial values are $\tilde{S}(0) = S(p) = 1$, $\tilde{S}'(0) = S'(p) = C(p) = 0$, and $\tilde{C}(0) = C(p) = 0$, $\tilde{C}'(0) = C'(p) = -S(p) = -1$. By uniqueness of solutions to the initial value problem (Theorem 6.1), we obtain

$$\tilde{S}(x) = C(x), \qquad \tilde{C}(x) = -S(x),$$

that is,

$$S(x + p) = C(x), \qquad C(x + p) = -S(x).$$

Iterating these relations:

$$S(x + 2p) = S((x + p) + p) = C(x + p) = -S(x),$$
$$C(x + 2p) = C((x + p) + p) = -S(x + p) = -C(x),$$
$$S(x + 4p) = S((x + 2p) + 2p) = -S(x + 2p) = S(x),$$
$$C(x + 4p) = C((x + 2p) + 2p) = -C(x + 2p) = C(x).$$

Thus $S$ and $C$ are periodic with period $4p$. $\square$
