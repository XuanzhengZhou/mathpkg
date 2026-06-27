---
role: exercise
locale: en
chapter: "8"
section: "37"
exercise_number: 7
---

Prove the following inequalities:

(a) $n(q_1, q_2) \leq \binom{q_1 + q_2 - 2}{q_1 - 1}$;

(b) $n(q_1, \ldots, q_m) \leq \sum_{i=1}^{m} n(q_1 - \delta_{1i}, q_2 - \delta_{2i}, \ldots, q_m - \delta_{mi})$,

where the Kronecker delta $\delta_{ji} = 0$ if $j \neq i$ and 1 if $j = i$;

(c) $n(q_1, \ldots, q_m) \leq \frac{\left[ \sum_{i=1}^{m} (q_i - 1) \right]!}{\prod_{i=1}^{m} [(q_i - 1)!]}$.

We introduce some working terminology for the present section. A graph $\Gamma$ will be called a $(q_1, q_2)$-graph if $\omega(\Gamma) < q_1$ and $\alpha_0(\Gamma) < q_2$. A $(q_1, q_2)$-graph will be called $d$-deficient, or will be said to have deficiency $d$, if $d = n(q_1, q_2) - \nu_0(\Gamma) - 1$. Clearly $d \geq 0$.
