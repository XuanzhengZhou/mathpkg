---
role: proof
locale: en
of_concept: liouvilles-theorem
source_book: gtm055
source_chapter: "5"
source_section: "6"
---

Let $f$ be an entire function and $\alpha$ an arbitrary complex number. The Taylor series expansion
$$f(\lambda) = \sum_{n=0}^{\infty} \alpha_n (\lambda - \alpha)^n$$
of $f$ about $\alpha$ converges everywhere. Hence the Cauchy estimates hold for every $r > 0$. Thus $|\alpha_n| \leq M_r / r^n$ for every positive integer $n$ and every positive number $r$, where $M_r = \max\{|f(\zeta)| : |\zeta - \alpha| = r\}$. If $f$ is bounded, say $|f(\lambda)| \leq M$ for all $\lambda \in \mathbb{C}$, then $M_r \leq M$ for all $r$. Hence $|\alpha_n| \leq M / r^n$ for every $r > 0$. Letting $r \to \infty$, we obtain $\alpha_n = 0$ for all $n \geq 1$. Therefore $f(\lambda) = \alpha_0$ is constant.
