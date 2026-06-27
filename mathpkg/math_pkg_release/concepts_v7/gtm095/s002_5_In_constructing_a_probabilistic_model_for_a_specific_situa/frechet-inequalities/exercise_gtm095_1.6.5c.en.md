---
role: exercise
locale: en
chapter: "1"
section: "6"
exercise_number: "5(c)"
---

# Exercise 5(c) — Frechet's Inequalities

Prove **Frechet's inequalities**: for $m = 1, 2, \ldots, n-1$,

$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_{m+1}}{\binom{n-1}{m}} \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}},$$

where $\tilde{S}_m$ is defined as in part (b). These inequalities show that the Gumbel bounds form a monotonically decreasing sequence.

*Hint:* Use part (b) for the first inequality. For the second, show the equivalent inequality
$$\binom{n-1}{m-1} \tilde{S}_{m+1} \leq \binom{n-1}{m} \tilde{S}_m$$
by comparing the contributions of each outcome $\omega$ to both sides, using properties of binomial coefficients.
