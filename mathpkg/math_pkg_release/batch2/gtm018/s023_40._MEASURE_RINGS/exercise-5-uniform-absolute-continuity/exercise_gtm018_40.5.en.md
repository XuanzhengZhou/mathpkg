---
role: exercise
locale: en
chapter: "X"
section: "40"
exercise_number: 5
---

If $\{\nu_n\}$ is a sequence of finite signed measures on $\mathbf{S}$ such that $\nu_n \ll \mu$ and such that $\lim_n \nu_n(E)$ exists and is finite for every $E$ in $\mathbf{S}$, then the set functions $\nu_n$ are uniformly absolutely continuous with respect to $\mu$.

*Hint:* Let $\mathbf{s}$ be the metric space of $(X,\mathbf{S},\mu)$ and write, for each fixed positive number $\epsilon$,

$$\mathcal{E}_k = \bigcap_{n=k}^{\infty} \bigcap_{m=k}^{\infty} \left\{ E: E \in \mathbf{S}, |\nu_n(E) - \nu_m(E)| \leq \frac{\epsilon}{3} \right\}.$$

Since each $\mathcal{E}_k$ is closed, and since $\mathbf{s}$ is a complete metric space, the Baire category theorem implies that there exists a positive integer $k_0$, a positive number $r_0$, and a set $E_0$ in $\mathbf{s}$ such that $\{ E: \rho(E,E_0) < r_0 \} \subset \mathcal{E}_{k_0}$. Let $\delta$ be a positive number such that $\delta < r_0$ and such that $|\nu_n(E)| < \frac{\epsilon}{3}$ whenever $\mu(E) < \delta$ and $n = 1, \cdots, k_0$. Observe that if $\mu(E) < \delta$, then

$$\rho(E_0 - E, E_0) < r_0 \quad \text{and} \quad \rho(E_0 \cup E, E_0) < r_0,$$

and

$$|\nu_n(E)| \leq |\nu_{k_0}(E)| + |\nu_n(E_0 \cup E) - \nu_{k_0}(E_0 \cup E)| + |\nu_n(E_0 - E) - \nu_{k_0}(E_0 - E)|.$$
