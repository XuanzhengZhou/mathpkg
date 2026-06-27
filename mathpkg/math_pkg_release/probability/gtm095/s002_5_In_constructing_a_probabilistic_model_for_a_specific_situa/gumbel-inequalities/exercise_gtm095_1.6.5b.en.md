---
role: exercise
locale: en
chapter: "1"
section: "6"
exercise_number: "5(b)"
---

# Exercise 5(b) — Gumbel's Inequalities

Prove **Gumbel's inequalities**: for $m = 1, 2, \ldots, n$,

$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}},$$

where

$$\tilde{S}_m = \sum_{1 \leq i_1 < \cdots < i_m \leq n} \mathrm{P}(A_{i_1} \cup \cdots \cup A_{i_m}),$$

and $\binom{n-1}{m-1}$ is the binomial coefficient.

*Hint:* For a given outcome $\omega$ belonging to $\nu$ of the events, count how many $m$-tuples of events have a union containing $\omega$. Show that this number is at least $\binom{n-1}{m-1}$ whenever $\nu \geq 1$.
