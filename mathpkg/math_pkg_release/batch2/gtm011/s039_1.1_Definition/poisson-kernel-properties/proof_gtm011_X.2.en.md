---
role: proof
locale: en
of_concept: poisson-kernel-properties
source_book: gtm011
source_chapter: "X"
source_section: "2.3"
---

\textbf{(a)} For a fixed value of $r$, $0 \leq r < 1$, the series (2.1) converges uniformly in $\theta$. So
$$\frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta) \, d\theta = \sum_{n=-\infty}^{\infty} r^{|n|} \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{in\theta} \, d\theta = 1,$$
since $\int_{-\pi}^{\pi} e^{in\theta} \, d\theta = 0$ for $n \neq 0$ and equals $2\pi$ for $n = 0$.

\textbf{(b)} From equation (2.2), $P_r(\theta) = (1 - r^2) |1 - re^{i\theta}|^{-2} > 0$ since $r < 1$. The remaining properties $P_r(-\theta) = P_r(\theta)$ and $2\pi$-periodicity follow directly from the definition.

\textbf{(c)} Let $0 < \delta < \theta \leq \pi$ and define $f: [\delta, \theta] \to \mathbb{R}$ by $f(t) = P_r(t)$. Since $f'(t) < 0$ on $(0, \pi)$ for $0 < r < 1$, $f$ is strictly decreasing, giving $P_r(\theta) < P_r(\delta)$.

\textbf{(d)} For $|\theta| \geq \delta$, we have $|1 - re^{i\theta}| \geq |1 - e^{i\delta}|/2$ for $r$ sufficiently close to $1$, so $P_r(\theta) = (1 - r^2)/|1 - re^{i\theta}|^2 \to 0$ uniformly as $r \to 1^-$.
