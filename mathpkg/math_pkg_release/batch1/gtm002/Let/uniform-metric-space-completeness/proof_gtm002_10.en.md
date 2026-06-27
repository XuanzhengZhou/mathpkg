---
role: proof
locale: en
of_concept: uniform-metric-space-completeness
source_book: gtm002
source_chapter: "10"
source_section: "10. Examples of Metric Spaces"
---

Let $\{f_n\}$ be any Cauchy sequence in $C$, say $\varrho(f_i, f_j) \leq \varepsilon$ for all $i, j \geq n(\varepsilon)$. Then

$$|f_i(x) - f_j(x)| \leq \varepsilon \quad \text{for all} \quad i, j \geq n(\varepsilon) \quad \text{and} \quad a \leq x \leq b.$$

Hence, for each $x$ in $[a, b]$, $\{f_n(x)\}$ is a Cauchy sequence of real numbers. It therefore converges to a limit $f(x)$. Letting $j \to \infty$ we see that $|f_i(x) - f(x)| \leq \varepsilon$ for all $i \geq n(\varepsilon)$ and all $x$ in $[a, b]$. Thus $f_i$ converges to $f$ uniformly on $[a, b]$. By the well-known theorem that the uniform limit of continuous functions is continuous, $f$ is continuous on $[a, b]$. Hence $f_i \to f$ in $C$.
