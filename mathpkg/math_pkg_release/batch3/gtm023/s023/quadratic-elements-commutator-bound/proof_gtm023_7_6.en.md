---
role: proof
locale: en
of_concept: quadratic-elements-commutator-bound
source_book: gtm023
source_chapter: "7"
source_section: "6"
---

Without loss of generality we may assume that $y \neq \pm x$. Then the elements $e, x, y$ are linearly independent, as is easily checked.

Since every element of $A$ satisfies a quadratic equation (by the fundamental theorem of algebra and the fact that $A$ is a division algebra), the elements $x + y$ and $x - y$ satisfy quadratic equations:

$$(x + y)^2 + \alpha(x + y) + 2\beta e = 0, \quad \alpha, \beta \in \mathbb{R},$$

$$(x - y)^2 + \gamma(x - y) + 2\delta e = 0, \quad \gamma, \delta \in \mathbb{R}.$$

Expanding the left-hand sides and using $x^2 = y^2 = -e$, we obtain

$$(x + y)^2 = x^2 + xy + yx + y^2 = -2e + xy + yx,$$
$$(x - y)^2 = x^2 - xy - yx + y^2 = -2e - (xy + yx).$$

Substituting these into the quadratic equations and adding them gives

$$(-2e + xy + yx) + \alpha(x + y) + 2\beta e + (-2e - xy - yx) + \gamma(x - y) + 2\delta e = 0,$$

which simplifies to

$$(\alpha + \gamma)x + (\alpha - \gamma)y + 2(\beta + \delta - 2)e = 0.$$

Since $e, x, y$ are linearly independent, the coefficients must vanish:

$$\alpha + \gamma = 0, \quad \alpha - \gamma = 0, \quad \beta + \delta = 2.$$

Hence $\alpha = 0$ and $\gamma = 0$.

Now the quadratic equations reduce to

$$(x + y)^2 = -2\beta e, \quad (x - y)^2 = -2\delta e.$$

Expanding the first equation:

$$x^2 + xy + yx + y^2 = -2e + xy + yx = -2\beta e,$$

so $xy + yx = 2(1 - \beta)e$.

From $\beta + \delta = 2$ and the fact that $x+y$ and $x-y$ satisfy quadratic equations with real coefficients (implying $\beta$ and $\delta$ are determined by the structure), we have $-2\beta = |x+y|^2 \geq 0$ and $-2\delta = |x-y|^2 \geq 0$, so $\beta \leq 0$ and $\delta \leq 0$. Combined with $\beta + \delta = 2$, we get $0 \leq \beta \leq 2$.

Setting $\lambda = 1 - \beta$, we obtain $-1 \leq \lambda \leq 1$ and

$$xy + yx = 2\lambda e.$$
