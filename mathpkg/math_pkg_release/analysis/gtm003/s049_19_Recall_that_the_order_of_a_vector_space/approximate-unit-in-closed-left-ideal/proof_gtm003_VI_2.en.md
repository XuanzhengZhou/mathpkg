---
role: proof
locale: en
of_concept: approximate-unit-in-closed-left-ideal
source_book: gtm003
source_chapter: "VI"
source_section: "2"
---

Suppose first that $A$ is unital and $x = x^* \in J$. Define $f_n(t) = n t^2 / (1 + n t^2)$ for $n \in \mathbf{N}$ and $t \in \mathbf{R}$. From Corollary 1 to Theorem 2.2, we conclude $\sigma(f_n(x)) \subset [0, 1]$ and $\sigma(e - f_n(x)) \subset [0, 1]$. Define $e_n := f_n(x)$. Then $e_n = n(e + n x^2)^{-1} x^2 \in J$. With $g_n(t) := t^2(1 - f_n(t))$, we obtain $\sigma(x^2(e - e_n)) = \sigma(g_n(x)) = g_n(\sigma(x)) \subset [0, 1/n]$, hence by 2.1, $\|x^2(e - e_n)\| \leq 1/n$. Since $x$ and $e - e_n$ are self-adjoint and commute, $\|e - e_n\| \leq 1$, so $\|x - x e_n\|^2 = \|x^2(e - e_n)\|^2 \leq \|x^2(e - e_n)\| \leq 1/n$.

If $x$ is not self-adjoint, construct a similar sequence $(e_n')$ with respect to $x^*x$. Then $\|(x^*x)(e - e_n')\| \to 0$ as $n \to \infty$, and $\|x - x e_n'\|^2 = \|(e - e_n')x^*x(e - e_n')\| \leq \|x^*x(e - e_n')\|$.

Finally, if $A$ is not unital, the preceding construction still applies to the unitization $\tilde{A}$ of $A$, because the ideal $J$ is closed in $\tilde{A}$ as well.

For general $x \in J$ (not necessarily a single element), one constructs an approximate unit for the whole ideal by taking the net of finite sums of such $e_n$'s, ordered by inclusion. The properties extend by standard arguments.
