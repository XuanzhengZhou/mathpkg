---
role: proof
locale: en
of_concept: total-variation-of-smooth-curve
source_book: gtm011
source_chapter: "IV"
source_section: "1"
---

Let $P = \{a = t_0 < t_1 < \ldots < t_m = b\}$ be any partition of $[a, b]$. Then

$$v(\gamma; P) = \sum_{k=1}^{m} |\gamma(t_k) - \gamma(t_{k-1})|
= \sum_{k=1}^{m} \left| \int_{t_{k-1}}^{t_k} \gamma'(t) \, dt \right|
\leq \sum_{k=1}^{m} \int_{t_{k-1}}^{t_k} |\gamma'(t)| \, dt
= \int_{a}^{b} |\gamma'(t)| \, dt.$$

Taking the supremum over all partitions $P$ yields $V(\gamma) \leq \int_a^b |\gamma'(t)| \, dt$, so $\gamma$ is of bounded variation.

For the reverse inequality, since $\gamma'$ is continuous on $[a, b]$, it is uniformly continuous. Given $\epsilon > 0$, choose $\delta_1 > 0$ such that $|s - t| < \delta_1$ implies $|\gamma'(s) - \gamma'(t)| < \epsilon$. Also choose $\delta_2 > 0$ such that if $\|P\| < \delta_2$, then

$$\left| \int_a^b |\gamma'(t)| \, dt - \sum_{k=1}^{m} |\gamma'(\tau_k)| (t_k - t_{k-1}) \right| < \epsilon$$

for any choice of $\tau_k \in [t_{k-1}, t_k]$. Hence

$$\int_a^b |\gamma'(t)| \, dt \leq \epsilon + \sum_{k=1}^{m} |\gamma'(\tau_k)| (t_k - t_{k-1}).$$

Now, for each subinterval $[t_{k-1}, t_k]$,

$$|\gamma(t_k) - \gamma(t_{k-1})| = \left| \int_{t_{k-1}}^{t_k} \gamma'(t) \, dt \right|
\geq \left| \int_{t_{k-1}}^{t_k} |\gamma'(\tau_k)| \, dt \right| - \int_{t_{k-1}}^{t_k} |\gamma'(t) - \gamma'(\tau_k)| \, dt.$$

Choosing the partition with $\|P\| < \min(\delta_1, \delta_2)$ and using uniform continuity,

$$\int_a^b |\gamma'(t)| \, dt \leq \epsilon + \sum_{k=1}^{m} (|\gamma(t_k) - \gamma(t_{k-1})| + \epsilon(t_k - t_{k-1}))
\leq \epsilon + V(\gamma) + \epsilon(b - a).$$

Letting $\epsilon \to 0+$ gives $\int_a^b |\gamma'(t)| \, dt \leq V(\gamma)$, which together with the first inequality yields equality.
