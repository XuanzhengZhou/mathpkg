---
role: proof
locale: en
of_concept: prop-t-b-bty-t-b-byt
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: Consider the reversed random walk with transition function $P^*(x,y) = P(y,x)$. If we call $\Pi_B^*(x,y)$ what one gets if one forms $\Pi_B$ for the transition function $P^*$ in accordance with D10.1, then by P1

for every aperiodic recurrent random walk. Here it is convenient to use the measure theoretical definition of $\Pi_B$, giving

$$\sum_{y \in B} \Pi_B(x,y) = P_z[T_B < \infty] \geq P_z[T_z < \infty],$$

since $T_z = \min [k \mid 1 \leq k \leq \infty; x_k = x] \geq T_B$. But

$$P_z[T_z < \infty] = \sum_{k=1}^{\infty} F_k(x,x) = \sum_{k=1}^{\infty} F_k(0,0) = F$$

in the terminology of section 1, and $F = 1$ since the process is recurrent. That completes the proof.

Now P2 opens up an important possibility. It enables us to transform P1 into

$$\sum_{t \in R} P_{n+1}(x,t)H_B(t,y)$$

$$= H_B(x,y) + \sum_{t \in B}[c_n + G_n(x,t)][\Pi_B(t,y) - \delta(t,y)]$$

where the $c_n$ are arbitrary constants (independent of $t$). We choose to let $c_n = -G_n(0,0)$ and define
