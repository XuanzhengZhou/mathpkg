---
role: exercise
locale: en
chapter: "Chapter 3"
section: "§5. Inversion formula, moments and semi-invariants"
exercise_number: 9
---

# Exercise 9

Let $\xi$ be an integral-valued random variable and $\varphi_\xi(t)$ its characteristic function. Show that

$$P(\xi = k) = \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{-ikt} \varphi_\xi(t) dt, \quad k \in \mathbb{Z}.$$

**Hint:** For an integral-valued random variable, the characteristic function is $\varphi_\xi(t) = \sum_{n=-\infty}^{\infty} P(\xi = n) e^{int}$. Multiply by $e^{-ikt}$ and integrate over $[-\pi, \pi]$, using the orthogonality relation $\frac{1}{2\pi} \int_{-\pi}^{\pi} e^{i(n-k)t} dt = \delta_{nk}$.
