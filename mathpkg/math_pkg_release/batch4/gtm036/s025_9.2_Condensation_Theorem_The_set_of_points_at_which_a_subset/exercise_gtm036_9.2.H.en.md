---
role: exercise
locale: en
chapter: "9"
section: "9.2"
exercise_number: "H"
---

**Additive Set Functions.** Let $\mathcal{S}$ be a $\sigma$-ring of subsets of a set $X$ and $\{\phi_n\}$ a sequence of finite, countably additive set functions on $\mathcal{S}$ such that $\lim_n \phi_n(A)$ exists for every $A$ in a subfamily $\mathcal{S}_0$ of $\mathcal{S}$. Show that there exists a finite measure $\nu$ on $\mathcal{S}$ such that each $\phi_n$ is absolutely continuous with respect to $\nu$. Conclude that the limit $\phi = \lim \phi_n$ is countably additive.

*Hint:* Let $\mu_n$ be the total variation of $\phi_n$, and define $\nu = \sum 2^{-n}(1 + c_n)^{-1} \mu_n$ where $c_n = \sup\{\mu_n(A) : A \in \mathcal{S}\} < \infty$.
