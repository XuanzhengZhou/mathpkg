---
role: exercise
locale: en
chapter: "9"
section: "13"
exercise_number: 3
---

Let a recurrent chain $P$ be started in state $0$. Let $\alpha_i^E$ be the mean number of times in state $i$ in the time required to reach the set $E$ and then return to $0$.
(a) Prove that for any set $E$ there is a constant $k_E$ such that $\alpha_i^E = k_E \alpha_i$.
(b) Let $Q$ be the transition matrix for the transient states when $0$ is made absorbing and let $\bar{\alpha}$ be the restriction of $\alpha$ to the transient states. Show that if $E$ does not contain $0$, then $1 - {}_E \bar{H}_{00} = \frac{1}{\alpha_0} \bar{\alpha}[(I - Q)B^E 1]$, where $B^E$ is restricted to the transient states.
(c) Conclude that if $E$ does not contain $0$, then $1/k_E$ is the transient capacity of $E$ in the chain $Q$, provided the distinguished superregular measure is $\bar{\alpha}$.
