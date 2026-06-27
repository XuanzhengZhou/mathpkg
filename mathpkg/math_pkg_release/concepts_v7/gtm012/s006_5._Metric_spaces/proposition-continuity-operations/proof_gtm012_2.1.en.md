---
role: proof
locale: en
of_concept: proposition-continuity-operations
source_book: gtm012
source_chapter: "2"
source_section: "1. Continuity, uniform continuity, and compactness"
---

# Proof of Proposition 1.1: Continuity of Algebraic Operations

Suppose $(S, d)$ is any metric space, and suppose $f, g: S \to \mathbb{C}$ are functions which are continuous at $x \in S$.

**Sum $f + g$.** Given $\varepsilon > 0$, choose $\delta_1, \delta_2 > 0$ such that $|f(y) - f(x)| < \varepsilon/2$ when $d(y, x) < \delta_1$, and $|g(y) - g(x)| < \varepsilon/2$ when $d(y, x) < \delta_2$. Let $\delta = \min\{\delta_1, \delta_2\}$. Then if $d(y, x) < \delta$,

$$|(f + g)(y) - (f + g)(x)| \leq |f(y) - f(x)| + |g(y) - g(x)| < \varepsilon/2 + \varepsilon/2 = \varepsilon.$$

Thus $f + g$ is continuous at $x$.

**Scalar multiple $af$.** Given $\varepsilon > 0$, choose $\delta > 0$ such that $|f(y) - f(x)| < \varepsilon/(|a| + 1)$ when $d(y, x) < \delta$. Then

$$|(af)(y) - (af)(x)| = |a| \, |f(y) - f(x)| < |a| \cdot \frac{\varepsilon}{|a| + 1} < \varepsilon.$$

Thus $af$ is continuous at $x$.

**Product $fg$.** Choose $M > \max\{|f(x)|, |g(x)|, 1\}$. Given $\varepsilon > 0$, choose $\delta_1, \delta_2 > 0$ such that $|f(y) - f(x)| < \varepsilon/2M$ when $d(y, x) < \delta_1$, and $|g(y) - g(x)| < \varepsilon/2M$ when $d(y, x) < \delta_2$. Also choose $\delta_3 > 0$ such that $|f(y) - f(x)| < 1$ when $d(y, x) < \delta_3$. Let $\delta = \min\{\delta_1, \delta_2, \delta_3\}$. If $d(y, x) < \delta$, then

$$\begin{aligned}
|(fg)(y) - (fg)(x)| &= |f(y)g(y) - f(x)g(x)| \\
&= |f(y)g(y) - f(y)g(x) + f(y)g(x) - f(x)g(x)| \\
&\leq |f(y)| \, |g(y) - g(x)| + |f(y) - f(x)| \, |g(x)| \\
&\leq |f(y)| \cdot \frac{\varepsilon}{2M} + M \cdot \frac{\varepsilon}{2M}.
\end{aligned}$$

But also

$$|f(y)| = |f(y) - f(x) + f(x)| \leq |f(y) - f(x)| + |f(x)| < 1 + |f(x)| \leq M,$$

so $|(fg)(y) - (fg)(x)| < M \cdot \varepsilon/2M + \varepsilon/2 = \varepsilon$. Thus $fg$ is continuous at $x$.

**Quotient $f/g$.** Suppose $g(x) \neq 0$. Choose $r > 0$ so that $|g(y) - g(x)| < \frac{1}{2}|g(x)|$ if $d(y, x) < r$. Then if $d(y, x) < r$ we have

$$|g(x)| = |g(y) + g(x) - g(y)| \leq |g(y)| + \tfrac{1}{2}|g(x)|,$$

so $|g(y)| \geq \frac{1}{2}|g(x)| > 0$. Thus $1/g$ is defined on $B_r(x)$. Since the product of functions continuous at $x$ is continuous at $x$, we only need to show that $1/g$ is continuous at $x$. But if $y \in B_r(x)$, then

$$|1/g(y) - 1/g(x)| = \frac{|g(y) - g(x)|}{|g(y)| \, |g(x)|} \leq K \, |g(y) - g(x)|,$$

where $K = 2/|g(x)|^2$. Since $g$ is continuous at $x$, it follows that $1/g$ is continuous at $x$. Consequently, $f/g = f \cdot (1/g)$ is continuous at $x$. $\square$
