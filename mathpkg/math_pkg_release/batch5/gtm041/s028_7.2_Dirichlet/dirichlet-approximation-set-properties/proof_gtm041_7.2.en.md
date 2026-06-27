---
role: proof
locale: en
of_concept: dirichlet-approximation-set-properties
source_book: gtm041
source_chapter: "7"
source_section: "7.2"
---

**(a)** By Theorem 7.3, $S(\theta)$ is nonempty.

**(b)** Assume $\theta$ is irrational and define

$$\alpha = \inf \left\{ \left| \theta - \frac{h}{k} \right| : (h, k) \in S(\theta) \right\}.$$

If $S(\theta)$ were finite, then $\alpha > 0$ (since $\theta$ irrational implies $\theta \neq h/k$ for any rational $h/k$). Choose $N$ such that $1/N < \alpha$. By Theorem 7.2 there exists a pair $(h, k)$ with $(h, k) = 1$, $k \leq N$, and $|k\theta - h| < 1/N$. Then

$$\left| \theta - \frac{h}{k} \right| < \frac{1}{kN}.$$

Now $1/(kN) \leq 1/k^2$ so the pair $(h, k) \in S(\theta)$. But we also have

$$\frac{1}{kN} \leq \frac{1}{N} < \alpha, \quad \text{so} \quad \left| \theta - \frac{h}{k} \right| < \alpha,$$

contradicting the definition of $\alpha$. This shows that $S(\theta)$ cannot be finite if $\theta$ is irrational.

**(c)** Assume that all pairs $(h, k)$ in $S(\theta)$ have $k \leq M$ for some $M$. We will show that this leads to a contradiction by showing that the number of choices for $h$ is also bounded. If $(h, k) \in S(\theta)$ we have

$$|k\theta - h| < \frac{1}{k} \leq 1,$$

so

$$|h| = |h - k\theta + k\theta| \leq |h - k\theta| + |k\theta| < 1 + |k\theta| \leq 1 + M|\theta|.$$

Therefore the number of choices for $h$ is bounded, contradicting the fact that $S(\theta)$ is infinite.

**(d)** Assume $\theta$ is rational, say $\theta = a/b$, where $(a, b) = 1$ and $b > 0$. Then the pair $(a, b) \in S(\theta)$ because $\theta - a/b = 0$. Now we assume that $S(\theta)$ is an infinite set and obtain a contradiction. If $S(\theta)$ is infinite then by part (c) there is a pair $(h, k)$ in $S(\theta)$ with $k > b$. For this pair we have

$$0 < \left| \frac{a}{b} - \frac{h}{k} \right| < \frac{1}{k^2},$$

from which we find $0 < |ak - bh| < b/k < 1$. This is a contradiction because $ak - bh$ is an integer.

**Conclusion.** Theorem 7.4 shows that a real number $\theta$ is irrational if, and only if, there are infinitely many rational numbers $h/k$ with $(h, k) = 1$ such that $|\theta - h/k| < 1/k^2$.
