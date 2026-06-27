---
role: proof
locale: en
of_concept: completeness-of-uniform-metric-space-of-continuous-functions
source_book: gtm002
source_chapter: "10"
source_section: "Examples of Metric Spaces"
---

Let $\{f_n\}$ be any Cauchy sequence in $(C[a, b], \varrho)$. Given $\varepsilon > 0$, there exists $n(\varepsilon)$ such that $\varrho(f_i, f_j) \leq \varepsilon$ for all $i, j \geq n(\varepsilon)$. Then by definition of the uniform metric,
$$
|f_i(x) - f_j(x)| \leq \varepsilon \quad \text{for all} \quad i, j \geq n(\varepsilon) \quad \text{and} \quad a \leq x \leq b.
$$

Hence, for each fixed $x \in [a, b]$, the sequence $\{f_n(x)\}$ is a Cauchy sequence of real numbers. Since $\mathbb{R}$ is complete, it converges to a limit, which we denote by $f(x)$. Letting $j \to \infty$ in the inequality above, we obtain
$$
|f_i(x) - f(x)| \leq \varepsilon \quad \text{for all} \quad i \geq n(\varepsilon) \quad \text{and} \quad a \leq x \leq b.
$$
Thus $f_i$ converges to $f$ uniformly on $[a, b]$. By the well-known theorem that the uniform limit of continuous functions is continuous, it follows that $f$ is continuous on $[a, b]$, i.e., $f \in C[a, b]$. Hence $f_i \to f$ in the metric $\varrho$, proving that $(C[a, b], \varrho)$ is complete.
