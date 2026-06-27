---
role: exercise
locale: en
chapter: "17"
section: "19"
exercise_number: "N"
---

Let $(X, \mathbf{S}, \mu)$ be a measure space, and let $\mathcal{E}$ be a Banach space. Prove that if $\Phi$ is a measurable mapping of $X$ into $\mathcal{E}$ and $\Psi$ is a measurable mapping of $X$ into the dual space $\mathcal{E}^*$, then $x \rightarrow \Psi(x)(\Phi(x))$ is a measurable complex-valued function on $X$. Show also that if $p$ and $q$ are Hölder conjugates, and if $\Phi$ and $\Psi$ belong to $\mathcal{L}_p(X; \mathcal{E})$ and $\mathcal{L}_q(X; \mathcal{E}^*)$, respectively, then

$$\int_X |\Psi(x)(\Phi(x))| d\mu(x) \leq \|\Phi\|_p \|\Psi\|_q.$$

Hence, setting $\Omega(\Phi) = \int_X \Psi(x)(\Phi(x)) d\mu(x)$ defines a bounded linear functional on $\mathcal{L}_p(X; \mathcal{E})$ satisfying $\|\Omega\| \leq \|\Psi\|_q$.
