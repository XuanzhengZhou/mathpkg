---
role: proof
locale: en
of_concept: theorem-1-9
source_book: gtm011
source_chapter: "Complex Integration"
source_section: "1. Riemann-Stieltjes integrals"
---

Proof. Again we only consider the case where $\gamma$ is smooth. Also, by looking at the real and imaginary parts of $\gamma$, we reduce the proof to the case where $\gamma([a,b]) \subset \mathbb{R}$. Let $\epsilon > 0$ and choose $\delta > 0$ such that if $P = \{a = t_0 < \ldots < t_n = b\}$ has $\|P\| < \delta$ then

1.10 $$\left| \int_a^b fd\gamma - \sum_{k=1}^n f(\tau_k) [\gamma(t_k) - \gamma(t_{k-1})] \right| < \frac{1}{2}\epsilon$$

and

1.11 $$\left| \int_a^b f(t)\gamma'(t) dt - \sum_{k=1}^n f(\tau_k)\gamma'(\tau_k)(t_k - t_{k-1}) \right| < \frac{1}{2}\epsilon$$

for any choice of $\tau_k$ in $[t_{k-1}, t_k]$. If we apply the Mean Value Theorem for derivatives we get that there is a $\tau_k$ in $[t_{k-1}, t_k]$ with $\gamma'(\tau_k) = [\gamma(t_k) - \gamma(t_{k-1})](t_k - t_{k-1})^{-1}$. (Note that the fact that $\gamma$ is real valued is needed to apply the Mean Value Theorem.) Thus,

$$\sum_{k=1}^n f(\tau_k) [\gamma(t_k) - \gamma(t_{k-1})] = \sum_{k=1}^n f(\tau_k)\gamma'(\tau_k)(
