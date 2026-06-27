---
role: proof
locale: en
of_concept: picard-iteration-for-linear-differential-equations
source_book: gtm023
source_chapter: "8"
source_section: "8.27"
---

Define $\varphi_0(t) = \iota$ and $\varphi_{n+1}(t) = \iota + \int_{t_0}^{t} \psi(t) \circ \varphi_n(t) \, dt$. Let $\Delta_n(t) = \varphi_n(t) - \varphi_{n-1}(t)$. Then $\Delta_n(t) = \int_{t_0}^{t} \psi(t) \circ \Delta_{n-1}(t) \, dt$ for $n \geq 2$, and $\Delta_1(t) = \int_{t_0}^{t} \psi(t) \, dt$.

Set $M = \max_{t_0 \leq t \leq t_1} |\psi(t)|$. By induction, $|\Delta_n(t)| \leq \frac{M^n}{n!}(t - t_0)^n$. Hence $\sum |\Delta_n(t)| \leq \sum \frac{M^n}{n!}(t_1 - t_0)^n = e^{M(t_1-t_0)} - 1$.

Since the series converges uniformly, $\varphi_n(t) = \iota + \sum_{k=1}^n \Delta_k(t)$ converges uniformly to a limit $\varphi(t)$. By uniform convergence, taking the limit in the recurrence yields $\varphi(t) = \iota + \int_{t_0}^{t} \psi(t) \circ \varphi(t) \, dt$. Differentiating gives $\dot{\varphi}(t) = \psi(t) \circ \varphi(t)$ and $\varphi(t_0) = \iota$ is immediate.
