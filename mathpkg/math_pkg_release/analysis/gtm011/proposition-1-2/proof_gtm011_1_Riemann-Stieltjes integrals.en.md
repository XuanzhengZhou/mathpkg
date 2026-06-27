---
role: proof
locale: en
of_concept: proposition-1-2
source_book: gtm011
source_chapter: "Complex Integration"
source_section: "1. Riemann-Stieltjes integrals"
---

Proof. Assume that $\gamma$ is smooth (the complete proof is easily deduced from this). Recall that when we say that $\gamma$ is smooth this means $\gamma'$ is continuous.

Let $P = \{a = t_0 < t_1 < \ldots < t_m = b\}$. Then, from the definition,

$$v(\gamma; P) = \sum_{k=1}^{m} |\gamma(t_k) - \gamma(t_{k-1})|$$

$$= \sum_{k=1}^{m} \left| \int_{t_{k-1}}^{t_k} \gamma'(t) \, dt \right|$$

$$\leq \sum_{k=1}^{m} \int_{t_{k-1}}^{t_k} |\gamma'(t)| \, dt$$

$$= \int_{a}^{b} |\gamma'(t)| \, dt$$

Hence $V(\gamma) \leq \int_a^b |\gamma'(t)| \, dt$, so that $\gamma$ is of bounded variation.

Since $\gamma'$ is continuous it is uniformly continuous; so if $\epsilon > 0$ is given we can choose $\delta_1 > 0$ such that $|s-t| < \delta_1$ implies that $|\gamma'(s) - \gamma'(t)| < \epsilon$. Also, we may choose $\delta_2 > 0$ such that if $P = \{a = t_0 < t_1 < \ldots < t_m = b\}$ and $\|P\| = \max \{(t_k - t_{k-1}): 1 \leq k \leq m\} < \delta_2$ then

$$\left| \int_a^b |\gamma'(t)| \, dt - \sum_{k=1}^{m} |\gamma'(\tau_k)| (t_k - t_{k-1}) \right| < \epsilon$$

where $\tau_k$ is any point in $[t_{k-1}, t_k]$. Hence

$$\int_a^b |\gamma'(t)| \, dt \leq \epsilon + \sum_{k=1}^{m} |\gamma'(\tau_k)| (t

Letting $\epsilon \to 0+$, gives

$$\int_{a}^{b} |\gamma'(t)| dt \leq V(\gamma),$$

which yields equality.
