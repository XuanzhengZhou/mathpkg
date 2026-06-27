---
role: exercise
locale: en
chapter: "Chapter 3"
section: "§5. Inversion formula, moments and semi-invariants"
exercise_number: 15
---

# Exercise 15

Let $(m_n)_{n \geq 1}$ be the sequence of moments of a random variable $X$ with distribution function $F = F(x)$ ($m_k = \int_{-\infty}^{\infty} x^k dF(x)$). Show that $(m_n)_{n \geq 1}$ determines $F = F(x)$ uniquely whenever the series $\sum_{k=1}^{\infty} \frac{m_k}{k!} s^k$ absolutely converges for some $s > 0$.

**Hint:** The absolute convergence of $\sum m_k s^k/k!$ implies that the characteristic function $\varphi(t) = \sum (it)^k m_k/k!$ converges for $|t| \leq s$ and is analytic. Then use the analytic continuation argument as in the proof of Theorem 7.
