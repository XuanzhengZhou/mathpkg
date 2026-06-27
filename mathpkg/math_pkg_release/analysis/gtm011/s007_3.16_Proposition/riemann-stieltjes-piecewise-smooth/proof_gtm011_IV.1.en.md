---
role: proof
locale: en
of_concept: riemann-stieltjes-piecewise-smooth
source_book: gtm011
source_chapter: "IV"
source_section: "1"
---

We consider the case where $\gamma$ is smooth; the piecewise smooth case follows by summing over the smooth subintervals. By decomposing into real and imaginary parts, it suffices to consider the case $\gamma([a,b]) \subset \mathbb{R}$.

Let $\epsilon > 0$. By Theorem 1.4, choose $\delta > 0$ such that if $P = \{a = t_0 < \cdots < t_n = b\}$ has $\|P\| < \delta$, then

$$\left| \int_a^b f \, d\gamma - \sum_{k=1}^n f(\tau_k) [\gamma(t_k) - \gamma(t_{k-1})] \right| < \frac{\epsilon}{2}$$

and

$$\left| \int_a^b f(t) \gamma'(t) \, dt - \sum_{k=1}^n f(\tau_k) \gamma'(\tau_k) (t_k - t_{k-1}) \right| < \frac{\epsilon}{2}$$

for any choice of $\tau_k \in [t_{k-1}, t_k]$.

Since $\gamma$ is real-valued and differentiable, the Mean Value Theorem implies that for each $k$ there exists $\tau_k \in [t_{k-1}, t_k]$ such that

$$\gamma'(\tau_k) = \frac{\gamma(t_k) - \gamma(t_{k-1})}{t_k - t_{k-1}}.$$

Thus,

$$\sum_{k=1}^n f(\tau_k) [\gamma(t_k) - \gamma(t_{k-1})] = \sum_{k=1}^n f(\tau_k) \gamma'(\tau_k) (t_k - t_{k-1}).$$

Combining the inequalities yields

$$\left| \int_a^b f \, d\gamma - \int_a^b f(t) \gamma'(t) \, dt \right| < \epsilon.$$

Since $\epsilon > 0$ is arbitrary, the two integrals are equal.
