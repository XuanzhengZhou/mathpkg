---
role: proof
locale: en
of_concept: hilbert-symbol-norm-characterization
source_book: gtm007
source_chapter: "III"
source_section: "§1. Local properties"
---

If $b$ is the square of an element $c$, the equation $z^2 - a x^2 - b y^2 = 0$ has $(c, 0, 1)$ for a solution, hence $(a, b) = 1$, and the proposition is clear in this case since $k_b = k$ and $N k_b^* = k^*$.

Otherwise, $k_b$ is quadratic over $k$; if $\beta$ denotes a square root of $b$, every element $\xi \in k_b$ can be written $z + \beta y$ with $y, z \in k$ and the norm $N(\xi)$ of $\xi$ is equal to $z^2 - b y^2$.

If $a \in N k_b^*$, there exist $y, z \in k$ such that $a = z^2 - b y^2$. Then $(z, 1, y)$ is a nontrivial solution of $z^2 - a x^2 - b y^2 = 0$, hence $(a, b) = 1$.

Conversely, if $(a, b) = 1$, there exists $(z, x, y) \neq (0, 0, 0)$ such that $z^2 - a x^2 - b y^2 = 0$. If $x = 0$, then $z^2 - b y^2 = 0$, which implies $b = (z/y)^2$ (since $(z, x, y) \neq (0, 0, 0)$ forces $y \neq 0$), contradicting that $b$ is not a square. Thus $x \neq 0$, and we may write
$$
a = \left(\frac{z}{x}\right)^2 - b \left(\frac{y}{x}\right)^2 = N\left(\frac{z}{x} + \beta \frac{y}{x}\right) \in N k_b^*.
$$

This completes the proof. From this characterization one deduces that the norm group satisfies:
$$
a' \in N k_b^* \iff a a' \in N k_b^*,
$$
and further properties i), ii), iv) of the norm group, which translate into corresponding properties of the Hilbert symbol.
