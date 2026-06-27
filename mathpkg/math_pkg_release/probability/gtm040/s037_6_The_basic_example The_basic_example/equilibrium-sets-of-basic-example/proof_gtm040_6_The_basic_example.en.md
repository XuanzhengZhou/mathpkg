---
role: proof
locale: en
of_concept: equilibrium-sets-of-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

For $P$, let $E$ be a finite set with $m$ as its last element. The equilibrium potential $e^E$ satisfies $e^E = (I-P)h^E$ where $h^E_i$ is the probability of hitting $E$ starting from $i$. For $i > m$, the only way to avoid hitting $E$ is to march straight out to the right without ever returning to 0, which has probability $\beta_\infty/\beta_i$. Hence:

$$h^E_i = 1 - \frac{\beta_\infty}{\beta_i} \quad \text{for } i > m.$$

Computing $e^E = (I-P)h^E$ yields the equilibrium measure concentrated on $E$ with total mass (capacity) $C(E) = \beta_\infty$.

If $E$ is infinite, then the chain will visit $E$ infinitely often almost surely, so $h^E \equiv 1$. Then $e^E = (I-P)1 = 0$, which cannot be a non-zero charge, so $E$ is not an equilibrium set. The fact that the supremum of capacities of finite subsets of an infinite set $E$ equals $\beta_\infty$ does not contradict Proposition 8-39, since $\hat{N}$ does not have columns tending to zero (a required condition in that proposition).

For $\hat{P}$, let $E$ be any set with least element $m$. Then $\hat{h}^E_i = 1$ for $i \geq m$. For $i < m$:

$$\hat{h}^E_i = \hat{h}^E_0 = \hat{H}_{0m} = \frac{\hat{N}_{0m}}{\hat{N}_{mm}} = \frac{(\beta_m/\beta_\infty) - 1}{\beta_m/\beta_\infty} = 1 - \frac{\beta_\infty}{\beta_m}.$$

The equilibrium charge $\hat{e}^E = (I - \hat{P})\hat{h}^E$ is non-zero and concentrated at $m$ (and possibly at 0 if $m=0$), confirming that every set is an equilibrium set for $\hat{P}$.
