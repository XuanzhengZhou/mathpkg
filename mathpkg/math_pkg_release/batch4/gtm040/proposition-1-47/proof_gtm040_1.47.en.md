---
role: proof
locale: en
of_concept: proposition-1-47
source_book: gtm040
source_chapter: "1"
source_section: "47"
---

**Proof:** Set $f_n = \min(f, n)$. By Theorem 1-44,

$$\lim_n \int_X f_n d\mu = \int_X f_d\mu.$$

Since $f$ is integrable, we may find an $N$ such that

$$\int_X (f - f_N) d\mu < \frac{\epsilon}{2}$$

by Proposition 1-45. Let $\delta = \epsilon/(2N)$. If $\mu(E) < \delta$, then

$$\int_E f d\mu = \int_E (f - f_N) d\mu + \int_E f_N d\mu \quad \text{by Proposition 1-45}$$
$$\leq \int_X (f - f_N) d\mu + N\mu(E) \quad \text{by Proposition 1-39}$$
$$< \epsilon.$$

Our third theorem for this section is known as Fatou's Theorem.
