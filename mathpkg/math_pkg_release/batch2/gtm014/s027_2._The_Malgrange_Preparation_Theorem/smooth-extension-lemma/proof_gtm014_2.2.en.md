---
role: proof
locale: en
of_concept: smooth-extension-lemma
source_book: gtm014
source_chapter: "2"
source_section: "2. The Malgrange Preparation Theorem"
---

It is sufficient to prove the lemma for $h \equiv 0$. For let $F_1$ be the extension for $g - h$ and $0$; then $F = F_1 + h$ is the required extension for $g$ and $h$. So assume $h \equiv 0$.

Choose coordinates $y_1, \ldots, y_n$ on $\mathbb{R}^n$ so that $V$ is defined by the equations $y_1 = \cdots = y_j = 0$ and $W$ is defined by the equations $y_{j+1} = \cdots = y_k = 0$. This is possible since $V + W = \mathbb{R}^n$.

Let $\rho$ be a smooth function on $\mathbb{R}$ such that $\rho(t) = 1$ for $|t| \leq 1/2$, $\rho(t) = 0$ for $|t| \geq 1$, and $0 \leq \rho(t) \leq 1$ for all $t$. Let $\{\mu_l\}_{l=0}^{\infty}$ be an increasing sequence of real numbers with $\lim_{l \to \infty} \mu_l = \infty$, to be chosen later.

Define

$$F(y) = \sum_{\alpha = (a_1, \ldots, a_j, 0, \ldots, 0)} \frac{y^\alpha}{\alpha!} \frac{\partial^{|\alpha|} g}{\partial y^\alpha}(0, \ldots, 0, y_{j+1}, \ldots, y_n) \; \rho\!\left( \mu_{|\alpha|} \sum_{i=1}^{j} y_i^2 \right).$$

The right-hand side is well-defined since for any given $y = (y_1, \ldots, y_n)$, only finitely many terms are nonzero: $\rho(\mu_{|\alpha|} \sum y_i^2) = 0$ whenever $\mu_{|\alpha|} \sum y_i^2 \geq 1$, i.e., whenever $\sum y_i^2 \geq 1/\mu_{|\alpha|}$.

For $y$ with $y_1 = \cdots = y_j = 0$ (i.e., $y \in V$), we have $\sum y_i^2 = 0$, so $\rho(0) = 1$ and the sum reduces to the Taylor expansion of $g$ along $W$, hence $F$ and all its derivatives agree with $g$ on $V$.

To show that $F$ is smooth on a neighborhood of $0$ in $\mathbb{R}^n$:

Let $K$ be a compact neighborhood of $0$ in $\mathbb{R}^n$ contained in the domain of $g$ (along $W$). Let

$$M_{l}^{\beta} = \sup_{x \in K \cap W} \left| \frac{\partial^{|\beta|}}{\partial y^\beta} \left( \frac{\partial^{l} g}{\partial y^\alpha} \right)(0, \ldots, 0, y_{j+1}, \ldots, y_n) \right|.$$

Differentiating the series termwise and estimating as in the series construction lemma (where one constructs a smooth function from a formal power series using rapidly shrinking bump functions), the $\mu_l$ can be chosen to increase sufficiently rapidly to infinity so that all differentiated series converge uniformly on $\mathbb{R}^n \times K$. This guarantees that $F$ is smooth on a neighborhood of $0$. $\square$
