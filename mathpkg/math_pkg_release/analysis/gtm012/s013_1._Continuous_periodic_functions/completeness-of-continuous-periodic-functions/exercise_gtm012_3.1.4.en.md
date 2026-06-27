---
role: exercise
locale: en
chapter: "3"
section: "1. Continuous periodic functions"
exercise_number: 4
---

# Exercise 4

Suppose $d'$ is the metric associated with the norm $|u|'$ in Exercise 3. Show that $\mathcal{C}$ is not complete with respect to this metric.

**Hint:** Take a sequence of functions $(u_n)_{n=1}^{\infty}$ in $\mathcal{C}$ such that

$$0 \leq u_n(x) \leq 1, \quad x \in \mathbb{R}, \quad n = 1, 2, \ldots,$$

$$u_n(x) = 0, \quad x \in [0, \pi/2 - 1/n] \cup [3\pi/2 + 1/n, 2\pi],$$

$$u_n(x) = 1, \quad x \in [\pi/2, 3\pi/2].$$

Then $|u_n - u_m|' \to 0$ as $n, m \to \infty$. If $u \in \mathcal{C}$, there is an open interval $(\pi/2 - \delta, \pi/2 + \delta)$ on which either $|u(x)| > \frac{1}{3}$ or $|u(x) - 1| > \frac{1}{3}$. Show that $|u_n - u|' > \delta/6\pi$ for large values of $n$.
