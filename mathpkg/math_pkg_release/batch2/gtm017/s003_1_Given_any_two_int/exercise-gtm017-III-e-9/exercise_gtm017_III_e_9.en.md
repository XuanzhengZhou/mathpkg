---
role: exercise
locale: en
chapter: "III"
section: "e"
exercise_number: 9
---

Show that if the characteristic function $\varphi(t)$ is differentiable up to order $2n$, then $P[|X| \geq t] = o(t^{-2n})$ as $t \to \infty$. The differentiability of $\varphi$ at even orders implies the existence of moments up to that order, which by Markov's inequality gives the tail bound. Specifically, if $E[X^{2n}] < \infty$, then $P(|X| \geq t) \leq E[X^{2n}]/t^{2n}$.
